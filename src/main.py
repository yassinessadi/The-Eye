import sys
sys.path.append('../')  # Replace with the actual path to your project folder

from include import web_driver, data_handler, get_elements, search_engine

if __name__ == "__main__":
    driver = web_driver.initialize_driver()
    
    # Display search engine options to the user
    print("Choose a search engine:")
    print("1. Google")
    print("2. Yandex")
    choice = input("Enter your choice (1/2): ")
    
    keyword = input("Enter the keyword: ")
    dorks = input("Enter dorks: ")
    
    if choice == '1':
        search_engine.search_google(driver, dorks, keyword)
        search_results_headers = get_elements.get_search_results(driver, 'google')
    elif choice == '2':
        search_engine.search_yandex(driver, dorks, keyword)
        search_results_headers = get_elements.get_search_results(driver, 'yandex')
    else:
        print("Invalid choice. Please try again.")
        sys.exit(1)
    
    # Print all collected search result headers
    print("\nCollected Search Result Headers:")
    for idx, heading in enumerate(search_results_headers, start=1):
        print(f"{idx}. {heading}")
    
    # Save the collected data to a CSV file
    data_handler.save_to_csv(search_results_headers)