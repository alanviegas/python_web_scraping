from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.http_operator import SimpleHttpOperator

from airflow.utils.dates import days_ago

from airflow.models.xcom import XCom, XCOM_RETURN_KEY

from datetime import timedelta
import json

from scripts.requests_database import crud_main
from scripts.requests_site import get_reclameaqui

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['alan.viegas@semantix.com.br'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}

dag = DAG(
    'ReclameAqui_scraping_scores',
    default_args=default_args,
    description='Coleta score no site Reclame Aqui e armazena no mongodb',
    schedule_interval=timedelta(days=1),
)


company='Cielo'
collection='scores' 

args_t1 = {"company" : company}
t1 = SimpleHttpOperator(
                task_id='consulta_scores_reclameaqui',
                provide_context=True,
                endpoint = 'http://api_consultareclameaqui:5000/{}'.format(collection),
                method = 'GET',
                response_check = True,
                xcom_push = True,
                log_response = True, 
                data = args_t1 
            )


t2 = SimpleHttpOperator(
                task_id='persiste_dados_mongodb',
                endpoint = 'http://api_persistenciadados:5005/{}'.format(collection),
                method = 'POST',
                headers = {'content-type': 'application/json'},
                response_check = True,
                log_response = True, 
                kwargs = args_t2,
                #data = t1.xcom_pull.re(context=['consulta_scores_reclameaqui'],   
                #                    task_ids='consulta_scores_reclameaqui')     -- isto não esta funcionando
            )


t3 = BashOperator(
            task_id='print_date',
            bash_command='date',
            dag=dag
        )


dag.doc_md = __doc__

t1.doc_md = """\
#### Task Documentation
You can document your task using the attributes `doc_md` (markdown),
`doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets
![img](http://montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)
rendered in the UI's Task Instance Details page.
"""

t1 >> t2 >> t3
