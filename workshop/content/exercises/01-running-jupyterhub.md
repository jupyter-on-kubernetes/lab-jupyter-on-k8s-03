Our eventual target is to be able to run JupyterHub in Kubernetes in a container from a container image, but we are going to start by deploying it locally first.

Following best practice, first create a Python virtual environment in which to install the JupyterHub and Jupyter notebook software. To do this, run:

```execute
python3 -m venv jupyter
```

Having created the Python virtual environment, activate it so the Python runtime from the Python virtual environment is used.

```execute
source jupyter/bin/activate
```

Before installing and additional Python packages, ensure the latest version of ``pip`` is installed into the Python virtual environment by running:

```execute
pip install -U pip
```

In order to work in its default configuration, JupyterHub needs to use a proxy, which is used to route user sessions to their respective Jupyter notebook instances. This proxy is implemented in node.js. To install it run:

```execute
npm install -g configurable-http-proxy
```

Now install JupyterHub using:

```execute
pip install jupyterhub
```

Initially we are going to have JupyterHub spawn local instances of the Jupyter notebook application, so we install it as well.

```execute
pip install notebook jupyterlab
```
