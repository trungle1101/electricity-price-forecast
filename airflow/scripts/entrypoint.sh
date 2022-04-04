#!/usr/bin/env bash
export PYTHON_PATH=~/airflow/
python -m pip install --user --upgrade pip
pip install --user  --no-cache-dir -r /opt/airflow/scripts/requirements.txt
airflow db init
airflow users create --firstname admin --lastname admin --email admin --password admin --username admin --role Admin
airflow webserver