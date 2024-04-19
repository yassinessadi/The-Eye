import pandas as pd

class DataHandler:
    @staticmethod
    def save_to_json(all_search_results, filename="../data/output.json"):
        df_list = []
        
        for result in all_search_results:
            for info in result['info']:
                df_info = pd.DataFrame([info])  # Removed index=[0]
                df_info['SearchEngine'] = result['SearchEngine']
                df_list.append(df_info.to_dict(orient='records'))
                
            for question in result['questions']:
                df_questions = pd.DataFrame({'Question': [question]})
                df_questions['SearchEngine'] = result['SearchEngine']
                df_list.append(df_questions.to_dict(orient='records'))
                
        df_combined = pd.DataFrame(df_list)
        df_combined.to_json(path_or_buf=filename, orient='records', lines=True, force_ascii=False)
