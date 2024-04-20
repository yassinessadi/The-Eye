from bs4 import BeautifulSoup

class WebScraper:
    @staticmethod
    def parse_website(page_source):
        return BeautifulSoup(page_source, 'html.parser')
