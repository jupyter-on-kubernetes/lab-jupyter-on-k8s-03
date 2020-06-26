Using the simple local process spawner allows us to demonstrate how JupyterHub can provide separate Jupyter notebook instances for each authenticated user. Because all Jupyter notebooks instances in this case ran as the same UNIX user, within the same host, there was no separation between each.

When using Kubernetes, it provides the ability to have separation between different application instances by using containers. Each container will have its own environment which behaves much like a separate host, with its own separate file system, process space, IP address etc. In Kubernetes these separate application environments are called pods.

To create the container, we need access to a container image for the Jupyter notebook application. In the prior workshops we used one of the pre-built container images supplied by the Jupyter project. These are:

* jupyter/base-notebook
* jupyter/r-notebook
* jupyter/minimal-notebook
* jupyter/scipy-notebook
* jupyter/tensorflow-notebook
* jupyter/datascience-notebook
* jupyter/pyspark-notebook
* jupyter/all-spark-notebook

The GitHub repository used to create all the Jupyter project images can be found at:

https://github.com/jupyter/docker-stacks

The standard notebook image is ``jupyter/minimal-notebook``. It includes the Jupyter notebook application and JupyterLab extension, as well as the kernels for using Jupyter notebooks with the Python language.

The first step in using Kubernetes as the platform for running JupyterHub, is to configure the spawner used by JupyterHub to that for Kubernetes.

```
c.JupyterHub.spawner_class = "kubespawner.KubeSpawner"
```

Because how JupyterHub may be deployed into Kubernetes can vary, additional configuration will also be required to match what is applied by the deployment. The configuration may also need to vary based on the Jupyter notebook image selected to be used.

 To see the full configuration used in this case run:

```execute
cat jupyterhub-v3/jupyterhub_config.py
```

At this point we are actually cheating a bit, as JupyterHub itself is not being run from a pre-built container image, instead it is being run locally instead, with it relying on the fact that this workshop environment is running in Kubernetes and configured to allow access to the Kubernetes cluster to deploy workloads.

Before we can run JupyterHub with this configuration, we need to install the Python packages for the Kubernetes spawner and other components we need. To install all the Python packages required, run:

```execute
pip install -r jupyterhub-v3/requirements.txt
```

As the Kubernetes spawner is going to be creating the Jupyter notebook instances as separate pods, run a watch on pods being created.

```execute-2
watch kubectl get pods
```

Now run JupyterHub again, but tell it to use the new configuration file.

```execute-1
jupyterhub -f jupyterhub-v3/jupyterhub_config.py
```

To access the JupyterHub application click on the link:

http://{{session_namespace}}-8000.{{ingress_domain}}/

If this is the first time the Jupyter notebook image has been used with the Kubernetes cluster, it may take a while to spin up the instance as it will first need to pull down the container image from Docker Hub. The configuration has increased the startup timeout for the instance to accomodate for this, but if it does fail due to taking too long, retry until it works.

After being satisfied that the Jupyter notebook image is running correctly and you come back here, you should see that the watch on active pods shows an entry similar to the following:

```
NAME                                                  READY  STATUS   RESTARTS  AGE
jupyter-03d1bf03-2d6c4c-2d4b0f-2d8364-2dc30a32f3fd47  1/1    Running  0         60s
```

This is the details of the pod created to run the Jupyter notebook.

If you return to the Jupyter notebook web interface and click on the **Control Panel** button top right, then stop your Jupyter notebook service instance by clicking on **Stop My Server**, you should see that the pod running the instance will also be terminated.

This will only stop your Jupyter notebook instance and JupyterHub itself will still be running. You can therefore still start up a new instance of a Jupyter notebook from the web interface if desired.

When done, trigger the running JupyterHub instance to shutdown by interrupting it.

```execute-1
<ctrl-c>
```

If you hadn't shutdown the Jupyter notebook instance before doing this, you will see that the pod for the Jupyter notebook instance will also be terminated when JupyterHub is shutdown.

As we are down with this test, stop the watch on the pods.

```execute-2
<ctrl-c>
```
