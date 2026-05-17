# główny plik
import os
import shutil

import pandas as pd
import kagglehub

from steps import step_3_group_by_sessions as step_3, step_1_add_column_names as step_1, \
    step_4_scale_standardise as step_4, step_6_category_encoding as step_6, step_5_merge as step_5, \
    step_2_fix_data_errors as step_2

raw_dir = 'raw_data'
processed_dir = 'processed_data'
results_dir = 'results'

if not os.path.exists(raw_dir):
    os.mkdir(raw_dir)
if not os.path.exists(processed_dir):
    os.mkdir(processed_dir)
if not os.path.exists(results_dir):
    os.mkdir(results_dir)

# pliki do przerabiania
files = [
    'UNSW-NB15_1.csv',
    'UNSW-NB15_2.csv',
    'UNSW-NB15_3.csv',
    'UNSW-NB15_4.csv'
         ]

for file in files:
    if not os.path.exists(f'{raw_dir}/{file}'):
        print("Missing raw files found, re-downloading...")
        os.removedirs(raw_dir)

        path = kagglehub.dataset_download("mrwellsdavid/unsw-nb15")
        shutil.copytree(path + "/", raw_dir + "/")

        for file in os.listdir(raw_dir):
            print(f'Re-encoding {raw_dir}/{file}...')
            with open(f'{raw_dir}/{file}', 'r', encoding='1252') as f:
                content = f.read()
            with open(f'{raw_dir}/{file}', 'w', encoding='utf-8') as f:
                f.write(content)

        print("Creating labeled and merged raw file...")
        raw_files = [pd.read_csv(f'{raw_dir}/{x}', low_memory=False, header=None) for x in files]
        step_1.add_column_names(step_5.merge(raw_files, f'{raw_dir}/intermediate_raw.csv'), f'{raw_dir}/raw.csv')

        print("Raw data ready!")
        break

results = []

for file in files:
    data = pd.read_csv(f'{raw_dir}/{file}', low_memory=False, header=None)
    print (f'\nProcessing {file}...')

    data = step_1.add_column_names(data, f'{processed_dir}/step_1_{file}')
    len_1 = len(data)

    data = step_2.fix_data_errors(data, f'{processed_dir}/step_2_{file}')
    len_2 = len(data)
    print(f'Dataset size change (1 -> 2): {len_1} -> {len_2}')

    data = step_3.group_by_sessions(data, f'{processed_dir}/step_3_{file}')
    len_3 = len(data)
    print(f'Dataset size change (2 -> 3): {len_2} -> {len_3}')

    # kroki stricte pod przygotowanie do uczenia maszynowego
    data = step_4.scale_standardise(data, f'{processed_dir}/step_4_{file}')
    len_4 = len(data)

    results.append(data)

print('')

data = step_5.merge(results, f'{processed_dir}/step_5_{'_'.join(files)}')

step_6.category_encoding(data, results_dir)

print('\nDone!')