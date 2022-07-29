In this workshop you have seen how you can create your own containerised deployment of JupyterHub running in Kubernetes.

The Jupyter project team does have the Zero to JupyterHub with Kubernetes project, but it is designed for a very large scale deployment supporting many thousands of users.

For smaller personal deployments, or deployments in an organisation, using an architecture able to support very large scale deployments may not be a wise choice and may consume more resources for the base install than you want.

The alternative as illustrated in this workshop provides a basic structure you can use to create your own containerised deployment customised to your own specific use case.

As written, to customise the example provided, you would modify the ``jupyterhub_config.py`` file to configure JupyterHub, and if necessary also modify the Kubernetes resources for the deployment.
