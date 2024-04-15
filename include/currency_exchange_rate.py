from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


def get_currency(driver,search_query):
    # Navigate to Google Search
    driver.get('https://www.google.com/')
    # Search for exchange rate
    search_box = driver.find_element(By.NAME, 'q')  # Locate search box
    search_box.send_keys(search_query)  # Input the query
    search_box.send_keys(Keys.RETURN)  # Execute the search

    # Wait for the search results to load
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'b1hJbf')))
        
        # Extract HTML content
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # Find and extract exchange rate
        try:
            # Find the div containing the exchange rate
            exchange_rate_div = soup.find('div', {'class': 'b1hJbf'})

            # Extract exchange rate value from data-exchange-rate attribute
            exchange_rate = exchange_rate_div['data-exchange-rate']

            print(f"Exchange rate: {exchange_rate}")
        except AttributeError:
            print("Exchange rate not found.")
            
    except Exception as e:
        print(f"Error: {e}")
        
    # Close the browser
    driver.quit()
