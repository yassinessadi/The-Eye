import time
from selenium.webdriver.common.by import By

class GetElements:
    @staticmethod
    def get_search_results(driver, search_engine):
        search_results_headers = []
        scrolls = 0
        max_scrolls = 10
        last_scroll_height = driver.execute_script("return document.body.scrollHeight")

        while scrolls < max_scrolls:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

            if search_engine == 'google':
                try:
                    h3_elems = driver.find_elements(By.XPATH, "//h3")
                    for h3_elem in h3_elems:
                        title = h3_elem.text
                        if title:
                            search_results_headers.append(title)
                except Exception as e:
                    print(f"Error extracting data from Google search result: {e}")
            elif search_engine == 'yandex':
                try:
                    h2_elems = driver.find_elements(By.XPATH, '//h2')
                    for h2_elem in h2_elems:
                        result_text = h2_elem.text
                        if result_text:
                            search_results_headers.append(result_text)
                except Exception as e:
                    print(f"Error extracting text from Yandex search result: {e}")

            new_scroll_height = driver.execute_script("return document.body.scrollHeight")
            if new_scroll_height == last_scroll_height:
                break

            last_scroll_height = new_scroll_height
            scrolls += 1

        return search_results_headers
