import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def search_engine(driver, url: str, search_box_selector: str,query: str):
    """
    Search using a specific search engine.
    
    Args:
    - driver: The Selenium WebDriver instance.
    - url (str): The URL of the search engine.
    - search_box_selector (str): The selector for the search box.
    - query (str): conatins Additional search terms & The main search term.
    """
    driver.get(url)
    time.sleep(3)
    search_box = driver.find_element(By.CSS_SELECTOR, search_box_selector)
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)

def search_google(driver, query: str):
    """
    Search on Google.
    
    Args:
    - driver: The Selenium WebDriver instance.
    - query (str): conatins Additional search terms & The main search term.
    """
    search_engine(driver, "https://www.google.com", "[name='q']", query)

def search_yandex(driver, query: str):
    """
    Search on Yandex.
    
    Args:
    - driver: The Selenium WebDriver instance.
    - query (str): conatins Additional search terms & The main search term.
    """
    search_engine(driver, "https://www.yandex.com", "#text", query)
