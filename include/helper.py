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
    def get_query_list(dorks_input):
        return dorks_input.split(',')
