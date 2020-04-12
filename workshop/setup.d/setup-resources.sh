#!/bin/bash

envsubst < hub-v3/values.yaml.in > hub-v3/values.yaml
envsubst < hub-v3/ingress.yaml.in > hub-v3/ingress.yaml
envsubst < hub-v3/sources.yaml.in > hub-v3/sources.yaml
envsubst < hub-v3/imagedestinations.yaml.in > hub-v3/imagedestinations.yaml
