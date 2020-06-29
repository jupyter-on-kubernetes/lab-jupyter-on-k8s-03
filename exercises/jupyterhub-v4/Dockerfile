FROM jupyterhub/k8s-hub:0.9.0

USER root

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py

USER ${NB_USER}
