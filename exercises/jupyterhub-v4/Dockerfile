FROM jupyterhub/k8s-hub:0.9.0

USER root

RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && \
    npm install -G configurable-http-proxy

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py

USER ${NB_USER}
