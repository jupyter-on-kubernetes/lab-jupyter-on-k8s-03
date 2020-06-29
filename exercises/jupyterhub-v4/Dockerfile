FROM jupyterhub/k8s-hub:0.9.0

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends nodejs=8.10.0~dfsg-2ubuntu0.2 nodejs-dev=8.10.0~dfsg-2ubuntu0.2 npm && \
    apt-get purge && \
    apt-get clean && \
    npm install -g configurable-http-proxy

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py

USER ${NB_USER}
