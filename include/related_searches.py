class RelatedSearches:

    @staticmethod
    def getRelatedSearches(soup):
        related_searches = []  # Initialize an empty list to store questions
        if soup:
            soup = soup.find('div', {'class': 'y6Uyqe'})
            if soup:  # Check if elements exist
                elements = soup.find_all('div', {'data-hveid': 'CEwQAA'})  # Use find_all in N760 container
                for element in elements:
                    related = element.find('div', {'class': 's75CSd'})  # Find the div containing the question
                    related = related.text.strip() if related else None  # Extract the question text
                    if related:  # Only append if question is found
                        related_searches.append(related)
        else:
            print("Error: soup variable is None")
        return related_searches