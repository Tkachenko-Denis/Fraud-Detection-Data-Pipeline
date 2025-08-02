import pandas as pd
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROCESSED_PATH = os.path.join(BASE_DIR, "data", "processed_transactions.parquet")
METRICS_PATH = os.path.join(BASE_DIR, "data", "model_metrics.json")
PREVIOUS_METRICS_PATH = os.path.join(BASE_DIR, "data", "previous_model_metrics.json")

def monitor_data():
    print("Starting data and model monitoring...")

    # --- Data checks ---
    df = pd.read_parquet(PROCESSED_PATH)
    issues = []

    # Missing values
    missing = df.isnull().sum().sum()
    if missing > 0:
        issues.append(f"Found {missing} missing values in the dataset.")

    # Fraudulent transaction ratio
    fraud_ratio = df['Class'].mean()
    if fraud_ratio < 0.001:
        issues.append("Very few fraudulent transactions detected (<0.1%).")

    # Amount range check
    if (df['Amount'] <= 0).any():
        issues.append("Transactions with zero or negative amounts were found.")

    print(f"Fraudulent transaction ratio: {fraud_ratio:.4f}")

    # --- Model metrics checks ---
    if os.path.exists(METRICS_PATH):
        with open(METRICS_PATH, "r") as f:
            current_metrics = json.load(f)
    else:
        print("Model metrics file not found.")
        return

    if os.path.exists(PREVIOUS_METRICS_PATH):
        with open(PREVIOUS_METRICS_PATH, "r") as f:
            previous_metrics = json.load(f)

        # ROC-AUC comparison
        if current_metrics["roc_auc"] < previous_metrics["roc_auc"] - 0.02:
            issues.append("ROC-AUC decreased by more than 0.02 compared to the previous model.")
    else:
        print("No previous metrics found. Saving current metrics as a baseline.")

    # Save current metrics as baseline for future comparisons
    with open(PREVIOUS_METRICS_PATH, "w") as f:
        json.dump(current_metrics, f, indent=4)

    # --- Result ---
    
    if issues:
        print("\n Problems found by monitoring:")
        for i in issues:
            print("-", i)
    else:
        print(" Monitoring completed, no problems found.")

if __name__ == "__main__":
    monitor_data()
