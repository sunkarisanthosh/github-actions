import os
from datetime import timedelta

from airflow import DAG
from airflow.models.baseoperator import chain
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

DAG_ID = os.path.basename(__file__).replace(".py", "")


with DAG(
    dag_id=DAG_ID,
    description="Run AWS Glue ETL Jobs - source data to raw (bronze) data",
    default_args=DEFAULT_ARGS,
    dagrun_timeout=timedelta(minutes=5),
    start_date=days_ago(1),
    schedule_interval=None,
    tags=["data lake demo", "raw", "bronze"],
) as dag:
    begin = DummyOperator(task_id="begin")
    end = DummyOperator(task_id="end")
