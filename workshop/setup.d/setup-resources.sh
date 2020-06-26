#!/bin/bash

envsubst < exercises/jupyterhub-v4/resources/values.yaml.in > exercises/jupyterhub-v4/resources/values.yaml
envsubst < exercises/jupyterhub-v4/resources/deployment.yaml.in > exercises/jupyterhub-v4/resources/deployment.yaml
envsubst < exercises/jupyterhub-v4/resources/ingress.yaml.in > exercises/jupyterhub-v4/resources/ingress.yaml
