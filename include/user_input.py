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
            query, active_converter = UserInput.google_input()
        elif choice == "2":
            query = UserInput.yandex_input()
        
        return choice, query, active_converter

    @staticmethod
    def google_input():
        user_choice_currency = input("Do you want the current data exchange rate? (yes/no): ").lower()
        
        if user_choice_currency == "yes":
            Currency_Field_1 = input("Enter the Currency Amount Field 1: ")
            Currency_Field_2 = input("Enter the Currency Amount Field 2: ")
            return Helper.build_currency_query(Currency_Field_1, Currency_Field_2), True
        
        user_choice_query = input("Do you want to enter a custom query? (yes/no): ").lower()
        
        if user_choice_query == "yes":
            print("\nDo you want to use a custom query? ->Please make sure you are using ',' between the query to allow multi-search in Google result. example: intext:'orange' site:fruit.com ,inurl:'orange' site:exmple.com\n")
            return Helper.custom_query(), False
        
        domain = input("Enter the domain: ")
        keyword = input("Enter the keyword: ")
        return Helper.build_dorks_query(domain, keyword), False

    @staticmethod
    def yandex_input():
        user_choice_query = input("Do you want to enter a custom query? (yes/no): ").lower()
        
        if user_choice_query == "yes":
            return Helper.custom_query()
        
        domain = input("Enter the domain: ")
        keyword = input("Enter the keyword: ")
        return Helper.build_dorks_query(domain, keyword), False
