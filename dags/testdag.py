import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import timedelta
default_args = {
    'start_date': airflow.utils.dates.days_ago(0),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag_id = DAG{
    'test1',
    default_args=default_args,
    description='hjh'
    schedule_interval=NONE,
    dagrun_timeout=timedelta(minutes=20))
  
