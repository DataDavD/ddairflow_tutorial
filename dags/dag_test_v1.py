# import packages
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from external_func import random_date


def start_print():
    print('\nDAG starting...\n')


def end_print():
    print('\nDAG end...\nCONGRATS DD!\n')


default_args = {
    'owner': 'DavD',
    'depends_on_past': False,
    'start_date': datetime(2019, 3, 3),
    'email': 'email@email.com',
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
    'concurrency': 1
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG(dag_id='dd_test_v1',
          default_args=default_args,
          schedule_interval=timedelta(minutes=5))

# t1, t2, t3, and t5 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='Date',
    bash_command='date',
    dag=dag)

t2 = PythonOperator(
    task_id='py_1',
    python_callable=start_print,
    dag=dag)

t3 = PythonOperator(
    task_id='py_2',
    python_callable=random_date,
    dag=dag)

t4 = PythonOperator(
    task_id='py_3',
    python_callable=end_print,
    dag=dag)

t1 >> t2 >> t3 >> t4
