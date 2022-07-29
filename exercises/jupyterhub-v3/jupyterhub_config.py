import os

import tmpauthenticator
import kubespawner

# Set up authentication to allow anonymous user access.

c.JupyterHub.authenticator_class = tmpauthenticator.TmpAuthenticator

# Enable the use of the spawner for Kubernetes and set the target namespace
# for creating the Jupyter notebook instances to be the session namespace 
# of the workshop environment. Also specify the Jupyter notebook container
# image to be used.

c.JupyterHub.spawner_class = kubespawner.KubeSpawner

c.KubeSpawner.namespace = "default"

c.KubeSpawner.image = "jupyter/minimal-notebook:latest"

c.KubeSpawner.uid = 1000
c.KubeSpawner.gid = 100
c.KubeSpawner.supplemental_gids = [1]

# Override Jupyter port configuration to match what is configured for the
# workshop environment. The requirements for the IP address of the JupyterHub
# instance is a bit strange because for this test it is being run from the
# workshop environment container and not as a pod in the Kubernetes cluster.

c.JupyterHub.port = 8000
c.JupyterHub.hub_ip = "0.0.0.0"
c.JupyterHub.hub_port = 8001
c.JupyterHub.hub_connect_ip = os.environ[f"{os.environ['SESSION_NAMESPACE'].upper().replace('-', '_')}_JUPYTERHUB_SERVICE_HOST"]
c.ConfigurableHTTPProxy.api_url = f"http://127.0.0.1:8002"

# Increase startup timeouts since Jupyter notebook instances are slower
# to start up when run in pods versus local processes.

c.Spawner.start_timeout = 180
c.Spawner.http_timeout = 60
