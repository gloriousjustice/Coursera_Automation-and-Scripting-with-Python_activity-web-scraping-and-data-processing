# Coursera_Automation-and-Scripting-with-Python_activity-web-scraping-and-data-processing
# Baseball Betting Statistics Web Scraper

A Python-based web scraping tool that automates the collection, extraction, and structuring of baseball game statistics and betting data from web elements.

## Features
* **Automated Extraction**: Fetches live local HTML structures using `requests`.
* **HTML Parsing**: Uses `BeautifulSoup` to break down multi-column table data.
* **Data Structuring**: Converts raw unstructured string data into clear Python dictionaries.
* **Spreadsheet Export**: Formats statistics using `pandas` and exports cleanly to a structured CSV file.

## Tech Stack
* **Language**: Python 3
* **Libraries**: BeautifulSoup4, Pandas, Requests, Lxml

## Project Structure
* `main.py`: The core automation script containing data collection, cleaning, and storage operations.
* `sports_statistics.csv`: The finalized output dataset containing structured sports metrics.

## Extracted Metrics
The script targets and parses the following data points for each game:
* Game ID
* Team 1 & Team 2 Names
* Expected Runs (for both teams)
* Over/Under Bets
* Moneyline Favorite Team

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gloriousjustice/Coursera_Automation-and-Scripting-with-Python_activity-web-scraping-and-data-processing
   cd https://github.com/gloriousjustice/Coursera_Automation-and-Scripting-with-Python_activity-web-scraping-and-data-processing
   ```

2. **Install dependencies:**
   ```bash
   pip install bs4 pandas lxml requests
   ```

3. **Run the script:**
   ```bash
   python3 main.py
   ```
