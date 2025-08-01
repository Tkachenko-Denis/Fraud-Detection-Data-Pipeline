import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "transactions_sample.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "raw_transactions.parquet")


def ingest_data():
    """Load raw transaction data from CSV, validate required columns, and save as Parquet."""

    # Load CSV
    df = pd.read_csv(RAW_DATA_PATH)
    print(f"Loaded {len(df)} rows from {RAW_DATA_PATH}.")

    # Basic column check
    required_cols = ["Time", "Amount", "Class"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Save as Parquet
    df.to_parquet(OUTPUT_PATH, index=False)
    print(f"Data successfully saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    ingest_data()