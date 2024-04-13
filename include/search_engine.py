import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def build_query(dorks: str, keyword: str) -> str:
    """
    Build the search query based on the dorks and keyword.
    
    Args:
    - dorks (str): Additional search terms.
    - keyword (str): The main search term.
    
    Returns:
    - str: The constructed search query.
    """
    if dorks.strip() == "":
        return keyword
    else:
        return f"{dorks} {keyword}"

def search_engine(driver, url: str, search_box_selector: str, dorks: str, keyword: str):
    """
    Search using a specific search engine.
    
    Args:
    - driver: The Selenium WebDriver instance.
    - url (str): The URL of the search engine.
    - search_box_selector (str): The selector for the search box.
    - dorks (str): Additional search terms.
    - keyword (str): The main search term.
    """
    driver.get(url)
    time.sleep(3)
    search_box = driver.find_element(By.CSS_SELECTOR, search_box_selector)
    query = build_query(dorks, keyword)
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)

def search_google(driver, dorks: str, keyword: str):
    """
    Search on Google.
    
    Args:
    - driver: The Selenium WebDriver instance.
    - dorks (str): Additional search terms.
    - keyword (str): The main search term.
    """
    search_engine(driver, "https://www.google.com", "[name='q']", dorks, keyword)

def search_yandex(driver, dorks: str, keyword: str):
    """
    Search on Yandex.
    
    Args:
    - driver: The Selenium WebDriver instance.
    - dorks (str): Additional search terms.
    - keyword (str): The main search term.
    """
    search_engine(driver, "https://www.yandex.com", "#text", dorks, keyword)
