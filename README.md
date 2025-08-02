# Fraud Detection Data Pipeline

An end-to-end ML pipeline prototype for financial fraud detection.

## Objectives

- Simulate a Data Engineer workflow:
  - Collect transaction data
  - Perform data cleaning, quality checks, and feature generation
  - Train machine learning model to detect fraudulent transactions
  - Monitor data quality and model performance
  - Orchestrate the entire process using Airflow
- Demonstrate expertise in:
  - **Python, PySpark, scikit-learn**
  - **ETL processes**
  - **ML lifecycle orchestration with Airflow**

---

## Architecture

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
- **Apache Airflow** – pipeline orchestration
- **Parquet, CSV** – data storage formats

---

## Repository structure

```plaintext
fraud-detection-pipeline/
│
├── README.md
├── requirements.txt
├── data/                         # sample data
│
├── dags/
│   └── fraud_pipeline_dag.py     # Airflow DAG
│
├── src/
│   ├── ingest_data.py            # upload data
│   ├── process_data_spark.py     # processing, cleaning, feature eng.
│   ├── train_model.py            # training model
│   └── monitor_data_quality.py   # data quality metrics
│
└── tests/
    └── test_data_processing.py   # unit-tests
    └── test_model_training.py

```

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

---

## Possible Improvements and Future Enhancements
This project is an educational prototype. Below are some potential directions to evolve it into a more production-ready solution, aligned with real-world Data/ML engineering practices and Rabobank’s requirements:

### Cloud Deployment (Azure)
- Store raw and processed data in Azure Blob Storage.
- Run Spark-based data processing and model training on Azure Databricks clusters.
- Use Azure Machine Learning for model versioning, deployment, and endpoint management.
- Integrate Azure Monitor or Application Insights for real-time pipeline health and performance tracking.

### Advanced Logging and Monitoring
- Implement structured logging via Python’s logging module (INFO, WARNING, ERROR levels).
- Save historical model metrics in a time-stamped folder (data/metrics_history/) for trend analysis.
- Set up basic alerts (email, Slack) in case of pipeline failures or model performance degradation.

### Full Test Coverage (Unit & Integration Tests)
- Extend test coverage to all pipeline steps: ingestion, processing, training, monitoring.
- Add integration tests for the end-to-end pipeline flow.
- Use pytest-cov to measure and improve test coverage.

### CI/CD Automation
- Configure GitHub Actions to:
  - Run linting (e.g., flake8, black) and unit tests on every pull request.
  - Build and push a Docker image of the pipeline and Airflow setup.
  - Enable seamless deployment to cloud or containerized environments.

### Model Evaluation Notebook
- Add a Jupyter Notebook for deeper analysis of model results:
  - ROC Curve and Precision-Recall Curve visualizations.
  - Feature importance or logistic regression coefficients.
  - Example predictions on real data batches.
  - This makes model performance easier to interpret and communicate.

### Configuration Management (Optional)
- Use .yaml or .env configuration files for paths, model hyperparameters, and data sources.
- Simplifies environment migration (local → cloud).

### Containerization with Docker (Optional)
- Package the entire pipeline and Airflow services into a Docker Compose setup.
- Ensures reproducibility and a standardized execution environment.
