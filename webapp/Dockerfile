FROM python:3.8-slim

ADD /webapp/requirements.txt /proj/webapp/

WORKDIR /proj

COPY requirements.txt /

RUN pip install -r /proj/webapp/requirements.txt

ADD ./webapp /proj/webapp

ENV ENVIRONMENT_FILE=".env"

EXPOSE 8085

ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "index:server"]