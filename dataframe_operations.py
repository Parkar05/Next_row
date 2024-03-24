#!/usr/bin/env python
# coding: utf-8

# In[6]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By 

import selenium 
import pandas as pd
import numpy as np
import numpy.random as nr
import itertools

from pathlib import Path
import json
import os

import re

import os
import pickle

import time as t
from time import sleep


import warnings
warnings.filterwarnings('ignore')


# In[2]:


df = pd.read_csv("test.csv")
df.head()


# In[3]:


df.columns

driver = webdriver.Chrome()
chrome_driver_path = "chromedriver.exe"
service = Service(chrome_driver_path)
# In[5]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from pathlib import Path
import json
import pandas as pd

# Initialize WebDriver and perform LinkedIn login
def initialize_driver():
    driver = webdriver.Chrome()
    driver.get("https://linkedin.com/uas/login")
    sleep(3)

    if not Path('cookies.json').is_file():
        # Enter username
        username = driver.find_element(By.ID, "username")
        username.send_keys("mohammedaliparkar123@gmail.com")
        sleep(3)
        
        # Enter password
        password = driver.find_element(By.ID, "password")
        password.send_keys("Mohammedali@123")
        sleep(5)
        
        # Click submit button
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        sleep(60)  # Wait for login to complete

        Path('cookies.json').write_text(
            json.dumps(driver.get_cookies(), indent=2)
        )
    else:
        for cookie in json.loads(Path('cookies.json').read_text()):
            driver.add_cookie(cookie)

        driver.refresh()

    return driver

# Function to process each row
def process_row(row):
    try:
        # Extract data from the row
        lead_id = row['leadid']
        contact_link = row['contactlink']
        comp_link = row['complink']
        address_link = row['addresslink']

        # Process the row (replace this with your actual processing logic)
        driver.get(contact_link)
        sleep(5)  
        driver.get(comp_link)
        sleep(5)
        driver.get(address_link)
        sleep(5) 

        # Perform operations using Selenium
        # Example:
        # Your Selenium operations here

        # Return any processed data if needed
        return "Processing successful"  # Placeholder, replace with actual processed data

    except Exception as e:
        # Log any errors
        error_message = str(e)
        print(f"Error processing row {lead_id}: {error_message}")

        # Return any error message or indicator
        return f"Processing failed: {error_message}"  # Placeholder, replace with actual error handling

# Load your dataset
data = pd.read_csv("test.csv")

# Initialize WebDriver and perform LinkedIn login
driver = initialize_driver()

# Apply the process_row function to each row using the apply function
processed_data = data.apply(process_row, axis=1)

# Log the processing status
print(processed_data)

# Quit the WebDriver session after processing
driver.quit()


# ### Using Loop 

# In[ ]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from pathlib import Path
import json
import pandas as pd

# Initialize WebDriver and perform LinkedIn login
def initialize_driver():
    driver = webdriver.Chrome()
    driver.get("https://linkedin.com/uas/login")
    sleep(3)

    if not Path('cookies.json').is_file():
        # Enter username and password
        driver.find_element(By.ID, "username").send_keys("mohammedaliparkar123@gmail.com")
        sleep(3)
        driver.find_element(By.ID, "password").send_keys("Mohammedali@123")
        sleep(5)
        
        # Click submit button
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        sleep(60)  # Wait for login to complete

        # Save cookies to file
        Path('cookies.json').write_text(json.dumps(driver.get_cookies(), indent=2))
    else:
        # Load cookies from file
        for cookie in json.loads(Path('cookies.json').read_text()):
            driver.add_cookie(cookie)

        driver.refresh()

    return driver

# Function to process each row
def process_row(row, driver):
    try:
        # Extract data from the row
        lead_id = row['leadid']
        contact_link = row['contactlink']
        comp_link = row['complink']
        address_link = row['addresslink']

        # Process the row
        for link in [contact_link, comp_link, address_link]:
            driver.get(link)
            sleep(5)  

        # Return success message
        return "Processing successful"  

    except Exception as e:
        # Log any errors
        error_message = str(e)
        print(f"Error processing row {lead_id}: {error_message}")

        # Return error message
        return f"Processing failed: {error_message}"  

# Load your dataset
data = pd.read_csv("test.csv")

# Initialize WebDriver and perform LinkedIn login
driver = initialize_driver()

# Apply the process_row function to each row using the apply function
processed_data = data.apply(lambda row: process_row(row, driver), axis=1)

# Log the processing status
print(processed_data)

# Quit the WebDriver session after processing
driver.quit()

