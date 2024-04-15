import validators

class Validator:
    @staticmethod
    def validate_url(url):
        return validators.url(url)
