import pytest
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize SparkSession for tests
@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder \
        .master("local[1]") \
        .appName("pytest_spark") \
        .getOrCreate()

def test_processing_creates_amount_log(spark):
    # Sample data
    data = [(1, 100.0, 0), (2, 50.0, 1)]
    columns = ["Time", "Amount", "Class"]
    df = spark.createDataFrame(data, columns)

    # Data processing
    df = df.filter(col("Amount") > 0)
    df = df.withColumn("Amount_log", col("Amount"))

    # Check: column is created and rows are preserved
    assert "Amount_log" in df.columns
    assert df.count() == 2

def test_no_negative_amounts(spark):
    # Sample data with a negative amount
    data = [(1, -100.0, 0), (2, 50.0, 1)]
    columns = ["Time", "Amount", "Class"]
    df = spark.createDataFrame(data, columns)

    # Filter out invalid rows
    df_clean = df.filter(col("Amount") > 0)

    # Check: negative transactions are removed
    assert df_clean.count() == 1
