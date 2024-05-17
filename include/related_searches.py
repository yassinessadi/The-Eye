class RelatedSearches:

    @staticmethod
    def getRelatedSearches(soup):
        related_searches = []  
        if soup:
            soup = soup.find('div', {'class': 'ULSxyf'})
            if soup:  # Check if elements exist
                elements = soup.find_all('div', {'class': 'y6Uyqe'})  
                for element in elements:
                    links = element.find_all('a', {'class': 'ngTNl'})
                    for link in links:
                        href = link.get('href')
                        related_searches.append({str(link.getText()).strip() : href})
        else:
            print("Error: soup variable is None")
        return related_searches
        