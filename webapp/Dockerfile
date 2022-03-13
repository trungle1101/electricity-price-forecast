FROM python:3.8-slim

ADD /webapp/requirements.txt /webapp/

WORKDIR /webapp

RUN pip install -r /webapp/requirements.txt

ADD ./webapp /webapp

ENV ENVIRONMENT_FILE=".env"

EXPOSE 8085

ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "index:server"]