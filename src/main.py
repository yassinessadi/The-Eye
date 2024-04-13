import sys
import time
sys.path.append('../')  

from include import web_driver, data_handler, get_elements, search_engine

def get_dorks_list(dorks_input):
    return dorks_input.split(',')

if __name__ == "__main__":
    driver = web_driver.initialize_driver()
    
    # Display search engine options to the user
    print("Choose a search engine:")
    print("1. Google")
    print("2. Yandex")
    choice = input("Enter your choice (1/2): ")
    
    keyword = "Yassine Essadi"  # Fixed keyword for the example
    dorks_input = input("Enter dorks separated by commas: ")
    dorks_list = get_dorks_list(dorks_input)
    
    all_search_results = []
    
    for dork in dorks_list:
        if choice == '1':
            search_engine.search_google(driver, dork, keyword)
            
            # Check for Google CAPTCHA and wait for manual solving
            if "captcha" in driver.current_url.lower() or "captcha" in driver.page_source.lower():
                print("Google CAPTCHA detected! Please solve it manually within 20 seconds.")
                time.sleep(20)
                print("Proceeding after 20 seconds...")
            
            search_results_headers = get_elements.get_search_results(driver, 'google')
        elif choice == '2':
            search_engine.search_yandex(driver, dork, keyword)
            search_results_headers = get_elements.get_search_results(driver, 'yandex')
        else:
            print("Invalid choice. Please try again.")
            sys.exit(1)
        
        all_search_results.extend(search_results_headers)
    
    # Print all collected search result headers
    print("\nCollected Search Result Headers:")
    for idx, heading in enumerate(all_search_results, start=1):
        print(f"{idx}. {heading}")
    
    # Save the collected data to a CSV file
    data_handler.save_to_csv(all_search_results)
