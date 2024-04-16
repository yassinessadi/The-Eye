import sys
from .helper import Helper

class UserInput:
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
