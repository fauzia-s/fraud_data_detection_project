import os
import json
import pandas as pd
from datetime import datetime
#from airflow.operators.email_operator import EmailOperator
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.providers.postgres.operators.postgres import PostgresOperator
import psycopg2

def load_transaction_data( ** kwargs):
    try:
       conn = psycopg2.connect("dbname=airflow user=airflow password=airflow host=postgres port=5432",options='-c search_path=public')
    except:
       print('Can\'t connect to postgres DB.Failing the task')

    cur = conn.cursor()

    with open('/opt/airflow/dags/data/train_transaction.csv', 'r') as f:
       next(f) # Skip the header row.
       cur.copy_from(f, 'transactions', sep = ',')
    conn.commit()   
    print('Loading data into  transaction table successful')

def load_identity_data( ** kwargs):
    try:
       conn = psycopg2.connect("dbname=airflow user=airflow password=airflow host=postgres port=5432",options='-c search_path=public')
    except:
       print('Can\'t connect to postgres DB.Failing the task')

    cur = conn.cursor()

    with open('/opt/airflow/dags/data/train_identity.csv', 'r') as f:
       next(f) # Skip the header row.
       cur.copy_from(f, 'identity', sep = ',')
    conn.commit()
    print('Loading data into identity table successful')




default_args = {
    'owner': 'airflow',
    'start_date': datetime(2021, 10, 22),
    'retries': 1
}
with DAG('fraud_data_etl_dag',
         schedule_interval='@daily',
         default_args=default_args,
         description='A simple data pipeline for ingesting Fraud data',
         catchup=False) as dag:

    transaction_file_sensor_task = FileSensor(
        task_id='transaction_file_sensor',
        poke_interval= 30,
        filepath="/opt/airflow/dags/data/train_transaction.csv"
    )
    
    identity_file_sensor_task = FileSensor(
        task_id='identity_file_sensor',
        poke_interval= 30,
        filepath="/opt/airflow/dags/data/train_identity.csv"
    )

    create_transactions_table = PostgresOperator(
        task_id = "create_transactions_table",
        postgres_conn_id = "postgres_fraud_etl",
        sql = "sql/create_transactions_table.sql",
        dag = dag)
     
    create_identity_table = PostgresOperator(
        task_id = "create_identity_table",
        postgres_conn_id = "postgres_fraud_etl",
        sql = "sql/create_identity_table.sql",
        dag = dag)



    load_transaction_task = PythonOperator(
    task_id='load_transaction',
    python_callable=load_transaction_data)

    load_identity_task = PythonOperator(
    task_id='load_identity',
    python_callable=load_identity_data)



   # send_email = EmailOperator(
   #     task_id='send_email',
   #     to=['test@test.com'],
   #     subject='Fraud data for today has been ingested',
   #     html_content='Please check your dashboard. :)'
   # )

    transaction_file_sensor_task >> create_transactions_table >> load_transaction_task 
    identity_file_sensor_task >> create_identity_table >> load_identity_task

    #file_sensor_task >> create_transactions_table >> load_transaction_task >> send_email


