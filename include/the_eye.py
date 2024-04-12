from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import validators
import pandas as pd

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
# while True:
#     url = input("Enter the search engine URL: ")
#     if validators.url(url):
#         break
#     else:
#         print("Invalid URL. Please enter a valid URL.")
# For demonstration, let's assume we are searching for the extracted title on Google
driver.get("https://www.google.com")
time.sleep(3)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(titles[0].text)
search_box.send_keys(Keys.ENTER)


scrolls = 0
max_scrolls = 10  # Maximum number of scrolls to perform
last_scroll_height = driver.execute_script("return document.body.scrollHeight")

# Loop to collect search result URLs from multiple pages by scrolling
search_results_header = []

while scrolls < max_scrolls:
    # Scroll down to the bottom of the page to load more search results
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  # Wait for the page to load more results
    
    # Extract search result URLs from the current page
    h3_elems = driver.find_elements(By.XPATH, "//h3")
    
    for h3_elem in h3_elems:
        title = h3_elem.text
        if title:
            search_results_header.append(title)

    
    # Check if the page has been scrolled to the bottom
    new_scroll_height = driver.execute_script("return document.body.scrollHeight")
    if new_scroll_height == last_scroll_height:
        break
    
    # Update the last scroll height
    last_scroll_height = new_scroll_height
    
    # Increment the number of scrolls
    scrolls += 1

# Print all collected search result URLs
print("\nCollected Search Result URLs:")
df = pd.DataFrame(search_results_header)
df.to_csv(path_or_buf="../data/output.csv")
# for idx, heading in enumerate(search_results_header, start=1):
#     print(f"{idx}. {heading}")