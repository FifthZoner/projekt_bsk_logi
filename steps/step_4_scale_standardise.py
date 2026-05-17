import os
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

# 4
# standaryzuje dane i dokonuje ewentualnego skalowania logarytmicznego
def scale_standardise(data, save_path):
    # po kolei dla każdego pola
    if os.path.exists(save_path):
        print(f'(4) Found cached file for: {save_path}')
        return pd.read_csv(save_path,  low_memory=False)
    print(f'(4) Scaling and normalising, will save to: {save_path}')

    to_scale = ['sbytes', 'dbytes', 'Sload', 'Dload', 'dur', 'Sjit', 'Djit',
        'tcprtt', 'synack', 'ackdat', 'Sintpkt', 'Dintpkt', 'res_bdy_len']
    for col in to_scale:
        if col in data.columns:
            data[col] = np.log1p(data[col])

    to_standardise = [
        'smeansz', 'dmeansz', 'spkts', 'dpkts', 'swin', 'dwin',
        'stcpb', 'dtcpb', 'trans_depth', 'ct_srv_src', 'ct_srv_dst'
        'ct_state_ttl', 'ct_flw_http_mthd', 'ct_ftp_cmd',
        'ct_dst_ltm', 'ct_src_ltm', 'ct_src_dport_ltm',
        'ct_dst_sport_ltm', 'ct_dst_src_ltm'
    ]

    exclude = ['srcip', 'dstip', 'sport', 'dsport', 'proto', 'state', 'service', 'attack_cat', 'Label', 'Stime', 'Ltime']
    all_numeric = [c for c in data.columns if c not in exclude and data[c].dtype != 'object']

    scaler = StandardScaler()
    data[all_numeric] = scaler.fit_transform(data[all_numeric])

    # zapisywanie, żeby widzieć wyniki z danego kroku
    data.to_csv(save_path, index=False)
    return data

# funkcje pomocnicze
