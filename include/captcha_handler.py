import time

class CaptchaHandler:
    @staticmethod
    def handle_captcha(driver):
        if "captcha" in driver.current_url.lower() or "captcha" in driver.page_source.lower():
            print("Google CAPTCHA detected! Please solve it manually within 20 seconds.")
            time.sleep(20)
            print("Proceeding after 20 seconds...")
