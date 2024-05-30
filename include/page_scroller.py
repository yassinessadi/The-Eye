import time

class PageScroller:
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