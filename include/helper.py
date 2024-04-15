import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append('../')  

from include import currency_exchange_rate

def custom_query():
    """
    Get a custom search query from the user.
    
    Returns:
    - str: The custom search query.
    """
    custom_query = input("Enter your custom query: ")
    return custom_query

def build_dorks_query(domain, keyword):
    """
    Build the search query based on the dorks and keyword.
    
    Args:
    - domain (str): link to the hostname.
    - keyword (str): The main search term.
    
    Returns:
    - str: The constructed search query.
    """
    dorks = [
        'intitle:"{}" site:{}',
        'filetype:pdf site:{}',
        'intext:"username" intext:"password" site:{}',
        'inurl:admin site:{}',
        'filetype:php intext:"$dbconfig" site:{}',
        'intitle:"{}" | inurl:view/view.shtml site:{}',
        'filetype:sql site:{}',
        'inurl:/wp-content/uploads/ site:{}',
    ]
    formatted_dorks = [dork.format(keyword, domain) if 'intitle:' in dork else dork.format(domain) for dork in dorks]
    query = ','.join(formatted_dorks)
    return query

def build_currency_query(from_currency,to_currency):
    query = f"{from_currency} to {to_currency}"
    return query

def userInput():
    """
    Get user input for search engine, domain, and keyword.
    
    Returns:
    - tuple: (choice, query)
    """
    # Display search engine options to the user
    print("Choose a search engine:")
    print("1. Google")
    print("2. Yandex")
    choice = input("Enter your choice (1/2): ")
    print("--------------------------------------")    
    user_choice_currency = input("Do you want the current data exchange rate? (yes/no): ").lower()
    active_converter = False
    if user_choice_currency =="yes":
        Currency_Field_1 = input("Enter the Currency Amount Field 1: ")
        Currency_Field_2 = input("Enter the Currency Amount Field 2: ")
        query = build_currency_query(Currency_Field_1,Currency_Field_2)
        active_converter = True
        return choice, query, active_converter
    else: 
        user_choice_query = input("Do you want to enter a custom query? (yes/no): ").lower()
        active_converter = False
        if user_choice_query == "yes":
            query = custom_query()
        else:
            domain = input("Enter the domain: ")
            keyword = input("Enter the keyword: ")
            query = build_dorks_query(domain, keyword)
        return choice, query, active_converter

def get_query_list(dorks_input):
    """
    Convert the dorks string into a list.
    
    Args:
    - dorks_input (str): The dorks string.
    
    Returns:
    - list: List of dorks.
    """
    return dorks_input.split(',')

def handle_captcha(driver):
    """
    Check and handle CAPTCHA in the driver.
    
    Args:
    - driver: Selenium WebDriver instance.
    """
    if "captcha" in driver.current_url.lower() or "captcha" in driver.page_source.lower():
        print("Google CAPTCHA detected! Please solve it manually within 20 seconds.")
        time.sleep(20)
        print("Proceeding after 20 seconds...")