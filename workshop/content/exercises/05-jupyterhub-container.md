In order to run JupyterHub in a container of its own, rather than locally, we need a container image for JupyterHub.

The Jupyter project provides a number of container images for JupyterHub. The first of these are:

* jupyterhub/jupyterhub
* jupyterhub/jupyterhub-onbuild

These two container images are designed for use with the ``DockerSpawner`` and are not suitable for use in Kubernetes.

The next is:

* jupyterhub/k8s-hub

This is the container image which is used in the helm templates of the Zero to JupyterHub with Kubernetes project. Although created for use with Kubernetes, it will not work for a more basic JupyterHub deployment.

The problem with this container image is that it expects the JupyterHub proxy to be run in a separate container of its own. We can remedy this by extending the image to add in the JupyterHub proxy.

Change to the ``~/exercises/jupyterhub-v4`` sub directory in the first terminal.

```execute-1
cd ~/exercises/jupyterhub-v4
```

as well as the second terminal.

```execute-2
cd ~/exercises/jupyterhub-v4
```

To view the contents of the ``Dockerfile`` run:

```execute
cat Dockerfile
```

The file should contain:

```
FROM jupyterhub/k8s-hub:0.9.0

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      nodejs=8.10.0~dfsg-2ubuntu0.2 \
      nodejs-dev=8.10.0~dfsg-2ubuntu0.2 npm && \
    apt-get purge && \
    apt-get clean && \
    npm install -g configurable-http-proxy

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py

USER 1000
```

The ``Dockerfile`` can be used to build a container image using ``docker build``, however, in this workshop environment the ``docker`` command cannot be used. Instead we will use ``kaniko`` to build the container image.

Because running ``kaniko`` directly is a bit fiddly, we are going to use ``skaffold`` to trigger the build. To do this run the command:

```execute-2
skaffold build
```

When running ``kaniko`` to build a container image, a build pod will be created in the Kubernetes cluster. This will create the container image, and when done push the resulting image to an image registry.

While the image is being built, you can check out the ``jupyterhub_config.py`` file being used.

```execute-1
cat jupyterhub_config.py
```

The configuration is similar to before, with details related to how the JupyterHub instance is accessed from within the cluster being changed.

When the build has completed, to verify details of the image created, run:

```execute
skopeo inspect docker://{{session_namespace}}-registry.{{ingress_domain}}/jupyterhub:latest
```

The view the resource files to deploy JupyterHub using this container image run:

```execute
tree resources -P '*.yaml'
```

To create the deployment run:

```execute
kubectl apply -f resources
```

Monitor the deployment by running:

```execute
kubectl rollout status deployment/jupyterhub
```

When the deployment has completed, access the JupyterHub application by clicking on the link:

http://{{session_namespace}}-jupyterhub.{{ingress_domain}}/
