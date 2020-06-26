# Set up authentication to allow anonymous user access.

c.JupyterHub.authenticator_class = "tmpauthenticator.TmpAuthenticator"

# Enable the use of the spawner for Kubernetes and specify the Jupyter
# notebook container image to be used.

c.JupyterHub.spawner_class = "kubespawner.KubeSpawner"

c.KubeSpawner.image = "jupyter/minimal-notebook:latest"

# Override Jupyter port configuration to match what is configured for the
# workshop environment.

c.JupyterHub.port = 8000
c.JupyterHub.hub_ip = "0.0.0.0"
c.JupyterHub.hub_port = 8001
c.JupyterHub.hub_connect_ip = "jupyterhub"
c.ConfigurableHTTPProxy.api_url = f"http://127.0.0.1:8002"

# Increase startup timeouts since Jupyter notebook instances are slower
# to start up when run in pods versus local processes.

c.Spawner.start_timeout = 180
c.Spawner.http_timeout = 60

# Configure location for database and cookie secret file. The target
# directory will be replaced with a persistent volume.

c.JupyterHub.db_url = "/opt/app-root/data/database.sqlite"
c.JupyterHub.cookie_secret_file = "/opt/app-root/data/cookie_secret"

# Patch JupyterHub to workaround a bug/limitation in certain Kubernetes
# environments (minikube), which prevents a process connecting to a port
# in the same pod via an exposed service name for the application. See:
# https://github.com/kubernetes/minikube/issues/1568 for details. This
# causes issues when the JupyterHub proxy is running in the same pod as
# JupyterHub itself.

import wrapt

@wrapt.patch_function_wrapper("jupyterhub.proxy", "ConfigurableHTTPProxy.add_route")
def _wrapper_add_route(wrapped, instance, args, kwargs):
    def _extract_args(routespec, target, data, *_args, **_kwargs):
        return (routespec, target, data, _args, _kwargs)

    routespec, target, data, _args, _kwargs = _extract_args(*args, **kwargs)

    old = "http://%s:%s" % (c.JupyterHub.hub_connect_ip, c.JupyterHub.hub_port)
    new = "http://127.0.0.1:%s" % c.JupyterHub.hub_port

    if target.startswith(old):
        target = target.replace(old, new)

    return wrapped(routespec, target, data, *_args, **_kwargs)
