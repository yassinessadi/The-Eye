import sys
sys.path.append('../')  # Replace with the actual path to your project folder

from include import web_driver, search_engine_automation, data_handler,get_elements

if __name__ == "__main__":
    driver = web_driver.initialize_driver()
    
    # the keywords will be a list of word then search on them individly
    keyword = input("Enter the keyword: ")
    
    google_dorks = input("Enter google dorks: ")
    target_website = input("Enter the target website: ")
    
    search_engine_automation.search_google(driver, google_dorks, target_website, keyword)
    
    # Additional code to collect and handle search results
    search_results_headers = get_elements.get_search_results(driver)
    
    # Print all collected search result headers
    print("\nCollected Search Result Headers:")
    for idx, heading in enumerate(search_results_headers, start=1):
        print(f"{idx}. {heading}")
    
    # Save the collected data to a CSV file
    data_handler.save_to_csv(search_results_headers)
