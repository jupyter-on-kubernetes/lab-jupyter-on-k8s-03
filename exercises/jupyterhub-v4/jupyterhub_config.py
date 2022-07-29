import tmpauthenticator
import kubespawner

# Set up authentication to allow anonymous user access.

c.JupyterHub.authenticator_class = tmpauthenticator.TmpAuthenticator

# Enable the use of the spawner for Kubernetes and specify the Jupyter
# notebook container image to be used.

c.JupyterHub.spawner_class = kubespawner.KubeSpawner

c.KubeSpawner.image = "jupyter/minimal-notebook:latest"

c.KubeSpawner.uid = 1000
c.KubeSpawner.gid = 100
c.KubeSpawner.supplemental_gids = [1]

# Override Jupyter port configuration to match what is configured for the
# Kubernetes environment.

c.JupyterHub.port = 8000
c.JupyterHub.hub_ip = "0.0.0.0"
c.JupyterHub.hub_port = 8001
c.JupyterHub.hub_connect_ip = "jupyterhub"
c.ConfigurableHTTPProxy.api_url = "http://127.0.0.1:8002"

# Increase startup timeouts since Jupyter notebook instances are slower
# to start up when run in pods versus local processes.

c.Spawner.start_timeout = 180
c.Spawner.http_timeout = 60

# Configure location for database and cookie secret file. The target
# directory will be replaced with a persistent volume.

c.JupyterHub.db_url = "/var/run/jupyterhub/database.sqlite"
c.JupyterHub.cookie_secret_file = "/var/run/jupyterhub/cookie_secret"
