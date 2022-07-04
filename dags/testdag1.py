import os
from datetime import timedelta

from airflow import DAG
from airflow.models.baseoperator import chain
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.providers.amazon.aws.operators.glue_crawler import AwsGlueCrawlerOperator
from airflow.utils.dates import days_ago

DAG_ID = os.path.basename(__file__).replace(".py", "")

with DAG(
    dag_id='my_dag',
    description = "this is a sample dag for unit testing"
    schedule_interval='None',
    catchup=False,
    default_args={'retries': 2},
) as dag:
    op = BashOperator(task_id='dummy', bash_command='Hello World!')
    print(op.retries)  # 2
