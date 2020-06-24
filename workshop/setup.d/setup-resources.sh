#!/bin/bash

envsubst < exercises/jupyterhub-v3/values.yaml.in > exercises/jupyterhub-v3/values.yaml
envsubst < exercises/jupyterhub-v3/deployment.yaml.in > exercises/jupyterhub-v3/deployment.yaml
envsubst < exercises/jupyterhub-v3/ingress.yaml.in > exercises/jupyterhub-v3/ingress.yaml
