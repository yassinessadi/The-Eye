class GetRelatedQuestions:

    @staticmethod
    def getQuestions(soup):
        questions = []  # Initialize an empty list to store questions
        if soup:
            soup = soup.find('div', {'jsname': 'N760b'})
            if soup:  # Check if elements exist
                elements = soup.find_all('div', {'jsname': 'yEVEwb'})  # Use find_all in N760 container
                for element in elements:
                    question_div = element.find('div', {'jsname': 'tJHJj'})  # Find the div containing the question
                    question = question_div.text.strip() if question_div else None  # Extract the question text
                    if question:  # Only append if question is found
                        questions.append(question)
        else:
            print("Error: soup variable is None")
        return questions