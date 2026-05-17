import pandas as pd
import os




# 1
# dopisuje etykiety do plików, domyślnie nie mają one nagłówków
def add_column_names(data, save_path):
    header_df = pd.read_csv('../raw_data/NUSW-NB15_features.csv')
    column_names = header_df.iloc[:, 1].tolist()
    if (os.path.exists(save_path)):
        print(f'(1) Found cached file for: {save_path}')
        return pd.read_csv(save_path,  low_memory=False)
    print(f'(1) Adding labels, will save to: {save_path}')

    data.columns = column_names

    data.to_csv(save_path, index=False)
    return data