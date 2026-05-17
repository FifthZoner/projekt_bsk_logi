import os
import numpy as np
import pandas as pd

# 3
# Grupuje rekordy za pomocą wspólnych adresów, portów i protokołów
# redukuje ilość danych i daje realny obraz połączeń w trakcie zbierania danych
def group_by_sessions(data, save_path):
    # po kolei dla każdego pola
    if (os.path.exists(save_path)):
        print(f'(3) Found cached file for: {save_path}')
        return pd.read_csv(save_path,  low_memory=False)
    print(f'(3) Grouping by sessions, will save to: {save_path}')

    data['Stime_dt'] = pd.to_datetime(data['Stime'], unit='s')

    agg_logic = {
        # dane o czasie
        'dur': 'sum',
        'Stime': 'min',
        'Ltime': 'max',

        # sumy
        'sbytes': 'sum',
        'dbytes': 'sum',
        'Spkts': 'sum',
        'Dpkts': 'sum',
        'sloss': 'sum',
        'dloss': 'sum',

        # średnie obciążenia i wydajności
        'Sload': 'mean',
        'Dload': 'mean',
        'smeansz': 'mean',
        'dmeansz': 'mean',
        'Sjit': 'mean',
        'Djit': 'mean',
        'Sintpkt': 'mean',
        'Dintpkt': 'mean',

        # parametry sieciowe
        'sttl': 'max',
        'dttl': 'max',
        'swin': 'max',
        'dwin': 'max',
        'stcpb': 'mean',
        'dtcpb': 'mean',
        'tcprtt': 'mean',
        'synack': 'mean',
        'ackdat': 'mean',

        # dane dodatkowe, możliwe, że będzie trzeba je przeliczyć samodzielnie
        'trans_depth': 'sum',
        'res_bdy_len': 'sum',
        'ct_flw_http_mthd': 'sum',
        'is_ftp_login': 'max',
        'ct_ftp_cmd': 'sum',

        # liczniki połączeń
        'ct_state_ttl': 'mean',
        'ct_srv_src': 'mean',
        'ct_srv_dst': 'mean',
        'ct_dst_ltm': 'mean',
        'ct_src_ltm': 'mean',
        'ct_src_dport_ltm': 'mean',
        'ct_dst_sport_ltm': 'mean',
        'ct_dst_src_ltm': 'mean',

        # kategorie
        'state': lambda x: x.mode()[0] if not x.mode().empty else x.iloc[0],
        'service': lambda x: x.mode()[0] if not x.mode().empty else x.iloc[0],
        'attack_cat': get_most_frequent,
        'Label': 'max',

        # inne
        'is_sm_ips_ports': 'max'
    }

    data = data.groupby([
        pd.Grouper(key='Stime_dt', freq='2min'),
        'srcip',
        'sport',
        'dstip',
        'dsport',
        'proto'
    ]).agg(agg_logic).reset_index().drop(columns=['Stime_dt'])

    # zapisywanie, żeby widzieć wyniki z danego kroku
    data.to_csv(save_path, index=False)
    return data

# funkcje pomocnicze
def get_most_frequent(x):
    attacks_only = x[x != 'Normal']

    if not attacks_only.empty:
        return attacks_only.mode().iloc[0]

    return 'Normal'