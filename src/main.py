import sys
import json
sys.path.append('../')

from include import web_driver, data_handler, get_elements, search_engine, helper, currency_exchange_rate, captcha_handler, user_input

class MainApp:
    def run(self):
        driver = web_driver.WebDriver().initialize_driver()

        choice, queries, active_converter = user_input.UserInput.user_input()
        if active_converter:
            currency_exchange_rate.CurrencyExchangeRate.get_currency(driver, queries)
            sys.exit(1)

        queries_list = helper.Helper.get_query_list(queries)
        all_search_results = []

        for query in queries_list:
            if choice == '1':
                search_engine.SearchEngine(driver).search_google(query)
                # Check for Google CAPTCHA and wait for manual solving
                source_page = get_elements.GetElements.get_page_source(driver)
                captcha_handler.CaptchaHandler.handle_captcha(source_page, 'google')
                get_elements.GetElements.scroll_page(driver)
                source_page = get_elements.GetElements.get_page_source(driver)
                search_results_json = get_elements.GetElements.extract_elements(source_page, 'google')
            elif choice == '2':
                search_engine.SearchEngine(driver).search_yandex(query)
                # Check for Yandex CAPTCHA and wait for manual solving
                source_page = get_elements.GetElements.get_page_source(driver)
                captcha_handler.CaptchaHandler.handle_captcha(source_page, 'yandex')
                get_elements.GetElements.scroll_page(driver)
                source_page = get_elements.GetElements.get_page_source(driver)
                search_results_json = get_elements.GetElements.extract_elements(source_page, 'yandex')
            else:
                print("Invalid choice. Please try again.")
                sys.exit(1)
            
            search_results = json.loads(search_results_json)
            search_results['SearchEngine'] = 'Google' if choice == '1' else 'Yandex'
            all_search_results.append(search_results)

        # Save the collected data to a JSON file
        data_handler.DataHandler.save_to_json(all_search_results)

if __name__ == "__main__":
    app = MainApp()
    app.run()
