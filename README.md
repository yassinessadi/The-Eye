# The eye

## Overview

This project provides a tool to perform web searches on Google and Yandex search engines. Additionally, it offers a feature to fetch the current currency exchange rate from Google. The project utilizes Selenium for web scraping and interaction and BeautifulSoup for parsing HTML content.

## Features

- Web search on Google and Yandex
- Fetching current currency exchange rate using Google
- Saving search results to a CSV file

## Project Structure

```bash
TheEye/
│
├── src/
│   └── main.py
│
└── include/
    ├── __init__.py
    ├── web_driver.py
    ├── url_validator.py
    ├── web_parser.py
    ├── search_engine_automation.py
    ├── get_elements.py
    ├── search_engine.py
    ├── related_searches.py
    ├── related_quetions.py
    ├── helper.py
    ├── user_input.py
    └── data_handler.py
```

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/yassinessadi/The-Eye.git
    ```
2. Install required packages using the requirements.txt:
    ```
    pip install -r requirements.txt
    ```
3. Download [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) and place it in `C://chromedriver//chromedriver.exe`.

## Usage

### Running the Main Application

1. Navigate to the project directory:
    ```bash
    cd The-Eye
    ```
2. Run the main application:
    ```bash
    cd src/
    python main.py
    ```

### Input

- Choose between Google and Yandex for web search.
- Enter the search queries separated by commas.
- Enter a currency code example (field 1: USD & field 2: MAD) to fetch the currency exchange rate from Google.

### Output

- first make sure you createa dir called `./data/`
- The search results will be displayed on the console.
- The search results will be saved to a CSV file named `output.csv` in the `data/` directory.

## Example: Custom Dorks Query

A Dorks query can be constructed using advanced Google search operators. Here's an example of a custom Dorks query to search for specific file types:


```bash
-> single query:
intext:"yassine essadi" site:github.com

-> multi query:
intext:"yassine essadi" site:"github.com" , intitle:"yassine essadi" site:"linkedin.com",inurl:"yassineesadi" site:"facebook.com"
```

To integrate this with the project:

1. Choose Google as the search engine.
2. Enter the Dorks query as the search query.

## Note

- Ensure proper handling of CAPTCHA if prompted during Google search.
- The currency exchange rate feature fetches data from Google, which might be subject to change.

## Contributors
- YASSINE ESSADI