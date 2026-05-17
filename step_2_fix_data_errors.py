import ipaddress
import os
import numpy as np
import pandas as pd

# 2
# Dopisuje brakujące wartości w danych,
# zapewnia pewność, że wartości są poprawne dla danych pól
def fix_data_errors(data, save_path):
    # po kolei dla każdego pola
    if (os.path.exists(save_path)):
        print(f'(2) Found cached file for: {save_path}')
        return pd.read_csv(save_path,  low_memory=False)
    print(f'(2) Fixing data errors, will save to: {save_path}')

    # ip pochodzenia
    data = data.dropna(subset=['srcip'])[data['srcip'].apply(is_valid_ip)]
    # port pochodzenia
    data = data.dropna(subset=['sport'])[data['sport'].apply(is_valid_port)]
    # ip docelowe
    data = data.dropna(subset=['dstip'])[data['dstip'].apply(is_valid_ip)]
    # port docelowy
    data = data.dropna(subset=['dsport'])[data['dsport'].apply(is_valid_port)]
    # protokół, tutaj puste uzupełniamy na podstawie numeru portu, będzie trzeba dodać więcej
    port_map = {
        80: 'http', 443: 'http', 8080: 'http', 8443: 'http',
        53: 'dns', 67: 'dhcp', 68: 'dhcp', 123: 'ntp',
        389: 'ldap', 636: 'ldap',
        20: 'ftp', 21: 'ftp', 22: 'ssh', 445: 'smb', 137: 'netbios', 138: 'netbios', 139: 'netbios',
        25: 'smtp', 465: 'smtp', 587: 'smtp',
        110: 'pop3', 995: 'pop3',
        143: 'imap', 993: 'imap',
        23: 'telnet', 3389: 'rdp', 5900: 'vnc', 161: 'snmp', 162: 'snmp',
        1433: 'sql', 1434: 'sql', 3306: 'sql', 5432: 'sql', 1521: 'sql',
        194: 'irc', 6667: 'irc'
    }
    data['proto'] = (data['proto'].replace('-', np.nan)
                                  .fillna(data['dsport'].map(port_map))
                                  .fillna(data['sport'].map(port_map)))
    # stan połączenia
    data = data.dropna(subset=['state'])[data['state'].apply(is_valid_state)]
    # czas połączenia, nieujemny
    data = data.dropna(subset=['dur'])[data['dur'] >= 0.]
    # wysłane bajty, nieujemny
    data = data.dropna(subset=['sbytes'])[data['sbytes'] >= 0]
    # otrzymane bajty, nieujemny
    data = data.dropna(subset=['dbytes'])[data['dbytes'] >= 0]
    # czas życia przy wysyłce, nieujemny
    data = data.dropna(subset=['sttl'])[data['sttl'] >= 0]
    # czas życia przy odbiorze, nieujemny
    data = data.dropna(subset=['dttl'])[data['dttl'] >= 0]
    # stracone paczki przy wysyłce
    data = data.dropna(subset=['sloss'])[data['sloss'] >= 0]
    # stracone paczki przy odbiorze
    data = data.dropna(subset=['dloss'])[data['dloss'] >= 0]
    # serwis używany w przypadku paczki
    data = data.dropna(subset=['service'])[data['service'].apply(is_valid_service)]
    # b/s wysyłki
    data = data.dropna(subset=['Sload'])[data['Sload'] >= 0.]
    # b/s odbioru
    data = data.dropna(subset=['Dload'])[data['Dload'] >= 0.]
    # ilość wysłanych paczek
    data = data.dropna(subset=['Spkts'])[data['Spkts'] >= 0]
    # ilość odebranych paczek
    data = data.dropna(subset=['Dpkts'])[data['Dpkts'] >= 0]
    # wartość okna ogłoszenia TCP źródła
    data = data.dropna(subset=['swin'])[data['swin'] >= 0][data['swin'] <= 255]
    # wartość okna ogłoszenia TCP celu
    data = data.dropna(subset=['dwin'])[data['dwin'] >= 0][data['dwin'] <= 255]
    # numer sekwencji TCP źródła
    data = data.dropna(subset=['stcpb'])[data['stcpb'] >= 0]
    # numer sekwencji TCP celu
    data = data.dropna(subset=['dtcpb'])[data['dtcpb'] >= 0]
    # średnia wielkość wysyłanej paczki
    data = data.dropna(subset=['smeansz'])[data['smeansz'] >= 0]
    # średnia wielkość odbieranej paczki
    data = data.dropna(subset=['dmeansz'])[data['dmeansz'] >= 0]
    # głębokość transakcji
    data = data.dropna(subset=['trans_depth'])[data['trans_depth'] >= 0]
    # długość ciała wiadomości
    data = data.dropna(subset=['res_bdy_len'])[data['res_bdy_len'] >= 0]
    # wariancja opóźnienia przy wysyłce
    data = data.dropna(subset=['Sjit'])[data['Sjit'] >= 0.]
    # warincja opóźnienia przy odbiorze
    data = data.dropna(subset=['Djit'])[data['Djit'] >= 0.]
    # czasy początku i końca transmisji
    data['Stime'] = pd.to_datetime(data['Stime'], unit='s')
    data['Ltime'] = pd.to_datetime(data['Ltime'], unit='s')
    data = data.dropna(subset=['Stime', 'Ltime'])
    data = data[~(data['Ltime'] < data['Stime'])]
    # przerwa między przybyciem ramki, a paczek
    data = data.dropna(subset=['Sintpkt'])[data['Sintpkt'] >= 0.]
    # przerwa między wysłaniem ramki, a paczek
    data = data.dropna(subset=['Dintpkt'])[data['Dintpkt'] >= 0.]
    # całkowity czas potrzeby na ustanowienie połączenia z potwierdzeniami
    data = data.dropna(subset=['tcprtt'])[data['tcprtt'] >= 0.]
    # czas pomiędzy SYN i SYN_ACK
    data = data.dropna(subset=['synack'])[data['synack'] >= 0.]
    # czas pomiędzy SYN_ACK i ACK
    data = data.dropna(subset=['ackdat'])[data['ackdat'] >= 0.]
    # oba adresy i porty są identyczne
    data['is_sm_ips_ports'] = ((data['srcip'] == data['dstip']) & (data['sport'] == data['dsport'])).astype(int)
    # kolejny numer dla stanu połączenia
    data = data.dropna(subset=['ct_state_ttl'])[data['ct_state_ttl'] >= 0]
    # ilość potoków zapytań GET i POST (np do detekcji DDOS)
    data['ct_flw_http_mthd'] = data['ct_flw_http_mthd'].fillna(0)
    data = data[data['ct_flw_http_mthd'] >= 0]
    # czy połączenie ftp jest używane przez użytkownika i hasło
    data['is_ftp_login'] = data['is_ftp_login'].fillna(0)
    data = data[data['is_ftp_login'].isin([0, 1])]
    # ilość połączeń ftp
    data['ct_ftp_cmd'] = pd.to_numeric(data['ct_ftp_cmd'], errors='coerce')
    data['ct_ftp_cmd'] = data['ct_ftp_cmd'].fillna(0)
    data = data[data['ct_ftp_cmd'] >= 0]
    # ilość połączeń z tym samym serwisem i adresem źródłowym w 100 połączeniach wg ostatniego czasu
    data = data.dropna(subset=['ct_srv_src'])[data['ct_srv_src'] >= 0]
    # ilość połączeń z tym samym serwisem i adresem docelowym w 100 połączeniach wg ostatniego czasu
    data = data.dropna(subset=['ct_srv_dst'])[data['ct_srv_dst'] >= 0]
    # ilość połączeń z tym samym adresem docelowym w ostatnich 100
    data = data.dropna(subset=['ct_dst_ltm'])[data['ct_dst_ltm'] >= 0]
    # ilość połączeń z tym samym adresem źródłowym w ostatnich 100
    data = data.rename(columns={'ct_src_ ltm': 'ct_src_ltm'})
    data = data.dropna(subset=['ct_src_ltm'])[data['ct_src_ltm'] >= 0]
    # ilość połączeń z tym samym adresem i portem źródłowym w ostatnich 100
    data = data.dropna(subset=['ct_src_dport_ltm'])[data['ct_src_dport_ltm'] >= 0]
    # ilość połączeń z tym samym adresem i portem docelowym w ostatnich 100
    data = data.dropna(subset=['ct_dst_sport_ltm'])[data['ct_dst_sport_ltm'] >= 0]
    # ilość połączeń z tym samym adresem docelowym i źródłowym w ostatnich 100
    data = data.dropna(subset=['ct_dst_src_ltm'])[data['ct_dst_src_ltm'] >= 0]
    # kategoria ataku, dajemy normal przy braku, bo niektóre modele moga potrzebować, tym samym kolejne jest useless
    data['attack_cat'] = data['attack_cat'].fillna('Normal')
    data['attack_cat'] = data['attack_cat'].astype(str).str.strip().str.title()
    data = data[data['attack_cat'].apply(is_valid_attack)]
    # czy atak
    data['Label'] = (data['attack_cat'] != 'Normal').astype(int)

    # usuwanie nieustawionych kolumn
    data = data.dropna()

    # zapisywanie, żeby widzieć wyniki z danego kroku
    data.to_csv(save_path, index=False)
    return data

# funkcje pomocnicze

# sprawdzenie, czy ip jest poprawnie napisane
def is_valid_ip(ip):
    try:
        ip_str = str(ip).strip()
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False

def is_valid_port(port):
    try:
        port = int(port)
        return 0 <= port <= 0xFFFF
    except ValueError:
        return False

def is_valid_state(state):
    string = str(state).strip().upper()
    allowed_values = {'ACC', 'CLO', 'CON', 'ECO', 'ECR', 'FIN', 'INT',
                      'MAS', 'PAR', 'REQ', 'RST', 'TST', 'TXD', 'URH', 'URN'}
    return string in allowed_values

def is_valid_service(service):
    string = str(service).strip().lower()
    allowed_values = {
         'http', 'dns', 'dhcp', 'ntp',
         'ldap', 'ftp','ssh', 'smb',
         'netbios', 'smtp', 'pop3', 'imap',
         'telnet', 'rdp', 'vnc', 'snmp',
         'sql', 'irc', '-'
    }
    return string in allowed_values

def is_valid_attack(attack):
    string = str(attack).strip().title()
    allowed_values = {'Fuzzers', 'Analysis', 'Backdoors', 'Dos', 'Exploits',
                      'Generic', 'Reconnaissance', 'Shellcode', 'Worms', 'Normal'}
    return string in allowed_values