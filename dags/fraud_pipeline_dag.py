from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# create DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'retries': 1
}

with DAG(
    dag_id='fraud_detection_pipeline',
    default_args=default_args,
    description='ETL + ML pipeline for fraud detection',
    schedule=None,
    catchup=False
) as dag:

    # 1. upload data
    ingest = BashOperator(
        task_id='ingest_data',
        bash_command=f'python3 {os.path.join(BASE_DIR, "src", "ingest_data.py")}'
    )

    # 2. transform data
    process = BashOperator(
        task_id='process_data',
        bash_command=f'python3 {os.path.join(BASE_DIR, "src", "process_data_spark.py")}'
    )

    # 3. model training
    train = BashOperator(
        task_id='train_model',
        bash_command=f'python3 {os.path.join(BASE_DIR, "src", "train_model.py")}'
    )

    # 4. quality monitoring
    monitor = BashOperator(
        task_id='monitor_quality',
        bash_command=f'python3 {os.path.join(BASE_DIR, "src", "monitor_data_quality.py")}'
    )

    # workflow
    ingest >> process >> train >> monitor
