import pandas as pd
import json
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, roc_auc_score

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROCESSED_PATH = os.path.join(BASE_DIR, "data", "processed_transactions.parquet")
METRICS_PATH = os.path.join(BASE_DIR, "data", "model_metrics.json")
MODEL_PATH = os.path.join(BASE_DIR, "data", "model_coefficients.json")


def train_model():
    """Train a logistic regression model to detect fraudulent transactions and save metrics and coefficients."""

    # Load processed data
    df = pd.read_parquet(PROCESSED_PATH)
    print(f"Loaded {len(df)} rows for model training.")

    # Split features and target variable
    X = df.drop(columns=["Class"])
    y = df["Class"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Train logistic regression model
    model = LogisticRegression(max_iter=500, class_weight='balanced')
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    # Calculate metrics
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_prob)

    metrics = {
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "roc_auc": round(roc_auc, 4)
    }

    # Save metrics
    with open(METRICS_PATH, "w") as f:
        json.dump(metrics, f, indent=4)

    # Save model coefficients
    coeffs = dict(zip(X.columns, model.coef_[0]))
    with open(MODEL_PATH, "w") as f:
        json.dump(coeffs, f, indent=4)

    print("Model trained successfully. Metrics saved:")
    print(metrics)


if __name__ == "__main__":
    train_model()
