#!/usr/bin/env bash
airflow db init
airflow users create -r Admin -u admin -e admin@example.com -f admin -l user -p admin1234
airflow connections add 'postgres_fraud_etl' \
    --conn-type 'postgres' \
    --conn-login 'airflow' \
    --conn-password 'airflow' \
    --conn-host 'postgres' \
    --conn-port '5432' \
    --conn-schema 'airflow'
airflow webserver
