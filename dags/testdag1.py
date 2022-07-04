import pendulum

with DAG(
    dag_id='my_dag',
    description = "This is the sample dag for testing"
    start_date=pendulum.datetime(2016, 1, 1, tz="UTC"),
    schedule_interval='@daily',
    catchup=False,
    default_args={'retries': 2},
) as dag:
    op = BashOperator(task_id='dummy', bash_command='Hello World!')
    print(op.retries)  # 2
