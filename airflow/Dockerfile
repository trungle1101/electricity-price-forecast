FROM apache/airflow:2.1.0-python3.8
RUN python -m pip install --user --upgrade pip
#USER root
#RUN apt-get update \
#  && apt-get install -y --no-install-recommends \
#         dos2unix \
#  && apt-get autoremove -yqq --purge \
#  && apt-get clean \
#  && rm -rf /var/lib/apt/lists/*
#USER airflow
#ADD /airflow/scripts/requirements.txt /tmp
#RUN pip install --no-cache-dir --user -r /tmp/requirements.txt
USER root
RUN apt-get update \
&& apt-get install -y wkhtmltopdf
USER airflow
ADD /airflow/scripts/requirements.txt /opt/airflow/scripts/
RUN pip install --no-cache-dir --user -r /opt/airflow/scripts/requirements.txt
#ENV PYTHONPATH ~/airflow/
