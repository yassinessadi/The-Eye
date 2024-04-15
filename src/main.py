import sys
sys.path.append('../')  

from include import web_driver, data_handler, get_elements, search_engine, helper, currency_exchange_rate


if __name__ == "__main__":
    driver = web_driver.initialize_driver()

    choice, queries, active_converter = helper.userInput()
    if active_converter:
        currency_exchange_rate.get_currency(driver,queries)
        sys.exit(1)

    queries_list = helper.get_query_list(queries)
    all_search_results = []
    
    for query in queries_list:
        if choice == '1':
            search_engine.search_google(driver, query)
            # Check for Google CAPTCHA and wait for manual solving
            helper.handle_captcha(driver)
            search_results_headers = get_elements.get_search_results(driver, 'google')
        elif choice == '2':
            search_engine.search_yandex(driver, query)
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
