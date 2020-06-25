import os

ingress_protocol = os.environ["INGRESS_PROTOCOL"]
ingress_domain = os.environ["INGRESS_DOMAIN"]
workshop_namespace = os.environ["WORKSHOP_NAMESPACE"]
session_namespace = os.environ["SESSION_NAMESPACE"]

c.JupyterHub.authenticator_class = "tmpauthenticator.TmpAuthenticator"

c.JupyterHub.spawner_class = "kubespawner.KubeSpawner"

c.JupyterHub.port = 8000
c.JupyterHub.hub_ip = "0.0.0.0"
c.JupyterHub.hub_port = 8081
c.JupyterHub.hub_connect_ip = f"{session_namespace}.{workshop_namespace}.svc.cluster.local"
c.ConfigurableHTTPProxy.api_url = f"http://{c.JupyterHub.hub_connect_ip}:8082"

c.Spawner.start_timeout = 120
c.Spawner.http_timeout = 60

c.KubeSpawner.namespace = session_namespace

"""
import wrapt

@wrapt.patch_function_wrapper('jupyterhub.proxy', 'ConfigurableHTTPProxy.add_route')
def _wrapper_add_route(wrapped, instance, args, kwargs):
    def _extract_args(routespec, target, data, *_args, **_kwargs):
        return (routespec, target, data, _args, _kwargs)

    routespec, target, data, _args, _kwargs = _extract_args(*args, **kwargs)

    old = 'http://%s:%s' % (c.JupyterHub.hub_connect_ip, c.JupyterHub.hub_port)
    new = 'http://127.0.0.1:%s' % c.JupyterHub.hub_port

    if target.startswith(old):
        target = target.replace(old, new)

    return wrapped(routespec, target, data, *_args, **_kwargs)
"""
