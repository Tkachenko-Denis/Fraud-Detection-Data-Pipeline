# Fraud Detection Data Pipeline

Прототип end-to-end ML-пайплайна для детекции финансового мошенничества

## Цели проекта

- Смоделировать рабочий процесс Data Engineer / ML Engineer:
  - Сбор данных транзакций (ingestion)
  - Очистка, проверка качества и генерация фичей
  - Обучение модели для выявления мошенничества
  - Мониторинг качества данных и метрик модели
  - Оркестрация процесса в Airflow
- Продемонстрировать навыки:
  - **Python, PySpark, scikit-learn**
  - **ETL-процессы, Data Quality**
  - **ML lifecycle orchestration (Airflow)**
  - **Проектирование решений, масштабируемых на Azure**

---

## Архитектура проекта

```mermaid
flowchart TD
    A[Ingestion: CSV -> Parquet] --> B[Processing: PySpark Cleaning & Features]
    B --> C[Model Training: Logistic Regression]
    C --> D[Monitoring: Data Quality & Metrics Check]
    D -->|Airflow DAG| E[End-to-End Pipeline]

## Технологии проекта
- **Python 3.10+**
- **Pandas, PySpark – обработка данных**
- **scikit-learn – обучение модели**
- ** Great Expectations – проверки качества данных**
- ** Apache Airflow – оркестрация пайплайна** 
- ** Jupyter Notebook – EDA и визуализация**
- ** Parquet, csv – форматы хранения данных**

## Установка и запуск
Linux
Клонировать репозиторий:

git clone https://github.com/Tkachenko-Denis/fraud-detection-pipeline.git
cd fraud-detection-pipeline

Создать виртуальное окружение и установить зависимости:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Выполнить пайплайн вручную:

python src/ingest_data.py
python src/process_data_spark.py
python src/train_model.py
python src/monitor_data_quality.py

Запустить Airflow:

airflow standalone

Важно! В файле airflow.cfg нужно поменять путь в dags_folder на тот, в котором хранится DAG 
Открыть http://localhost:8080 и активировать DAG fraud_detection_pipeline. 

