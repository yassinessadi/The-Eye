import time
from bs4 import BeautifulSoup

class GetElements:
    @staticmethod
    def get_page_source(driver):
        return driver.page_source

    @staticmethod
    def scroll_page(driver, max_scrolls=10):
        last_scroll_height = driver.execute_script("return document.body.scrollHeight")
        scrolls = 0
        while scrolls < max_scrolls:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            new_scroll_height = driver.execute_script("return document.body.scrollHeight")
            if new_scroll_height == last_scroll_height:
                break
            last_scroll_height = new_scroll_height
            scrolls += 1

    @staticmethod
    def extract_elements(source_page, search_engine):
        search_results = []
        
        soup = BeautifulSoup(source_page, 'html.parser')

        if search_engine == 'google':
            for container in soup.find_all(class_='yuRUbf'):
                title = container.find('h3').text.strip()
                link = container.find('a')['href']
                if title and link:
                    search_results.append({
                        'Title': title,
                        'Link': link
                    })
        elif search_engine == 'yandex':
            try:
                h2_elems = soup.find_all('h2')
                for h2_elem in h2_elems:
                    result_text = h2_elem.text
                    if result_text:
                        search_results.append(result_text)
            except Exception as e:
                print(f"Error extracting text from Yandex search result: {e}")
        
        return search_results
