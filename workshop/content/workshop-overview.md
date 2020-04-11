This is the third workshop exploring the options for deploying Jupyter notebooks to Kubernetes. The first workshop covered how to deploy Jupyter notebooks locally to your own computer, then moved onto the steps required to deploy to Kubernetes. The second workshop looked at using a Kubernetes operator to implement the steps to deploy a Jupyter notebook to Kubernetes.

In both workshops, the method of deployment required access to the Kubernetes cluster. It was not possible for a user to trigger the creation of a Jupyter notebook instance for their own use without access to the Kubernetes cluster.

This workshop is going to investigate the use of an intermediate application for spawning Jupyter notebook sessions for users. In particular, we will look at the use of JupyterHub.

For running JupyterHub on Kubernetes, the go to solution supported by the Jupyter project is the [Zero to JupyterHub with Kubernetes](https://github.com/jupyterhub/zero-to-jupyterhub-k8s) project. Although this solution does work, that this project is supported by the Jupyter project has more or less resulted in no competing solutions of note being developed for deploying JupyterHub and Jupyter notebooks to Kubernetes, at least no community base solutions.

Alternative solutions have been developed by cloud solution providers and other commercial organisations for a specific cloud platform, but these are in effect proprietary solutions where none of the code is available, or which is tied to that organisations infrastructure.

This workshop therefore is going to ignore the Zero to JupyterHub with Kubernetes project and look at the basics steps for deploying JupyterHub to Kubernetes and see if that spawns some ideas of what could be a better solution to the problem.
