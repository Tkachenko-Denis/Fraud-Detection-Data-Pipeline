import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, log1p

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_PATH = os.path.join(BASE_DIR, "data", "raw_transactions.parquet")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "processed_transactions.parquet")


def process_data():
    """Process raw transaction data using PySpark: clean data, generate features, and save the results."""

    spark = SparkSession.builder \
        .appName("FraudDataProcessing") \
        .getOrCreate()

    # Load raw data
    df = spark.read.parquet(RAW_PATH)
    print(f"Loaded {df.count()} rows from raw data.")

    # Basic cleaning
    # Remove transactions with zero or negative amounts
    df = df.filter(col("Amount") > 0)

    # Feature engineering: logarithmic transformation of Amount
    df = df.withColumn("Amount_log", log1p(col("Amount")))

    # Quality checks
    total_rows = df.count()
    fraud_rows = df.filter(col("Class") == 1).count()
    if fraud_rows == 0:
        raise ValueError("No fraudulent transactions left after cleaning!")

    print(f"After cleaning: {total_rows} rows, including {fraud_rows} fraudulent transactions.")

    # Save processed data
    df.write.mode("overwrite").parquet(OUTPUT_PATH)
    print(f"Processed data saved to {OUTPUT_PATH}")

    spark.stop()


if __name__ == "__main__":
    process_data()

