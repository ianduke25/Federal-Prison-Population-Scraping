# Federal Prison Data Scraper: ReadMe

## Overview
This Python script is designed to scrape data from all facility-level Bureau of Prisons (BOP) websites. It collects daily information including population size, visiting status, and operation levels of each individual federal facility. This tool is particularly useful for researchers, legal professionals, and journalists who require up-to-date information on BOP facility operating status and population sizes.

## Features
- Scrapes population, visiting status, and operation levels of federal prisons.
- Efficiently handles multiple requests using Selenium WebDriver with a headless Chrome browser.
- Incorporates random user-agent generation for each session to reduce the likelihood of being blocked by anti-scraping mechanisms.
- Outputs data in a structured CSV format for easy analysis and visualization.
- Includes a logging system to track data collection dates and times.

## Prerequisites
- Python 3.11.3
- Pandas
- Selenium
- ChromeDriver
- WebDriver-Manager
- pytz
- fake_useragent
  
## Output
The script outputs a CSV file named facilities_[timestamp].csv, where [timestamp] is the date and time of the data collection. The CSV file includes the following columns:
- Title
- Population
- Operation Level
- Visiting Status
- Datetime of Data

## Usage Instructions
To use the facility_info_scraper.py script, follow these steps:

### Step 1: Set Up Your Environment
Ensure Python 3.11.3 is installed on your system.

Install the required Python packages: Pandas, Selenium, WebDriver-Manager, pytz, and fake_useragent. You can install these using pip:

-*pip install pandas selenium webdriver_manager pytz fake_useragent*
  
### Step 2: Download ChromeDriver
The script requires ChromeDriver to interact with the Chrome browser. Ensure you have ChromeDriver that matches your Chrome browser version. It can be downloaded from ChromeDriver's website.

### Step 3: Running the Script
Navigate to the directory containing facility_info_scraper.py.

Run the script using Python:

-*python facility_info_scraper.py*

## Historical Data
Data has been intermittently collected since September 27, 2023. For access to archived data, please email Ian Duke directly. Include in your request a brief description of the intended use of the data.

## Disclaimer
This script is intended for educational and research purposes only. Users are responsible for ensuring compliance with any terms of service or usage policies of the websites being scraped.
