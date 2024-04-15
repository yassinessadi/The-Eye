import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class SearchEngine:
    def __init__(self, driver):
        self.driver = driver

    def search_engine(self, url: str, search_box_selector: str, query: str):
        self.driver.get(url)
        time.sleep(3)
        search_box = self.driver.find_element(By.CSS_SELECTOR, search_box_selector)
        search_box.send_keys(query)
        search_box.send_keys(Keys.ENTER)

    def search_google(self, query: str):
        self.search_engine("https://www.google.com", "[name='q']", query)

    def search_yandex(self, query: str):
        self.search_engine("https://www.yandex.com", "#text", query)
