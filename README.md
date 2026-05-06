# Scraping & API Data Pipeline Project

## Overview
This project demonstrates an end-to-end data pipeline that combines web scraping and API data extraction, followed by data cleaning, transformation, and storage.

The main objective is to collect data from multiple sources, process it, and store it in structured formats suitable for analysis.

---

## Project Workflow

### 1. Web Scraping
- The script uses Selenium to extract data from:
  https://books.toscrape.com/
- Extracted data includes:
  - Book title
  - Book price
- The scraped data is saved in a CSV file named `books.csv`.

---

### 2. API Data Extraction
- Data is fetched from the following API:
  https://dummyjson.com/products
- Extracted fields:
  - Product title
  - Price
- The raw API response is stored in `products.json`.

---

### 3. Data Cleaning and Transformation
- The scraped and API data are loaded using Pandas.
- Data preprocessing steps include:
  - Removing currency symbols
  - Converting price values to numeric format
  - Handling missing values
  - Removing duplicate records
  - Standardizing text formatting (lowercasing and trimming whitespace)

---

### 4. Data Integration
- The two datasets (scraped data and API data) are merged into a single dataset.
- The final cleaned dataset is saved as `final.csv`.

---

### 5. Database Storage
- The cleaned dataset is stored in a SQLite database using SQLAlchemy.
- Database file: `products.db`
- Table name: `cleaned_products`

---

## Technologies Used
- Python
- Selenium
- Requests
- Pandas
- CSV
- SQLAlchemy
- SQLite

---

## Output Files
- `books.csv` — Scraped website data
- `products.json` — Raw API data
- `final.csv` — Cleaned and merged dataset
- `products.db` — SQLite database containing final structured data

---

## Project Objective
This project was developed to practice and demonstrate skills in:
- Web scraping using Selenium
- API data extraction using Requests
- Data cleaning and preprocessing using Pandas
- Data integration from multiple sources
- Storing data in both file-based and database systems
