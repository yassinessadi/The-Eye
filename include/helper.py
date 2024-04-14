import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        'filetype:pdf site:{}',
        'inurl:/cgi-bin/ site:{}',
        'intext:"username" intext:"password" site:{}',
        'site:{} ext:sql',
        'site:{} ext:log',
        'inurl:admin site:{}',
        'filetype:php intext:"$dbconfig" site:{}',
        'intitle:"{}" | inurl:view/view.shtml site:{}',
        'filetype:sql site:{}',
        'inurl:/wp-content/uploads/ site:{}',
    ]

    formatted_dorks = [dork.format(keyword, domain) if 'intitle:' in dork else dork.format(domain) for dork in dorks]
    dorks_string = ','.join(formatted_dorks)
    return dorks_string

def userInput():
    # Display search engine options to the user
    print("Choose a search engine:")
    print("1. Google")
    print("2. Yandex")
    choice = input("Enter your choice (1/2): ")

    print("--------------------------------------")
    domain = input("Enter the domain: ")
    keyword = input("Enter the keyword: ")
    dorks = build_query(domain, keyword)
    return choice, dorks

def get_query_list(dorks_input):
    return dorks_input.split(',')


def handle_captcha(driver):
    if "captcha" in driver.current_url.lower() or "captcha" in driver.page_source.lower():
        print("Google CAPTCHA detected! Please solve it manually within 20 seconds.")
        time.sleep(20)
        print("Proceeding after 20 seconds...")
