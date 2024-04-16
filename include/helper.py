import time
import sys

class Helper:
    @staticmethod
    def custom_query():
        return input("Enter your custom query: ")

    @staticmethod
    def build_dorks_query(domain, keyword):
        dorks = [
            'intitle:"{}" site:{}',
            'filetype:pdf site:{}',
            'intext:"username" intext:"password" site:{}',
            'inurl:admin site:{}',
            'filetype:php intext:"$dbconfig" site:{}',
            'intitle:"{}" | inurl:view/view.shtml site:{}',
            'filetype:sql site:{}',
            'inurl:/wp-content/uploads/ site:{}',
        ]
        formatted_dorks = [dork.format(keyword, domain) if 'intitle:' in dork else dork.format(domain) for dork in dorks]
        return ','.join(formatted_dorks)

    @staticmethod
    def build_currency_query(from_currency, to_currency):
        return f"{from_currency} to {to_currency}"

    @staticmethod
    def user_input():
        print("Choose a search engine:")
        print("1. Google")
        print("2. Yandex")
        choice = input("Enter your choice (1/2): ")
        print("--------------------------------------")

        active_converter = False
        query = ""

        if choice == "1":
            user_choice_currency = input("Do you want the current data exchange rate? (yes/no): ").lower()
            if user_choice_currency == "yes":
                Currency_Field_1 = input("Enter the Currency Amount Field 1: ")
                Currency_Field_2 = input("Enter the Currency Amount Field 2: ")
                query = Helper.build_currency_query(Currency_Field_1, Currency_Field_2)
                active_converter = True
            else:
                user_choice_query = input("Do you want to enter a custom query? (yes/no): ").lower()
                if user_choice_query == "yes":
                    query = Helper.custom_query()
                else:
                    domain = input("Enter the domain: ")
                    keyword = input("Enter the keyword: ")
                    query = Helper.build_dorks_query(domain, keyword)
        elif choice == "2":
            user_choice_query = input("Do you want to enter a custom query? (yes/no): ").lower()
            if user_choice_query == "yes":
                query = Helper.custom_query()
            else:
                domain = input("Enter the domain: ")
                keyword = input("Enter the keyword: ")
                query = Helper.build_dorks_query(domain, keyword)
        else:
            print("Invalid choice. Please try again.")
            sys.exit(1)

        return choice, query, active_converter


    @staticmethod
    def get_query_list(dorks_input):
        return dorks_input.split(',')

    @staticmethod
    def handle_captcha(driver):
        if "captcha" in driver.current_url.lower() or "captcha" in driver.page_source.lower():
            print("Google CAPTCHA detected! Please solve it manually within 20 seconds.")
            time.sleep(20)
            print("Proceeding after 20 seconds...")
