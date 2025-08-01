# Fraud Detection Data Pipeline

An end-to-end ML pipeline prototype for financial fraud detection.

## Objectives

- Simulate a Data Engineer workflow:
  - Collect transaction data
  - Perform data cleaning, quality checks, and feature generation
  - Train a machine learning model to detect fraudulent transactions
  - Monitor data quality and model performance
  - Orchestrate the entire process using Airflow
- Demonstrate expertise in:
  - **Python, PySpark, scikit-learn**
  - **ETL processes and Data Quality**
  - **ML lifecycle orchestration with Airflow**
  - **Designing scalable solutions for Azure**

---

## Project Architecture

1. **Data Ingestion:** Load transaction data from CSV → Parquet  
2. **Data Processing:** Clean and transform data with PySpark, generate features  
3. **Model Training:** Train a logistic regression model for fraud detection  
4. **Monitoring:** Validate data quality and track model metrics  
5. **Orchestration:** Schedule and manage the full pipeline with Airflow  

---

## Tech Stack

- **Python 3.10+**
- **Pandas, PySpark** – data processing
- **scikit-learn** – model training
- **Great Expectations** – data quality checks
- **Apache Airflow** – pipeline orchestration
- **Jupyter Notebook** – exploratory data analysis and visualization
- **Parquet, CSV** – data storage formats

---

## Installation and Usage

### Clone the repository

```bash
git clone https://github.com/Tkachenko-Denis/fraud-detection-pipeline.git
cd fraud-detection-pipeline
```
Download the [**Credit Card Fraud Detection**](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) dataset from Kaggle and save the file as `transactions_sample.csv` in the `data` folder.


### Create a virtual environment and install dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Run the pipeline manually
```bash
python src/ingest_data.py
python src/process_data_spark.py
python src/train_model.py
python src/monitor_data_quality.py
```
### Run the pipeline with Airflow
```bash
airflow standalone
```
⚠️ Important: Update the dags_folder path in your airflow.cfg file to point to the folder containing the DAG.
Then, open http://localhost:8080 and activate the fraud_detection_pipeline DAG.

