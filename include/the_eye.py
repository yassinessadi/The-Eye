from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import validators

# Initialize Selenium WebDriver
service = Service("C://chromedriver//chromedriver.exe")
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Ask user to input website URL
while True:
    url = input("Enter the website URL: ")
    if validators.url(url):
        break
    else:
        print("Invalid URL. Please enter a valid URL.")

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


# Loop to collect search result URLs from multiple pages
search_results = []

while True:
    # Extract search result URLs from the current page
    search_elems = driver.find_elements(By.XPATH, "//div[@class='tF2Cxc']")
    
    for elem in search_elems:
        link = elem.find_element(By.TAG_NAME, "a").get_attribute("href")
        search_results.append(link)
        print("Added link:", link)
    
    # Check if there is a 'Next' button
    next_button = driver.find_elements(By.XPATH, "//a[@id='pnnext']")
    if len(next_button) == 0:
        break
    
    # Click 'Next' button to go to the next page
    next_button[0].click()
    time.sleep(3)  # Wait for the next page to load

# Print all collected search result URLs
print("\nCollected Search Result URLs:")
for idx, link in enumerate(search_results, start=1):
    print(f"{idx}. {link}")