from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class WebDriver:
    def __init__(self):
        self.service = Service("C://chromedriver//chromedriver.exe")
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        
    def initialize_driver(self):
        return webdriver.Chrome(service=self.service, options=self.chrome_options)
