# Wyniki dla Klasyfikator histogramowego wzmacniania gradientu
### Dla danych surowych
```
HistGradientBoostingClassifier(
    categorical_features='from_dtype',
    class_weight=None,          
    max_iter=200,               
    learning_rate=0.1,          
    max_leaf_nodes=31,          
    random_state=42
)
```
```
Confusion Matrix:
[[663787   1843]
 [  3457  92928]]

Classification Report:
              precision    recall  f1-score   support

           0       0.99      1.00      1.00    665630
           1       0.98      0.96      0.97     96385

    accuracy                           0.99    762015
   macro avg       0.99      0.98      0.98    762015
weighted avg       0.99      0.99      0.99    762015

ROC-AUC Score: 0.9997

Importances:
sttl: 0.1362
ct_state_ttl: 0.0092
dsport: 0.0043
service: 0.0020
dbytes: 0.0017
sport: 0.0010
ct_srv_dst: 0.0009
smeansz: 0.0007
sbytes: 0.0005
synack: 0.0005
proto: 0.0005
ct_srv_src: 0.0005
state: 0.0004
Dload: 0.0004
dmeansz: 0.0004
dloss: 0.0003
ct_flw_http_mthd: 0.0003
ct_dst_src_ltm: 0.0002
dur: 0.0002
Sload: 0.0002
ct_dst_sport_ltm: 0.0002
Dpkts: 0.0002
ct_src_ ltm: 0.0001
Dintpkt: 0.0001
ct_src_dport_ltm: 0.0001
Djit: 0.0001
ct_dst_ltm: 0.0001
dtcpb: 0.0001
Spkts: 0.0001
Sintpkt: 0.0001
sloss: 0.0001
res_bdy_len: 0.0000
Sjit: 0.0000
stcpb: 0.0000
is_ftp_login: 0.0000
ct_ftp_cmd: 0.0000
```
### Dla danych po pre-processingu
```
HistGradientBoostingClassifier(
    categorical_features='from_dtype',
    class_weight='balanced',  
    max_iter=400, 
    learning_rate=0.05, 
    max_leaf_nodes=63, 
    min_samples_leaf=50,
    random_state=42
)
```
```
Confusion Matrix:
[[532751   4603]
 [  5526  14439]]

Classification Report:
              precision    recall  f1-score   support

           0       0.99      0.99      0.99    537354
           1       0.76      0.72      0.74     19965

    accuracy                           0.98    557319
   macro avg       0.87      0.86      0.87    557319
weighted avg       0.98      0.98      0.98    557319

ROC-AUC Score: 0.9955

Importances:
sttl: 0.0531
dsport: 0.0021
ct_state_ttl: 0.0016
ct_srv_dst: 0.0016
state: 0.0006
ct_srv_src: 0.0005
smeansz: 0.0005
service: 0.0004
sport: 0.0003
sbytes: 0.0002
dmeansz: 0.0002
Djit: 0.0001
dbytes: 0.0001
ct_dst_src_ltm: 0.0001
dur: 0.0001
Dintpkt: 0.0001
res_bdy_len: 0.0001
ct_dst_ltm: 0.0000
Sintpkt: 0.0000
synack: 0.0000
proto: 0.0000
ct_src_ltm: 0.0000
ct_dst_sport_ltm: 0.0000
Dpkts: 0.0000
swin: 0.0000
Spkts: 0.0000
ct_flw_http_mthd: 0.0000
ct_src_dport_ltm: 0.0000
stcpb: 0.0000
dttl: 0.0000
dwin: 0.0000
is_ftp_login: 0.0000
```