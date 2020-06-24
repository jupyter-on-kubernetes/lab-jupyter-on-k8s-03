#!/bin/bash

envsubst < exercises/hub-v3/values.yaml.in > exercises/hub-v3/values.yaml
envsubst < exercises/hub-v3/deployment.yaml.in > exercises/hub-v3/deployment.yaml
envsubst < exercises/hub-v3/ingress.yaml.in > exercises/hub-v3/ingress.yaml
