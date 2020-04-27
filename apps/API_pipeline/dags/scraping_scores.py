from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.models import XCom 
from airflow.utils.dates import days_ago

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
    'ReclameAqui-scraping_scores',
    default_args=default_args,
    description='Coleta score no site Reclame Aqui e armazena no mongodb',
    schedule_interval=timedelta(days=1),
)


# jsondata = {'answered': '6666', 
#             'reclamations': '6151', 
#             'response_time': '15 dias e 21 horas ', 
#             'unanswered': '113'
#             }

company='Cielo'
collection='scores'
date = ''
args = {"metod" : 'GET', "company" : company, "collection" : collection }

t1 = PythonOperator (
            task_id = 'scores_reclameaqui',
            provide_context = False,
            python_callable = get_reclameaqui,
            op_kwargs=args,
            xcom_push=True,
            dag=dag
        )   


args = {"metod" : 'POST', "company" : company, "collection" : collection, "date" : date}
        #"jsondata" : {{ t1.xcom_pull('scores_reclameaqui') }} }

t2 = PythonOperator (
            task_id = 'persiste_dados_mongodb',
            provide_context = True,
            python_callable = crud_main,
            #op_kwargs=args,
            op_kwargs="{{ ti.xcom_pull('scores_reclameaqui') }}",
            dag=dag
        )

# args = {"metod" : 'GET', "company" : company, "collection" : collection}
# t3 = PythonOperator (
#             task_id = 'consulta_dados_company',
#             provide_context = False,
#             python_callable = crud_main,
#             op_kwargs=args,
#             dag=dag
#         )


# args = {"metod" : 'DELETE', "company" : company, "collection" : collection}
# t3 = PythonOperator (
#             task_id = 'delete_dados_company',
#             provide_context = False,
#             python_callable = crud_main,
#             op_kwargs=args,
#             dag=dag
#         )


# args = {"metod" : 'GET', "company" : company, "collection" : collection}
# t4 = PythonOperator (
#             task_id = 'consulta_dados_company2',
#             provide_context = False,
#             python_callable = crud_main,
#             op_kwargs=args,
#             dag=dag
#         )


t4 = BashOperator(
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

t1 >> t2 >> t4
