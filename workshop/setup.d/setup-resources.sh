#!/bin/bash

envsubst < hub-v3/values.yaml.in > hub-v3/values.yaml
envsubst < hub-v3/deployment.yaml.in > hub-v3/deployment.yaml
envsubst < hub-v3/ingress.yaml.in > hub-v3/ingress.yaml
