c.JupyterHub.authenticator_class = "tmpauthenticator.TmpAuthenticator"

c.JupyterHub.spawner_class = "kubespawner.KubeSpawner"

c.JupyterHub.hub_ip = "0.0.0.0"
c.JupyterHub.hub_port = 8081
c.JupyterHub.hub_connect_ip = "jupyterhub"

c.ConfigurableHTTPProxy.api_url = 'http://127.0.0.1:8082'

c.Spawner.start_timeout = 120
c.Spawner.http_timeout = 60

c.KubeSpawner.port = 8080
