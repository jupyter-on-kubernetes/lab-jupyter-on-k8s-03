The reason for the failure is that JupyterHub by default is configured to use what is called the local process spawner. This spawner will create the Jupyter notebook instances as local processes, but in doing that it attempts to run them as the Linux user under which the session was logged in.

In our case, the user name allocated to the session is a random value and there is no corresponding Linux user account for it. Thus the failure in looking up the details for the user.

Like the authenticator, the spawner used by JupyterHub can also be replaced.

To see our new configuration for JupyterHub run:

```execute
cat jupyterhub-v2/jupyterhub_config.py
```

The output should be:

```
c.JupyterHub.authenticator_class = "tmpauthenticator.TmpAuthenticator"

c.JupyterHub.spawner_class = "jupyterhub.spawner.SimpleLocalProcessSpawner"
```

In this case we replace the default local process spawner with a simplified version which allows us to create a Jupyter notebook instance per session, but where the Jupyter notebook instances run as the same user as JupyterHub. To allow some measure of separation, each session is assigned its own directory in which to save any work.

This spawner is only intended for development and you would never use this spawner if wanting to host Jupyter notebooks for many users since there is no proper separation between users as they share the same file system, and even the same Python virtual environment. We are using it here as an example as it helps introduce the concept of the spawner used by JupyterHub to create the Jupyter notebook instances.

Run JupyterHub again, but tell it to use this configuration file.

```execute
jupyterhub -f jupyterhub-v2/jupyterhub_config.py
```

To access the JupyterHub application click on the link:

{{ingress_protocol}}://{{session_namespace}}-8000.{{ingress_domain}}/

This time we are successfully able to launch a Jupyter notebook session.

![Jupyter Notebook Session](jupyter-notebook-session.png)

Because we are using ``tmpauthenticator.TmpAuthenticator`` for managing user authentication, every distinct user browser session will be assigned their own separate session. The problem we have right now is that these are just separate processes on the one host and so users could interfere with each other.

Before continuing, trigger the running JupyterHub instance to shutdown by interrupting it.

```execute
<ctrl-c>
```
