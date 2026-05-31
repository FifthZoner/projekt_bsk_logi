import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
from category_encoders import TargetEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer


def run_for_file(file_path, clf):
    print(f'Loading {file_path}...')
    df = pd.read_csv(file_path, low_memory=False)

    # Define your target and features
    target_column = 'Label'  # 0 for normal, 1 for anomaly/attack
    columns_to_drop = [
        target_column,
        'attack_cat',
        'srcip',
        'dstip',
        'Stime',
        'Ltime'
    ]
    X = df.drop(columns=columns_to_drop, errors='ignore')
    y = df[target_column]

    numeric_fixes = ['sport', 'dsport', 'ct_ftp_cmd']
    for col in numeric_fixes:
        if col in X.columns:
            X[col] = pd.to_numeric(X[col], errors='coerce')

    categorical_features = X.select_dtypes(include=['object', 'string', 'category']).columns.tolist()
    for col in categorical_features:
        X[col] = X[col].astype('category')

    # Kolumny ----------------------------------------------------------------------------------------------------------
    categorical_features = X.select_dtypes(include=['object', 'category']).columns.tolist()

    for col in categorical_features:
        X[col] = X[col].astype('category')

    print(f"Detected categorical features before encoding: {categorical_features}")
    print(f"Total missing values in dataset: {X.isna().sum().sum()}")

    nominal_cols = [c for c in categorical_features if c not in ['sport', 'dsport']]
    if nominal_cols:
        X = pd.get_dummies(X, columns=nominal_cols, drop_first=True)

    # Dzielenie danych -------------------------------------------------------------------------------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    encoder = TargetEncoder(cols=['sport', 'dsport'])
    X_train = encoder.fit_transform(X_train, y_train)
    X_test = encoder.transform(X_test)

    imputer = SimpleImputer(strategy='median')
    X_train_imp = imputer.fit_transform(X_train)
    X_test_imp = imputer.transform(X_test)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train_imp)
    X_test_scaled = scaler.transform(X_test_imp)

    # Trening ----------------------------------------------------------------------------------------------------------

    print("\nTraining L1-Regularized Logistic Regression model...")
    clf.fit(X_train_scaled, y_train)

    # Wyniki -----------------------------------------------------------------------------------------------------------

    y_pred = clf.predict(X_test_scaled)
    y_pred_proba = clf.predict_proba(X_test_scaled)[:, 1]

    print(f"\n=== Model Evaluation for {file_path} ===")
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    print(f"ROC-AUC Score: {roc_auc_score(y_test, y_pred_proba):.4f}")

    print("\nCoefficients / Feature Elimination:")
    # Map the coefficients back to the processed column names
    feature_names = X.columns
    coefficients = clf.coef_[0]

    # Sort features by absolute coefficient magnitude (highest impact first)
    sorted_indices = np.argsort(np.abs(coefficients))[::-1]

    for idx in sorted_indices:
        coef_val = coefficients[idx]
        if coef_val == 0:
            print(f"{feature_names[idx]}: ELIMINATED (0.0000)")
        else:
            print(f"{feature_names[idx]}: {coef_val:.4f}")

    print("\n=== End of data ===\n\n\n")


run_for_file('raw_data/raw.csv',
             LogisticRegression(
                 l1_ratio=1.0,
                 solver='saga',
                 C=0.1,
                 class_weight=None,
                 random_state=42
             ))

run_for_file('processed_data/step_2_UNSW-NB15_1.csv_UNSW-NB15_2.csv_UNSW-NB15_3.csv_UNSW-NB15_4.csv',
             LogisticRegression(
                 l1_ratio=1.0,
                 solver='saga',
                 C=0.1,
                 class_weight=None,
                 random_state=42
             ))


run_for_file('processed_data/step_3_UNSW-NB15_1.csv_UNSW-NB15_2.csv_UNSW-NB15_3.csv_UNSW-NB15_4.csv',
             LogisticRegression(
                 l1_ratio=1.0,
                 solver='saga',
                 C=0.1,
                 class_weight='balanced',
                 random_state=42
             ))

run_for_file('processed_data/step_5_UNSW-NB15_1.csv_UNSW-NB15_2.csv_UNSW-NB15_3.csv_UNSW-NB15_4.csv',
             LogisticRegression(
                 l1_ratio=1.0,
                 solver='saga',
                 C=0.1,
                 class_weight='balanced',
                 random_state=42
             ))