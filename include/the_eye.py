from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

service = Service("C://chromedriver//chromedriver.exe")

driver = webdriver.Chrome(service=service)
driver.get("https://www.amazon.com/")
driver.close()