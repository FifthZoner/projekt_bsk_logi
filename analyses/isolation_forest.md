# Wyniki dla lasu izolacyjnego

\* Podane poniżej parametry zostały zrobione pod ≥ 32GIB RAM

## Wyniki dla danych surowych
```
IsolationForest(
    n_estimators=1000,
    max_samples=0.25,
    contamination=0.12648,
    random_state=42,
    n_jobs=-1
)
```
```
Training Isolation Forest (completely unsupervised)...

Confusion Matrix:
[[2015438  203326]
 [ 203351  117932]]

Classification Report:
              precision    recall  f1-score   support

           0       0.91      0.91      0.91   2218764
           1       0.37      0.37      0.37    321283

    accuracy                           0.84   2540047
   macro avg       0.64      0.64      0.64   2540047
weighted avg       0.84      0.84      0.84   2540047
```



## Wyniki dla danych oczyszczonych
```
IsolationForest(
    n_estimators=1000,
    max_samples=0.25,
    contamination=0.12648,
    random_state=42,
    n_jobs=-1
)
```
```
Confusion Matrix:
[[1893107  201277]
 [ 213636  103766]]

Classification Report:
              precision    recall  f1-score   support

           0       0.90      0.90      0.90   2094384
           1       0.34      0.33      0.33    317402

    accuracy                           0.83   2411786
   macro avg       0.62      0.62      0.62   2411786
weighted avg       0.83      0.83      0.83   2411786
```
## Wyniki dla danych zgrupowanych niestandaryzowanych
```
IsolationForest(
    n_estimators=1000,
    max_samples=0.25,
    contamination=0.03582,
    random_state=42,
    n_jobs=-1
)
```
```
Confusion Matrix:
[[1751802   39377]
 [  39383   27167]]

Classification Report:
              precision    recall  f1-score   support

           0       0.98      0.98      0.98   1791179
           1       0.41      0.41      0.41     66550

    accuracy                           0.96   1857729
   macro avg       0.69      0.69      0.69   1857729
weighted avg       0.96      0.96      0.96   1857729
```
## Wyniki dla danych pre-procesowanych
```
IsolationForest(
    n_estimators=1000,
    max_samples=0.25,
    contamination=0.03582,
    random_state=42,
    n_jobs=-1
)
```
```
Confusion Matrix:
[[1746621   44558]
 [  44564   21986]]

Classification Report:
              precision    recall  f1-score   support

           0       0.98      0.98      0.98   1791179
           1       0.33      0.33      0.33     66550

    accuracy                           0.95   1857729
   macro avg       0.65      0.65      0.65   1857729
weighted avg       0.95      0.95      0.95   1857729
```





