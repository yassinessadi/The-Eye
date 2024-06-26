from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .web_parser import WebScraper
import pandas as pd
from .data_handler import DataHandler


class CurrencyExchangeRate:
    @staticmethod
    def get_currency(driver, search_query):
        driver.get('https://www.google.com/')
        search_box = driver.find_element(By.NAME, 'q')
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'b1hJbf')))
            html = driver.page_source
            soup = WebScraper.parse_website(html)

            exchange_rate_div = soup.find('div', {'class': 'b1hJbf'})

            exchange_rate = exchange_rate_div['data-exchange-rate']
            from_currency = exchange_rate_div.find("span",{"class":"vLqKYe"}).get_text(strip=True)
            to_currency = exchange_rate_div.find("span",{"class":"MWvIVe"}).get_text(strip=True)
            currency_data = [{
                "from" :from_currency,
                "to" : to_currency,
                "exchange rate" : exchange_rate
            }]
            df = pd.DataFrame.from_dict(currency_data)
            DataHandler.save_to_json(df,filename="../data/currency.json")
        except Exception as e:
            print(f"Error: {e}")

