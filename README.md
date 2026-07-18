# Baseball Betting Statistics Web Scraper

This project is an automated web scraping and data processing tool developed as a practical project within the **Automation and Scripting with Python** curriculum, a component of the **Microsoft Python Development Professional Certificate** program on Coursera. It automates the collection, extraction, parsing, and structuring of sports performance and betting metrics from web elements.

---

## Technical Specifications and Scope

### Academic and Professional Credential Context
* Certification Program: Microsoft Python Development Professional Certificate
* Platform Provider: Coursera
* Course Focus: Automation and Scripting with Python, Data Parsing, and Document Automation

### Data Engineering and Scraping Architecture
* Network Transport: Requests library handling automated local HTML structure fetching
* Content Parsing Engine: BeautifulSoup4 paired with the Lxml processing library
* Target Extraction Layout: Direct multi-column HTML data tables and nested matrix elements
* Data Manipulation & Storage: Pandas framework converting unstructured strings into organized data arrays

---

## Project Performance and Quantifiable Data Points

When preparing resume bullet points or project metrics, utilize the following structural details from this codebase:

### 1. Extracted Metric Scope
* Metrics Targeted: Programmed data maps to extract 5 distinct variables per entry: Game ID, Team Names, Expected Runs, Over/Under Bets, and Moneyline Favorites.
* Script Modularity: Engineered 1 central automation file (`main.py`) containing the complete collection, cleaning, and storage operations.

### 2. Output Data Engineering
* Data Structure Conversion: Converts raw unstructured string data into multi-key Python dictionaries.
* File Production: Automates a spreadsheet pipeline generating 1 structured output dataset (`sports_statistics.csv`) for subsequent analytics.

---

## Project Execution Guide

### 1. Local Environment Deployment
Install the required parsing and automation dependencies to establish the script execution environment:
```bash
pip install bs4 pandas lxml requests
```

### 2. Script Execution
Run the core automation script to process and export the sports metrics:
```bash
python3 main.py
```
