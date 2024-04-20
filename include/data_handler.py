import pandas as pd

class DataHandler:
    @staticmethod
    def save_to_json(all_search_results, filename="../data/output.json"):
        df_results = pd.DataFrame(all_search_results)
        df_results.to_json(path_or_buf=filename, orient='records', force_ascii=False)
