# 🌍 World Bank Data360 Scraper

This project is a Python-based web scraper that extracts dataset information from the World Bank Data360 platform.

It uses **Selenium** for browser automation and **BeautifulSoup** for parsing HTML content.

---

## 🚀 Features

* Scrapes data from multiple pages (up to 100 pages)
* Extracts:

  * Dataset Name
  * Update Details
  * Disaggregations
  * Database Name
  * PDF Download Links
  * Dataset Page Links
* Automatically navigates through pagination
* Stores extracted data into a CSV file

---

## 🛠️ Tech Stack

* Python
* Selenium
* BeautifulSoup
* Pandas

---

## 📂 Project Structure

```
world-bank-scraper/
│
├── scrap-worldbank.py      # Main scraping script
├── world_bank_data.csv     # Output file (generated after running)
└── README.md               # Project documentation
```

---

## ▶️ How to Run

### 1. Clone the repository

```
git clone https://github.com/your-username/world-bank-scraper.git
```

### 2. Install dependencies

```
pip install selenium pandas beautifulsoup4
```

### 3. Setup ChromeDriver

Download ChromeDriver and update the path in your script:

```python
s = Service("C:/Windows/chromedriver.exe")
```

Make sure:

* ChromeDriver version matches your Chrome browser

---

### 4. Run the script

```
python scrap-worldbank.py
```

---

## 📊 Output

After execution, a CSV file will be generated:

```
world_bank_data.csv
```

It contains structured dataset information scraped from the website.

---

## ⚠️ Notes

* The scraper is limited to **100 pages** (can be modified in code)
* Add delays if scraping large data to avoid blocking
* Ensure stable internet connection during execution

---

## 👤 Author

Abhilash Alle

