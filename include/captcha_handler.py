import time
from bs4 import BeautifulSoup
from .web_parser import WebScraper

class CaptchaHandler:
    @staticmethod
    def handle_captcha(source_page, search_engine):
        soup = WebScraper.parse_website(source_page)
        
        if search_engine == 'google':
            if "captcha" in source_page.lower():
                print("Google CAPTCHA detected! Please solve it manually within 20 seconds.")
                time.sleep(20)
                print("Proceeding after 20 seconds...")
        elif search_engine == 'yandex':
            try:
                if soup.find(class_="CheckboxCaptcha"):
                    print("Yandex CAPTCHA detected! Please solve it manually within 20 seconds.")
                    time.sleep(20)
                    print("Proceeding after 20 seconds...")
            except:
                pass