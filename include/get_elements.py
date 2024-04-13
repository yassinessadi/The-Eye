import time
from selenium.webdriver.common.by import By

def get_search_results(driver, search_engine):
    search_results_headers = []
    
    scrolls = 0
    max_scrolls = 10  # Maximum number of scrolls to perform
    last_scroll_height = driver.execute_script("return document.body.scrollHeight")
    
    while scrolls < max_scrolls:
        # Scroll down to the bottom of the page to load more search results
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Wait for the page to load more results
        
        # Extract search result headers from the current page
        if search_engine == 'google':
            h3_elems = driver.find_elements(By.XPATH, "//h3")
            for h3_elem in h3_elems:
                title = h3_elem.text
                if title:
                    search_results_headers.append(title)
                    
        elif search_engine == 'yandex':
            try:
                element = driver.find_element(By.XPATH, '//h2')
                result_text = element.text
                search_results_headers.append(result_text)
            except Exception as e:
                print(f"Error extracting text from Yandex search result: {e}")
        
        # Check if the page has been scrolled to the bottom
        new_scroll_height = driver.execute_script("return document.body.scrollHeight")
        if new_scroll_height == last_scroll_height:
            break
        
        # Update the last scroll height
        last_scroll_height = new_scroll_height
        
        # Increment the number of scrolls
        scrolls += 1

    return search_results_headers
