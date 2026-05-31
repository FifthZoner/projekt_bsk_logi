# Wyniki dla regresji logistycznej z regularyzacją L₁ (regresja Lasso)

\* Podane poniżej parametry zostały zrobione pod ≥ 32GIB RAM

## Wyniki dla danych surowych
```
LogisticRegression(
    l1_ratio=1.0,  
    solver='saga',
    C=0.1,
    class_weight=None,
    random_state=42
)
```
```
Confusion Matrix:
[[658435   7195]
 [  2827  93558]]

Classification Report:
              precision    recall  f1-score   support

           0       1.00      0.99      0.99    665630
           1       0.93      0.97      0.95     96385

    accuracy                           0.99    762015
   macro avg       0.96      0.98      0.97    762015
weighted avg       0.99      0.99      0.99    762015

ROC-AUC Score: 0.9989

Coefficients / Feature Elimination:
ct_state_ttl: 1.8838
sport: 1.1301
sttl: 1.0423
dttl: 0.8127
state_REQ: -0.7932
dmeansz: 0.6613
service_smtp: 0.5779
service_dns: 0.4720
proto_unas: 0.4467
service_http: 0.4354
state_FIN: 0.4284
service_ftp-data: 0.4190
state_CON: -0.3784
proto_tcp: -0.3393
swin: -0.3371
synack: -0.3105
sloss: 0.2479
dwin: -0.1997
is_sm_ips_ports: -0.1924
service_pop3: 0.1897
is_ftp_login: 0.1859
ct_srv_src: -0.1805
ct_srv_dst: -0.1766
proto_udp: 0.1748
Dload: 0.1677
tcprtt: -0.1676
trans_depth: 0.1669
proto_sctp: 0.1603
proto_ospf: 0.1543
ct_dst_sport_ltm: 0.1508
ct_dst_src_ltm: -0.1406
sbytes: 0.1350
proto_arp: -0.1128
smeansz: -0.1086
service_ftp: 0.0960
ct_src_ ltm: 0.0933
service_ssh: 0.0919
res_bdy_len: -0.0763
dbytes: -0.0719
proto_any: 0.0675
proto_sun-nd: 0.0624
proto_mobile: 0.0615
proto_swipe: 0.0608
proto_gre: 0.0601
proto_ipv6: 0.0558
proto_rsvp: 0.0554
service_dhcp: 0.0538
proto_pim: 0.0533
proto_sep: 0.0533
Sload: -0.0525
service_ssl: 0.0502
stcpb: -0.0487
proto_igmp: -0.0466
ct_ftp_cmd: 0.0441
dtcpb: -0.0439
proto_leaf-1: 0.0431
proto_iplt: 0.0422
proto_sdrp: 0.0421
proto_qnx: 0.0417
proto_mux: 0.0413
proto_idrp: 0.0412
proto_bbn-rcc: 0.0412
proto_cphb: 0.0410
proto_ipcv: 0.0410
proto_snp: 0.0410
proto_ipx-n-ip: 0.0408
proto_fc: 0.0408
proto_gmtp: 0.0407
proto_wb-mon: 0.0406
proto_rdp: 0.0406
proto_ipip: 0.0406
proto_merit-inp: 0.0405
proto_crudp: 0.0405
proto_sps: 0.0404
proto_trunk-1: 0.0404
proto_iso-ip: 0.0403
proto_prm: 0.0403
proto_ipv6-route: 0.0403
proto_dcn: 0.0401
proto_l2tp: 0.0400
proto_idpr: 0.0400
proto_pnni: 0.0400
proto_ifmp: 0.0399
proto_il: 0.0399
proto_visa: 0.0399
proto_aes-sp3-d: 0.0398
proto_ipv6-frag: 0.0398
proto_i-nlsp: 0.0398
proto_sprite-rpc: 0.0397
proto_vmtp: 0.0397
proto_ipcomp: 0.0397
proto_bna: 0.0397
proto_trunk-2: 0.0396
proto_mtp: 0.0396
proto_ddp: 0.0396
proto_iso-tp4: 0.0396
proto_etherip: 0.0395
proto_xnet: 0.0395
proto_stp: 0.0394
proto_tp++: 0.0394
proto_vrrp: 0.0394
proto_wb-expak: 0.0393
proto_netblt: 0.0393
proto_aris: 0.0393
proto_pri-enc: 0.0393
proto_narp: 0.0392
proto_ddx: 0.0392
proto_egp: 0.0392
proto_dgp: 0.0392
proto_micp: 0.0392
proto_cbt: 0.0392
proto_encap: 0.0391
proto_scps: 0.0391
proto_ip: 0.0391
proto_ttp: 0.0390
proto_iatp: 0.0390
proto_ippc: 0.0390
proto_sat-expak: 0.0389
proto_crtp: 0.0389
proto_a/n: 0.0389
proto_ipv6-no: 0.0388
proto_ptp: 0.0388
Djit: 0.0388
proto_pvp: 0.0387
proto_ipnip: 0.0387
proto_xtp: 0.0387
proto_hmp: 0.0387
proto_tlsp: 0.0386
proto_srp: 0.0386
proto_kryptolan: 0.0386
proto_br-sat-mon: 0.0386
proto_idpr-cmtp: 0.0385
proto_rvd: 0.0383
proto_emcon: 0.0383
proto_zero: 0.0383
proto_mhrp: 0.0383
proto_chaos: 0.0382
proto_ib: 0.0381
proto_skip: 0.0381
proto_ipv6-opts: 0.0381
proto_sat-mon: 0.0380
proto_uti: 0.0380
proto_st2: 0.0380
proto_pipe: 0.0380
proto_vines: 0.0380
proto_sm: 0.0379
proto_compaq-peer: 0.0378
proto_eigrp: 0.0377
proto_pup: 0.0375
proto_pgm: 0.0375
proto_argus: 0.0374
proto_tcf: 0.0373
proto_ax.25: 0.0373
proto_smp: 0.0373
proto_secure-vmtp: 0.0373
proto_isis: 0.0372
proto_leaf-2: 0.0372
proto_ggp: 0.0371
proto_nvp: 0.0371
proto_irtp: 0.0371
proto_xns-idp: 0.0370
proto_nsfnet-igp: 0.0370
proto_igp: 0.0369
proto_cpnx: 0.0368
proto_cftp: 0.0368
proto_fire: 0.0367
proto_larp: 0.0365
proto_mfe-nsp: 0.0364
proto_sccopmce: 0.0360
proto_wsn: 0.0356
state_RST: 0.0310
ct_flw_http_mthd: -0.0247
Sjit: -0.0237
service_snmp: 0.0225
Dpkts: 0.0208
state_INT: -0.0205
ct_src_dport_ltm: 0.0195
Spkts: -0.0176
ct_dst_ltm: 0.0171
service_irc: 0.0159
state_CLO: -0.0145
service_radius: 0.0125
Sintpkt: 0.0112
ackdat: 0.0100
dur: 0.0099
dloss: 0.0096
proto_esp: -0.0090
state_ECR: -0.0086
dsport: -0.0086
state_URH: 0.0066
Dintpkt: -0.0050
state_ECO: -0.0044
proto_icmp: -0.0030
state_MAS: -0.0024
state_no: -0.0017
state_URN: -0.0017
state_TST: -0.0015
proto_rtp: -0.0009
state_PAR: -0.0004
proto_udt: 0.0002
state_TXD: ELIMINATED (0.0000)
```



## Wyniki dla danych oczyszczonych
```
LogisticRegression(
    l1_ratio=1.0,  
    solver='saga',
    C=0.1,
    class_weight=None,
    random_state=42
)
```
```
Confusion Matrix:
[[621368   6947]
 [  2869  92352]]

Classification Report:
              precision    recall  f1-score   support

           0       1.00      0.99      0.99    628315
           1       0.93      0.97      0.95     95221

    accuracy                           0.99    723536
   macro avg       0.96      0.98      0.97    723536
weighted avg       0.99      0.99      0.99    723536

ROC-AUC Score: 0.9990

Coefficients / Feature Elimination:
ct_state_ttl: 1.8810
sport: 1.1493
sttl: 1.1382
state_REQ: -0.7955
dttl: 0.7909
dmeansz: 0.7076
service_smtp: 0.6176
service_dns: 0.5027
service_http: 0.4705
proto_unas: 0.4478
state_FIN: 0.4354
state_CON: -0.3546
proto_tcp: -0.3391
swin: -0.3363
synack: -0.3174
sloss: 0.2673
is_ftp_login: 0.2503
proto_arp: -0.2249
Dload: 0.2110
dwin: -0.1927
service_pop3: 0.1912
proto_udp: 0.1860
trans_depth: 0.1826
proto_ospf: 0.1747
ct_srv_dst: -0.1696
tcprtt: -0.1683
ct_srv_src: -0.1654
ct_dst_sport_ltm: 0.1615
proto_sctp: 0.1589
ct_dst_src_ltm: -0.1573
sbytes: 0.1411
service_ssh: 0.0997
smeansz: -0.0951
ct_src_ltm: 0.0903
dbytes: -0.0810
service_ftp: 0.0803
Sintpkt: -0.0707
res_bdy_len: -0.0698
proto_any: 0.0688
proto_swipe: 0.0635
proto_mobile: 0.0617
proto_sun-nd: 0.0616
proto_gre: 0.0605
service_dhcp: 0.0575
proto_sep: 0.0573
proto_rsvp: 0.0563
proto_ipv6: 0.0563
ct_ftp_cmd: 0.0542
proto_pim: 0.0541
is_sm_ips_ports: -0.0523
stcpb: -0.0520
Sload: -0.0520
proto_igmp: -0.0500
state_INT: -0.0462
proto_wb-expak: 0.0433
proto_fire: 0.0430
proto_isis: 0.0415
proto_irtp: 0.0413
proto_sat-expak: 0.0412
proto_tlsp: 0.0412
proto_iplt: 0.0412
proto_zero: 0.0412
proto_crtp: 0.0411
proto_dcn: 0.0411
proto_cftp: 0.0411
proto_pnni: 0.0410
proto_ipv6-frag: 0.0410
proto_visa: 0.0409
proto_bna: 0.0409
proto_iso-tp4: 0.0408
proto_idpr: 0.0407
proto_ipx-n-ip: 0.0406
proto_ipcv: 0.0406
proto_pup: 0.0405
proto_cphb: 0.0404
proto_vmtp: 0.0404
proto_ipv6-route: 0.0402
proto_trunk-1: 0.0402
proto_rvd: 0.0401
proto_netblt: 0.0400
proto_ipnip: 0.0399
proto_larp: 0.0399
proto_eigrp: 0.0399
proto_hmp: 0.0399
proto_idpr-cmtp: 0.0398
proto_mfe-nsp: 0.0398
proto_stp: 0.0398
proto_crudp: 0.0398
proto_pgm: 0.0398
proto_ddp: 0.0398
proto_egp: 0.0397
proto_prm: 0.0397
proto_ttp: 0.0397
proto_vines: 0.0397
proto_xtp: 0.0397
proto_leaf-1: 0.0396
proto_ippc: 0.0396
proto_skip: 0.0396
proto_ggp: 0.0396
proto_merit-inp: 0.0395
proto_smp: 0.0395
proto_sccopmce: 0.0395
proto_sps: 0.0394
proto_idrp: 0.0394
proto_chaos: 0.0392
proto_etherip: 0.0392
proto_wsn: 0.0392
proto_nvp: 0.0391
proto_leaf-2: 0.0391
proto_mtp: 0.0391
proto_qnx: 0.0391
proto_encap: 0.0391
proto_snp: 0.0390
proto_il: 0.0390
proto_mhrp: 0.0390
proto_compaq-peer: 0.0390
proto_sm: 0.0389
proto_tcf: 0.0389
proto_iso-ip: 0.0388
proto_uti: 0.0388
proto_xnet: 0.0387
proto_emcon: 0.0387
proto_secure-vmtp: 0.0387
dtcpb: -0.0386
proto_kryptolan: 0.0385
proto_narp: 0.0385
proto_sprite-rpc: 0.0384
proto_gmtp: 0.0384
proto_br-sat-mon: 0.0384
proto_sdrp: 0.0384
proto_vrrp: 0.0384
proto_ipip: 0.0384
proto_ddx: 0.0383
proto_ip: 0.0383
proto_pri-enc: 0.0383
proto_tp++: 0.0382
proto_ifmp: 0.0382
proto_pvp: 0.0382
proto_trunk-2: 0.0382
proto_fc: 0.0381
proto_micp: 0.0381
proto_scps: 0.0381
proto_nsfnet-igp: 0.0380
proto_pipe: 0.0379
proto_rdp: 0.0379
proto_xns-idp: 0.0379
proto_aes-sp3-d: 0.0378
proto_mux: 0.0378
proto_bbn-rcc: 0.0378
proto_cbt: 0.0378
proto_ipcomp: 0.0378
proto_iatp: 0.0375
proto_igp: 0.0374
proto_srp: 0.0374
proto_a/n: 0.0371
proto_ipv6-no: 0.0371
proto_sat-mon: 0.0370
Djit: 0.0369
proto_ax.25: 0.0369
proto_wb-mon: 0.0367
proto_i-nlsp: 0.0366
proto_ptp: 0.0365
proto_aris: 0.0364
proto_dgp: 0.0364
proto_ipv6-opts: 0.0362
proto_st2: 0.0362
state_RST: 0.0361
proto_l2tp: 0.0361
proto_cpnx: 0.0356
proto_ib: 0.0353
proto_argus: 0.0350
Spkts: -0.0340
Dintpkt: 0.0332
service_irc: 0.0256
ct_flw_http_mthd: -0.0254
service_snmp: 0.0239
Sjit: -0.0234
Dpkts: 0.0214
ackdat: 0.0203
ct_src_dport_ltm: 0.0176
ct_dst_ltm: 0.0160
state_CLO: -0.0160
dur: 0.0137
dloss: 0.0090
state_ECR: -0.0090
state_ECO: -0.0074
state_URH: 0.0068
proto_icmp: -0.0045
state_TST: -0.0016
state_URN: -0.0016
state_MAS: -0.0015
dsport: -0.0015
proto_rtp: -0.0001
proto_udt: ELIMINATED (0.0000)
state_PAR: ELIMINATED (0.0000)
state_TXD: ELIMINATED (0.0000)
```
## Wyniki dla danych zgrupowanych bez standaryzacji
```
LogisticRegression(
    l1_ratio=1.0,
    solver='saga',
    C=0.1,
    class_weight='balanced',
    random_state=42
)
```
```
Confusion Matrix:
[[527677   9677]
 [    64  19901]]

Classification Report:
              precision    recall  f1-score   support

           0       1.00      0.98      0.99    537354
           1       0.67      1.00      0.80     19965

    accuracy                           0.98    557319
   macro avg       0.84      0.99      0.90    557319
weighted avg       0.99      0.98      0.98    557319

ROC-AUC Score: 0.9950

Coefficients / Feature Elimination:
dttl: 1.5971
sport: 0.6691
state_INT: 0.5322
dmeansz: 0.4771
sttl: 0.4032
proto_udp: 0.3894
proto_tcp: -0.3624
swin: -0.3607
service_smtp: 0.3492
state_CON: -0.3468
proto_arp: -0.3398
service_http: 0.2921
dwin: -0.2907
service_dns: -0.2778
ct_state_ttl: 0.2531
synack: -0.2314
ct_dst_sport_ltm: -0.2224
state_FIN: 0.2152
ct_srv_dst: -0.2112
service_pop3: 0.1907
sloss: 0.1513
is_ftp_login: 0.1304
tcprtt: -0.1254
ct_srv_src: -0.1178
ct_src_dport_ltm: 0.0993
proto_iso-tp4: 0.0878
proto_pgm: 0.0818
state_RST: 0.0799
trans_depth: 0.0790
sbytes: 0.0770
proto_crudp: 0.0709
Spkts: -0.0705
ct_dst_src_ltm: -0.0652
Dintpkt: 0.0648
stcpb: -0.0578
state_REQ: -0.0574
dtcpb: -0.0550
Dload: 0.0535
proto_sat-mon: 0.0527
proto_sctp: 0.0520
ct_ftp_cmd: 0.0491
proto_rvd: 0.0480
dur: 0.0446
service_snmp: 0.0442
proto_gre: 0.0418
ct_src_ltm: 0.0416
dsport: 0.0403
proto_igmp: -0.0402
service_ftp: 0.0393
is_sm_ips_ports: -0.0380
service_dhcp: 0.0379
Sintpkt: 0.0369
Djit: 0.0360
proto_ipv6: 0.0349
proto_hmp: 0.0301
dbytes: -0.0295
proto_xtp: 0.0276
Sjit: -0.0234
ct_flw_http_mthd: -0.0230
proto_vmtp: 0.0219
smeansz: 0.0217
proto_netblt: 0.0211
service_ssh: 0.0209
state_CLO: -0.0208
Sload: 0.0194
proto_vines: 0.0186
proto_mobile: 0.0183
proto_swipe: 0.0182
Dpkts: 0.0179
proto_wb-expak: 0.0177
state_ECR: -0.0172
proto_scps: 0.0169
proto_visa: 0.0167
proto_ipv6-opts: 0.0164
proto_sun-nd: 0.0154
proto_sm: 0.0153
proto_pnni: 0.0145
res_bdy_len: -0.0144
proto_leaf-1: 0.0143
proto_ospf: -0.0141
proto_pim: 0.0141
proto_ipip: 0.0141
proto_nvp: 0.0141
proto_unas: 0.0140
proto_sep: 0.0140
proto_bbn-rcc: 0.0136
proto_igp: 0.0135
proto_emcon: 0.0134
proto_gmtp: 0.0131
proto_iplt: 0.0129
proto_argus: 0.0125
proto_egp: 0.0125
proto_prm: 0.0123
proto_rtp: -0.0122
proto_stp: 0.0122
proto_chaos: 0.0122
proto_xnet: 0.0119
proto_bna: 0.0119
proto_tcf: 0.0118
proto_i-nlsp: 0.0117
proto_ipcomp: 0.0116
proto_pipe: 0.0116
proto_zero: 0.0115
proto_mfe-nsp: 0.0114
proto_l2tp: 0.0114
proto_snp: 0.0113
proto_ddx: 0.0113
proto_sps: 0.0113
proto_skip: 0.0113
proto_compaq-peer: 0.0112
proto_ipv6-route: 0.0112
proto_idpr: 0.0111
proto_aris: 0.0111
proto_eigrp: 0.0111
proto_dgp: 0.0110
proto_mhrp: 0.0110
proto_ttp: 0.0110
proto_ipcv: 0.0109
proto_a/n: 0.0108
proto_sat-expak: 0.0108
proto_vrrp: 0.0108
proto_fire: 0.0107
proto_encap: 0.0107
proto_secure-vmtp: 0.0107
service_irc: 0.0106
proto_tlsp: 0.0106
proto_merit-inp: 0.0106
proto_mux: 0.0106
proto_wb-mon: 0.0106
proto_sprite-rpc: 0.0105
proto_iso-ip: 0.0105
proto_ptp: 0.0104
proto_ipx-n-ip: 0.0102
proto_pri-enc: 0.0102
proto_idrp: 0.0101
proto_leaf-2: 0.0099
proto_crtp: 0.0099
proto_etherip: 0.0098
proto_tp++: 0.0097
proto_any: 0.0097
proto_sccopmce: 0.0097
proto_fc: 0.0097
proto_irtp: 0.0096
proto_kryptolan: 0.0096
proto_wsn: 0.0095
proto_narp: 0.0095
proto_ib: 0.0095
proto_xns-idp: 0.0094
proto_uti: 0.0094
proto_cftp: 0.0094
proto_larp: 0.0094
proto_sdrp: 0.0093
proto_micp: 0.0092
proto_mtp: 0.0092
proto_ipv6-frag: 0.0091
proto_cpnx: 0.0089
proto_cphb: 0.0088
proto_ax.25: 0.0088
proto_qnx: 0.0087
proto_pup: 0.0085
proto_ggp: 0.0085
proto_trunk-2: 0.0085
proto_pvp: 0.0084
proto_trunk-1: 0.0083
proto_il: 0.0083
proto_isis: 0.0083
proto_ipv6-no: 0.0083
proto_nsfnet-igp: 0.0081
proto_dcn: 0.0081
proto_aes-sp3-d: 0.0080
proto_st2: 0.0075
proto_idpr-cmtp: 0.0074
proto_br-sat-mon: 0.0070
proto_ipnip: 0.0070
proto_rsvp: 0.0069
proto_smp: 0.0069
proto_ippc: 0.0068
proto_rdp: 0.0066
proto_ifmp: 0.0066
proto_iatp: 0.0065
proto_ip: 0.0063
proto_cbt: 0.0062
proto_icmp: -0.0061
dloss: 0.0058
ct_dst_ltm: 0.0053
proto_ddp: 0.0052
proto_srp: 0.0050
state_ECO: -0.0045
ackdat: 0.0035
state_URH: 0.0024
state_MAS: -0.0013
state_URN: -0.0004
state_TST: -0.0002
proto_udt: ELIMINATED (0.0000)
state_PAR: ELIMINATED (0.0000)
state_TXD: ELIMINATED (0.0000)
```
## Wyniki dla danych pre-procesowanych
```
LogisticRegression(
    l1_ratio=1.0,
    solver='saga',
    C=0.1,
    class_weight='balanced',
    random_state=42
)
```
```
Confusion Matrix:
[[528008   9346]
 [    80  19885]]

Classification Report:
              precision    recall  f1-score   support

           0       1.00      0.98      0.99    537354
           1       0.68      1.00      0.81     19965

    accuracy                           0.98    557319
   macro avg       0.84      0.99      0.90    557319
weighted avg       0.99      0.98      0.98    557319

ROC-AUC Score: 0.9938

Coefficients / Feature Elimination:
dttl: 1.9488
state_INT: 0.7556
sport: 0.7264
service_http: 0.4043
state_CON: -0.3808
synack: -0.3736
proto_arp: -0.3667
sttl: 0.3486
service_dns: -0.3429
proto_udp: 0.3406
service_smtp: 0.3300
Dintpkt: 0.3251
swin: -0.3131
proto_tcp: -0.3076
dur: 0.2642
res_bdy_len: -0.2602
sbytes: -0.2565
dmeansz: 0.2562
dwin: -0.2212
ct_srv_dst: -0.2047
service_pop3: 0.1855
Dload: 0.1801
state_FIN: 0.1792
ct_dst_sport_ltm: -0.1736
Sjit: -0.1629
ct_state_ttl: 0.1614
sloss: 0.1391
trans_depth: 0.1366
dbytes: 0.1332
dsport: 0.1170
smeansz: 0.1141
tcprtt: -0.1107
ct_srv_src: -0.1107
ct_ftp_cmd: 0.1003
proto_iso-tp4: 0.1000
state_RST: 0.0925
Spkts: -0.0917
proto_pgm: 0.0909
ackdat: -0.0878
state_REQ: 0.0853
proto_crudp: 0.0794
ct_src_dport_ltm: 0.0789
proto_ospf: -0.0659
proto_sat-mon: 0.0581
proto_sctp: 0.0525
service_ssh: -0.0478
state_CLO: -0.0468
ct_src_ltm: 0.0459
ct_dst_src_ltm: -0.0457
proto_rvd: 0.0430
proto_igmp: -0.0427
service_snmp: 0.0411
service_dhcp: 0.0399
proto_gre: 0.0387
ct_flw_http_mthd: -0.0351
proto_ipv6: 0.0350
Djit: 0.0314
proto_xtp: 0.0305
Dpkts: -0.0270
ct_dst_ltm: -0.0269
proto_hmp: 0.0269
stcpb: -0.0252
proto_vmtp: 0.0240
proto_netblt: 0.0232
state_ECR: -0.0229
proto_vines: 0.0214
Sload: -0.0210
Sintpkt: -0.0199
dtcpb: -0.0191
proto_scps: 0.0191
proto_wb-expak: 0.0191
dloss: 0.0187
is_sm_ips_ports: -0.0182
proto_unas: 0.0181
proto_mobile: 0.0178
proto_visa: 0.0174
proto_swipe: 0.0173
proto_sm: 0.0168
proto_sun-nd: 0.0148
proto_ipip: 0.0147
proto_leaf-1: 0.0147
proto_nvp: 0.0138
proto_gmtp: 0.0137
proto_rtp: -0.0135
proto_emcon: 0.0135
proto_bbn-rcc: 0.0130
proto_pim: 0.0128
proto_sep: 0.0128
proto_egp: 0.0127
proto_igp: 0.0127
proto_ipv6-opts: 0.0126
proto_stp: 0.0123
proto_argus: 0.0118
proto_bna: 0.0117
proto_mhrp: 0.0115
proto_vrrp: 0.0112
proto_ttp: 0.0108
proto_merit-inp: 0.0108
proto_xnet: 0.0108
proto_zero: 0.0107
proto_i-nlsp: 0.0107
proto_skip: 0.0107
proto_l2tp: 0.0106
proto_prm: 0.0106
proto_sat-expak: 0.0106
proto_sps: 0.0105
proto_idpr: 0.0105
proto_fire: 0.0105
proto_aris: 0.0104
proto_dgp: 0.0103
proto_eigrp: 0.0103
proto_iso-ip: 0.0102
service_ftp: 0.0101
proto_xns-idp: 0.0101
proto_sprite-rpc: 0.0101
proto_secure-vmtp: 0.0101
proto_wb-mon: 0.0100
proto_ipcomp: 0.0100
proto_pipe: 0.0099
proto_compaq-peer: 0.0099
proto_encap: 0.0099
proto_a/n: 0.0099
proto_mfe-nsp: 0.0099
proto_idrp: 0.0099
proto_tlsp: 0.0099
proto_ptp: 0.0098
proto_isis: 0.0098
proto_sccopmce: 0.0097
proto_pri-enc: 0.0097
proto_chaos: 0.0097
proto_mux: 0.0096
proto_iplt: 0.0095
service_irc: 0.0095
proto_ipx-n-ip: 0.0095
proto_snp: 0.0094
proto_ddx: 0.0094
proto_pnni: 0.0093
proto_etherip: 0.0093
proto_leaf-2: 0.0093
proto_tp++: 0.0091
is_ftp_login: -0.0091
proto_crtp: 0.0091
proto_wsn: 0.0091
proto_ipv6-route: 0.0090
proto_irtp: 0.0090
proto_micp: 0.0090
proto_ipv6-frag: 0.0090
proto_ib: 0.0090
proto_ggp: 0.0090
proto_larp: 0.0089
proto_any: 0.0089
proto_narp: 0.0089
proto_fc: 0.0088
proto_cphb: 0.0088
proto_ipcv: 0.0088
proto_cftp: 0.0088
proto_tcf: 0.0087
proto_mtp: 0.0087
proto_pup: 0.0086
proto_uti: 0.0086
proto_ax.25: 0.0085
proto_trunk-2: 0.0084
proto_kryptolan: 0.0084
proto_sdrp: 0.0081
proto_cpnx: 0.0080
proto_trunk-1: 0.0078
proto_nsfnet-igp: 0.0078
proto_aes-sp3-d: 0.0077
proto_pvp: 0.0076
proto_dcn: 0.0073
proto_ipv6-no: 0.0071
proto_il: 0.0071
proto_rsvp: 0.0068
proto_ipnip: 0.0068
proto_qnx: 0.0067
proto_st2: 0.0067
proto_ifmp: 0.0066
proto_idpr-cmtp: 0.0066
proto_iatp: 0.0063
proto_smp: 0.0063
proto_ippc: 0.0059
proto_ip: 0.0059
proto_rdp: 0.0058
proto_br-sat-mon: 0.0057
proto_cbt: 0.0054
proto_srp: 0.0050
state_URH: 0.0049
proto_ddp: 0.0047
proto_icmp: -0.0030
state_ECO: -0.0023
state_MAS: -0.0006
state_TST: 0.0000
proto_udt: ELIMINATED (0.0000)
state_PAR: ELIMINATED (0.0000)
state_URN: ELIMINATED (0.0000)
state_TXD: ELIMINATED (0.0000)
```





