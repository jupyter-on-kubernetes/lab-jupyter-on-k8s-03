import os

c.JupyterHub.authenticator_class = "tmpauthenticator.TmpAuthenticator"

c.JupyterHub.spawner_class = "kubespawner.KubeSpawner"

c.KubeSpawner.namespace = os.environ.get("SESSION_NAMESPACE")
c.JupyterHub.hub_ip = 
c.JupyterHub.hub_connect_ip =
