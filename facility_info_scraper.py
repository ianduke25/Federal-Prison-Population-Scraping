from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv
import pandas as pd
from datetime import datetime
import pytz
from fake_useragent import UserAgent


# manually clean up csv and import
# NOTE: replace with local filepath to facilities.csv
bop_facilities = pd.read_csv('./facilities.csv')

# create list of facilities
facility_list = bop_facilities['facilities']

# Initialize UserAgent
ua = UserAgent()

list_of_dictionaries = []

# Initialize the webdriver outside the loopto avoid opening a new browser
# for each URL.
chrome_options = Options()

# Add the headless argument to run Chrome in the background
chrome_options.add_argument("--headless")

# Assign a random user agent for the driver
chrome_options.add_argument(f"user-agent={ua.random}")

driver = webdriver.Chrome(
    executable_path=ChromeDriverManager().install(),
    options=chrome_options)

for i in range(len(facility_list)):
    facility_dictionary = {}
    url = facility_list[i]
    print(url)

    driver.get(url)

    time.sleep(10)

    title_tag = driver.find_element(By.XPATH, '//*[@id="title_cont"]/h2')
    title = title_tag.text

    population_tag = driver.find_element(By.XPATH, '//td[@id="pop_count"]')
    population = population_tag.text

    operations_tag = driver.find_element(By.XPATH, '//*[@id="ops_level"]/a')
    level = operations_tag.get_attribute('title')

    suspension_tag = driver.find_element(By.XPATH, '//*[@id="notice_cont"]/h3')
    suspension = suspension_tag.text

    # Get the current datetime and make it timezone-aware using the system's
    # local timezone
    current_datetime = datetime.now().astimezone(pytz.utc).astimezone()
    # Format the datetime with timezone
    formatted_datetime_with_tz = current_datetime.strftime(
        '%Y-%m-%d %H:%M:%S %Z')

    facility_dictionary['title'] = title
    facility_dictionary['population'] = population
    facility_dictionary['operation_level'] = level

    if len(suspension) > 0:
        facility_dictionary['visiting_status'] = 'Suspended'
    else:
        facility_dictionary['visiting_status'] = 'Not Suspended'

    facility_dictionary['datetime_of_data'] = formatted_datetime_with_tz

    list_of_dictionaries.append(facility_dictionary)

    # Delay between requests
    time.sleep(5)  # waits for 5 seconds to allow page to fully load

driver.quit()

# Specify the directory and filename for the CSV
# Get the current datetime and make it timezone-aware using the system's
# local timezone
current_datetime = datetime.now().astimezone(pytz.utc).astimezone()
# Format the datetime with timezone
formatted_datetime_with_tz = current_datetime.strftime(
    '%Y-%m-%d %H:%M:%S %Z').replace(':', '_').replace(' ', '_')
file_name = "facilities_" + formatted_datetime_with_tz + ".csv"
base_path = "./"
filename = base_path + file_name

# Write the data to the CSV
with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            'title',
            'population',
            'operation_level',
            'visiting_status',
            'datetime_of_data'])
    writer.writeheader()
    for facility_info in list_of_dictionaries:
        writer.writerow(facility_info)


###If script runs all the way through, log datetime of collection###
# Read the log
log_df = pd.read_csv(
    './collection_log.csv')

# Get the current datetime and make it timezone-aware using the system's
# local timezone
current_datetime = datetime.now().astimezone(pytz.utc).astimezone()
# Format the datetime with timezone
formatted_datetime_with_tz = current_datetime.strftime('%Y-%m-%d %H:%M:%S %Z')

# Append new date to the DataFrame
log_df = log_df._append(
    {'collection_datetime': formatted_datetime_with_tz}, ignore_index=True)

# Write the updated log to the CSV
log_df.to_csv('./collection_log.csv',index=False)
