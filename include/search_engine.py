import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def search_google(driver, google_dorks, target_website, keyword):
    driver.get("https://www.google.com")
    time.sleep(3)
    search_box = driver.find_element(By.NAME, "q")
    full_query = f"{google_dorks}:{target_website} {keyword}"
    search_box.send_keys(full_query)
    search_box.send_keys(Keys.ENTER)

def search_yandex(driver, yandex_dorks, target_website, keyword):
    driver.get("https://www.yandex.com")
    time.sleep(3)
    search_box = driver.find_element(By.ID, "text")
    full_query = f"{yandex_dorks}:{target_website} {keyword}"
    search_box.send_keys(full_query)
    search_box.send_keys(Keys.ENTER)
