FROM jupyter/scipy-notebook:python-3.8.8
USER root
#install Arctic

# RUN apt-get update
RUN pip install git+https://github.com/manahl/arctic.git
RUN conda install -c conda-forge ta-lib jupyter-server-proxy
ADD /jlab/requirements.txt /home
RUN pip install -r /home/requirements.txt
RUN jupyter labextension install jupyterlab-dash
RUN jupyter labextension install @jupyterlab/server-proxy

# ned@capogrecogroup.com quandl account API key for downloading data for Zipline
#ENV QUANDL_API_KEY=Y8wmszaeR4twaAGSJ9T4
#RUN zipline ingest