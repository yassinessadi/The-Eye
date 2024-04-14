import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def custom_query():
    """
    Get a custom search query from the user.
    
    Returns:
    - str: The custom search query.
    """
    custom_query = input("Enter your custom query: ")
    return custom_query

def build_query(domain, keyword):
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
        # 'filetype:pdf site:{}',
        # 'inurl:/cgi-bin/ site:{}',
        # 'intext:"username" intext:"password" site:{}',
        # 'site:{} ext:sql',
        # 'site:{} ext:log',
        # 'inurl:admin site:{}',
        # 'filetype:php intext:"$dbconfig" site:{}',
        # 'intitle:"{}" | inurl:view/view.shtml site:{}',
        # 'filetype:sql site:{}',
        # 'inurl:/wp-content/uploads/ site:{}',
    ]
    formatted_dorks = [dork.format(keyword, domain) if 'intitle:' in dork else dork.format(domain) for dork in dorks]
    query = ','.join(formatted_dorks)
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


    user_choice = input("Do you want to enter a custom query? (yes/no): ").lower()
    if user_choice == "yes":
        dorks = custom_query()
    else:
        domain = input("Enter the domain: ")
        keyword = input("Enter the keyword: ")
        dorks = build_query(domain, keyword)
    
    return choice, dorks

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
