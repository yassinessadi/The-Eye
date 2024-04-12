import validators

def validate_url(url):
    return validators.url(url)
