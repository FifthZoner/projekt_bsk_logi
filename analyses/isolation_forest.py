import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report, confusion_matrix

def run_for_file(file_path, iso_forest):
    print(f'Loading {file_path}...')
    df = pd.read_csv(file_path, low_memory=False)

    columns_to_drop = [
        'Label', 'attack_cat', 'srcip', 'dstip',
        'Stime', 'Ltime', 'sport', 'dsport'
    ]
    X = df.drop(columns=columns_to_drop, errors='ignore')

    # konwersja na dane numeryczne
    X = pd.get_dummies(X, drop_first=True)
    y_true = df['Label']

    # trening ----------------------------------------------------------------------------------------------------------

    print("Training Isolation Forest model...")
    iso_forest.fit(X)

    # przewidywanie ----------------------------------------------------------------------------------------------------
    y_pred_raw = iso_forest.predict(X)

    y_pred = np.where(y_pred_raw == -1, 1, 0)

    # Wyniki -----------------------------------------------------------------------------------------------------------
    print(f"\n=== Unsupervised Isolation Forest Evaluation for {file_path} ===")
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_true, y_pred))

    print("\nClassification Report:")
    print(classification_report(y_true, y_pred))
    print("\n=== End of data ===\n\n\n")

run_for_file('raw_data/raw.csv',
             IsolationForest(
                n_estimators=1000,
                max_samples=0.25,
                contamination=0.12648,
                random_state=42,
                n_jobs=-1
             ))
run_for_file('processed_data/step_2_UNSW-NB15_1.csv_UNSW-NB15_2.csv_UNSW-NB15_3.csv_UNSW-NB15_4.csv',
             IsolationForest(
                n_estimators=1000,
                max_samples=0.25,
                contamination=0.12648,
                random_state=42,
                n_jobs=-1
             ))
run_for_file('processed_data/step_3_UNSW-NB15_1.csv_UNSW-NB15_2.csv_UNSW-NB15_3.csv_UNSW-NB15_4.csv',
             IsolationForest(
                 n_estimators=1000,
                 max_samples=0.25,
                 contamination=0.03582,
                 random_state=42,
                 n_jobs=-1
             ))
run_for_file('processed_data/step_5_UNSW-NB15_1.csv_UNSW-NB15_2.csv_UNSW-NB15_3.csv_UNSW-NB15_4.csv',
             IsolationForest(
                 n_estimators=1000,
                 max_samples=0.25,
                 contamination=0.03582,
                 random_state=42,
                 n_jobs=-1
             ))
