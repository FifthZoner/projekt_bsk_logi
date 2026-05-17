import os
import pandas as pd

# 5
# łączy dane w jeden duży plik na potrzeby kategoryzacji
def merge(datas, save_path):
    # po kolei dla każdego pola
    if os.path.exists(save_path):
        print(f'(5) Found cached file for: {save_path}')
        return pd.read_csv(save_path,  low_memory=False)
    print(f'(5) Merging all data, will save to: {save_path}')

    data = pd.concat(datas, ignore_index=True)

    # zapisywanie, żeby widzieć wyniki z danego kroku
    data.to_csv(save_path, index=False)
    return data

# funkcje pomocnicze
