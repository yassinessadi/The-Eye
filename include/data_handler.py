import pandas as pd

class DataHandler:
    @staticmethod
    def save_to_csv(data, filename="../data/output.csv"):
        df = pd.DataFrame(data)
        df.to_csv(path_or_buf=filename)
