FROM jupyterhub/k8s-hub:1.1.3

USER root

RUN apt-get update && \
    curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y --no-install-recommends nodejs && \
    apt-get purge && \
    apt-get clean && \
    npm install -g configurable-http-proxy

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY jupyterhub_config.py /usr/local/etc/jupyterhub/jupyterhub_config.py

USER 1000
