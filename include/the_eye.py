from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time

# Initialize Selenium WebDriver
service = Service("C://chromedriver//chromedriver.exe")
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Ask user to input website URL
url = input("Enter the website URL: ")

# Use BeautifulSoup to parse the website and extract data
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Example: Extracting titles from the website
titles = soup.find_all('title')
for title in titles:
    print("Title:", title.text)

# Use Selenium to automate workflow based on extracted data
# For demonstration, let's assume we are searching for the extracted title on Google
driver.get("https://www.google.com/")
time.sleep(3)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(titles[0].text)
search_box.send_keys(Keys.ENTER)


