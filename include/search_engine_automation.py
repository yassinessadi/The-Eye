import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def search_google(driver, google_dorks, target_website, title):
    driver.get("https://www.google.com")
    time.sleep(3)
    search_box = driver.find_element(By.NAME, "q")
    full_query = f"{google_dorks}:{target_website} {title}"
    search_box.send_keys(full_query)
    search_box.send_keys(Keys.ENTER)
