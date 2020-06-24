FROM jupyterhub/jupyterhub:1.2

RUN adduser --home /srv/jupyterhub --no-create-home --disabled-password \
    --uid 1001 --gid 0 --gecos "JupyterHub" jupyterhub

RUN chmod g+w /srv/jupyterhub

COPY --chown=1001:0 requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY --chown=1001:0 jupyterhub_config.py .

USER 1001
