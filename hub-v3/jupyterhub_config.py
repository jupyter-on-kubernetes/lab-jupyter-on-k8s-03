c.JupyterHub.authenticator_class = "tmpauthenticator.TmpAuthenticator"

c.JupyterHub.spawner_class = "kubespawner.KubeSpawner"

c.JupyterHub.port = 8080
c.JupyterHub.hub_ip = "0.0.0.0"
c.JupyterHub.hub_port = 8081
c.JupyterHub.hub_connect_ip = "jupyterhub"

c.ConfigurableHTTPProxy.api_url = 'http://127.0.0.1:8082'

c.Spawner.start_timeout = 120
c.Spawner.http_timeout = 60

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

@wrapt.patch_function_wrapper('jupyterhub.spawner', 'LocalProcessSpawner.get_env')
def _wrapper_get_env(wrapped, instance, args, kwargs):
    env = wrapped(*args, **kwargs)

    target = env.get('JUPYTERHUB_API_URL')

    old = 'http://%s:%s' % (c.JupyterHub.hub_connect_ip, c.JupyterHub.hub_port)
    new = 'http://127.0.0.1:%s' % c.JupyterHub.hub_port

    if target and target.startswith(old):
        target = target.replace(old, new)
        env['JUPYTERHUB_API_URL'] = target

    return env
