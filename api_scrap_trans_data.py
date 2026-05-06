import requests
import pandas as pd
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from sqlalchemy import create_engine

def run_full():
    print("start scraping")

    driver = webdriver.Chrome()
    driver.get("https://books.toscrape.com/")

    scraped_data = []

    items = driver.find_elements(By.CLASS_NAME, "product_pod")[:10]

    with open("books.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price"])

        for item in items:
            title = item.find_element(
                By.CSS_SELECTOR, "h3 a"
            ).get_attribute("title")

            price = item.find_element(
                By.CLASS_NAME, "price_color"
            ).text

            writer.writerow([title, price])
            scraped_data.append([title, price])

    driver.quit()

    df_scraped = pd.DataFrame(scraped_data, columns=["title", "price"])

    print("Scraping completed. Data saved to books.csv")

    product_list = []

    try:
        url_api = "https://dummyjson.com/products"

        response = requests.get(url_api, timeout=10)
        response.raise_for_status()

        data = response.json()
        product_list = data.get("products", [])

        df_api = pd.DataFrame(product_list)[["title", "price"]]

        print("Successfully fetched data from API")
        print("Total products:", len(df_api))

        df_api.to_json("products.json", orient="records", indent=4)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")

        df_api = pd.DataFrame(columns=["title", "price"])

    print("cleaning started")

    df_scraped["price"] = df_scraped["price"].str.replace("£", "").astype(float)
    df_api["price"] = df_api["price"].astype(float)

    final_df = pd.concat([df_scraped, df_api], ignore_index=True)

    final_df = final_df.drop_duplicates(subset=["title"], keep="first")
    final_df["title"] = final_df["title"].str.strip().str.lower()
    final_df["price"] = final_df["price"].fillna(0)

    print("start saving to csv")
    final_df.to_csv("final.csv", index=False)

    print("saving to sqlite database")

    sql_engine = create_engine('sqlite:///products.db')

    final_df.to_sql(
        'cleaned_products',
        con=sql_engine,
        if_exists="replace",
        index=False
    )


run_full()