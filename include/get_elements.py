import time
from .related_quetions import GetRelatedQuestions
from .related_searches import RelatedSearches
from .web_parser import WebScraper
import json

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
        search_results = {'info': [], 'questions': []}
        soup = WebScraper.parse_website(source_page)
        if search_engine == 'google':
            try:
                for container in soup.find_all(class_='tF2Cxc'):
                    title_elem = container.find('h3')
                    link_elem = container.find('a')
                    snippet_elem = container.find('div', class_='yXK7lf')
                    
                    title = title_elem.text.strip() if title_elem else ""
                    link = link_elem['href'] if link_elem else ""
                    snippet = snippet_elem.text.strip() if snippet_elem else ""

                    print("Title:", title)
                    print("Link:", link)
                    print("Snippet:", snippet)
                    if title and link and snippet:
                        search_results['info'].append({
                            'Title': title,
                            'Link': link,
                            "Snippet": snippet
                        })

                # Extract related questions section
                search_results['questions'] =  GetRelatedQuestions.getQuestions(soup)
                search_results['related_searches'] =  RelatedSearches.getRelatedSearches(soup)
            except Exception as e:
                print(f"Error extracting text from Google search result: {e}")
        elif search_engine == 'yandex':
            try:
                h2_elems = soup.find_all('h2')
                for h2_elem in h2_elems:
                    result_text = h2_elem.text
                    if result_text:
                        search_results['info'].append(result_text)
            except Exception as e:
                print(f"Error extracting text from Yandex search result: {e}")

        return json.dumps(search_results, ensure_ascii=False, indent=4)
