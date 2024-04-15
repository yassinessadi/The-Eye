import requests
from bs4 import BeautifulSoup

class WebScraper:
    def parse_website(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return BeautifulSoup(response.content, 'html.parser')
