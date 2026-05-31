import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
from category_encoders import TargetEncoder
from sklearn.inspection import permutation_importance

def run_for_file(file_path, clf):

    print(f'Loading {file_path}...')
    df = pd.read_csv(file_path, low_memory=False)


    target_column = 'Label'
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

    print(f"Detected categorical features: {categorical_features}")
    print(f"Total missing values in dataset: {X.isna().sum().sum()}")

    # Dzielenie danych -------------------------------------------------------------------------------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    encoder = TargetEncoder(cols=['sport', 'dsport'])
    X_train = encoder.fit_transform(X_train, y_train)
    X_test = encoder.transform(X_test)

    # Trening ----------------------------------------------------------------------------------------------------------

    print("\nTraining HistGradientBoosting model...")
    clf.fit(X_train, y_train)

    # Wyniki -----------------------------------------------------------------------------------------------------------

    y_pred = clf.predict(X_test)
    y_pred_proba = clf.predict_proba(X_test)[:, 1]

    print(f"\n=== Model Evaluation for {file_path} ===")
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    print(f"ROC-AUC Score: {roc_auc_score(y_test, y_pred_proba):.4f}")

    print("Importances:")
    result = permutation_importance(clf, X_test, y_test, n_repeats=5, random_state=42)
    for i in result.importances_mean.argsort()[::-1]:
        if result.importances_mean[i] > 0:
            print(f"{X.columns[i]}: {result.importances_mean[i]:.4f}")
    print("\n=== End of data ===\n\n\n")


run_for_file('raw_data/raw.csv',
             HistGradientBoostingClassifier(
                 categorical_features='from_dtype',
                 class_weight=None,
                 max_iter=200,
                 learning_rate=0.1,
                 max_leaf_nodes=31,
                 random_state=42
             ))

run_for_file('processed_data/step_2_UNSW-NB15_1.csv_UNSW-NB15_2.csv_UNSW-NB15_3.csv_UNSW-NB15_4.csv',
             HistGradientBoostingClassifier(
                 categorical_features='from_dtype',
                 class_weight=None,
                 max_iter=200,
                 learning_rate=0.1,
                 max_leaf_nodes=31,
                 random_state=42
             ))
run_for_file('processed_data/step_3_UNSW-NB15_1.csv_UNSW-NB15_2.csv_UNSW-NB15_3.csv_UNSW-NB15_4.csv',
             HistGradientBoostingClassifier(
                 categorical_features='from_dtype',
                 class_weight='balanced',
                 max_iter=400,
                 learning_rate=0.05,
                 max_leaf_nodes=63,
                 min_samples_leaf=50,
                 random_state=42
             ))
run_for_file('processed_data/step_5_UNSW-NB15_1.csv_UNSW-NB15_2.csv_UNSW-NB15_3.csv_UNSW-NB15_4.csv',
             HistGradientBoostingClassifier(
                 categorical_features='from_dtype',
                 class_weight='balanced',
                 max_iter=400,
                 learning_rate=0.05,
                 max_leaf_nodes=63,
                 min_samples_leaf=50,
                 random_state=42
             ))
