FROM jupyterhub/jupyterhub:latest

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY jupyterhub_config.py .
