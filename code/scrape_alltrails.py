import os
import csv
import requests
import statistics

from pprint import pprint

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def extract_trail_soup_selenium(location):
    # Configure Selenium WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no browser UI)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    
    # Set up the WebDriver
    service = Service("C:\\Users\\rjiso\\OneDrive\\Desktop\\main\\ut\\code\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open the AllTrails URL
    url = f"https://www.alltrails.com/explore/us/{location}"
    driver.get(url)

    # Allow time for JavaScript to load
    time.sleep(10)  # Adjust based on your internet speed and page complexity

    # Get the HTML content
    html = driver.page_source
    driver.quit()

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    return soup

def get_trail_cards_from_soup(soup):
    trail_cards = soup.find_all("div", class_="VTOs0Uy8IXamcLOuKqgjjA==")

location = "texas/austin"
soup = extract_trail_soup_selenium(location)
print(soup.prettify())