from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators import GetReclameAqui, PersisteDatabase
from airflow.utils.dates import days_ago


company='Cielo'
collection='reclamations'

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
        'scraping_and_persist_reclamations',
        default_args=default_args,
        description='Coleta as 10 reclamacoes mais recentes do site ReclameAqui e armazena no mongodb',
        schedule_interval=timedelta(days=1),
        )

scraping_reclameaqui = GetReclameAqui(
                        company = company,
                        collection = collection,
                        task_id = 'consulta_reclameaqui',
                        provide_context = True,
                        xcom_push = True,
                        dag=dag
                        )

persist_database = PersisteDatabase(
                        method = 'POST',
                        company = company,
                        collection = collection,
                        task_id = 'persiste_database',
                        provide_context = True,
                        xcom_pull = True,
                        dag=dag
                        )

scraping_reclameaqui >> persist_database