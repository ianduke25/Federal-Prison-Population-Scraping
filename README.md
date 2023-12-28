Federal Prison Data Scraper: ReadMe
Overview
This Python script is designed to scrape data from all facility-level Bureau of Prisons (BOP) websites. It collects daily information including population size, visiting status, and operation levels of each individual federal facility. This tool is particularly useful for researchers, legal professionals, and journalists who require up-to-date information on Bureau of Prison facility operating status and population sizes.
Features
Scrapes population, visiting status, and operation levels of federal prisons.
Efficiently handles multiple requests using Selenium WebDriver with a headless Chrome browser.
Incorporates random user-agent generation for each session to reduce the likelihood of being blocked by anti-scraping mechanisms.
Outputs data in a structured CSV format for easy analysis and visualization.
Includes a logging system to track data collection dates and times.
Prerequisites
Python 3.x
Pandas
Selenium
ChromeDriver
WebDriver-Manager
pytz
fake_useragent
Output
The script outputs a CSV file named facilities_<timestamp>.csv, where <timestamp> is the date and time of the data collection. The CSV file includes the following columns:
Title
Population
Operation Level
Visiting Status
Datetime of Data
Historical Data
Data has been intermittently collected since September 27, 2023. For access to archived data, please contact Ian Duke. Include in your request a brief description of the intended use of the data.
Disclaimer
This script is intended for educational and research purposes only. Users are responsible for ensuring compliance with any terms of service or usage policies of the websites being scraped.
