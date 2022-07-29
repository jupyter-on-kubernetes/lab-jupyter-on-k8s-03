#!/bin/bash

kubectl create secret docker-registry session-registry-pull \
 --docker-username=$REGISTRY_USERNAME --docker-password=$REGISTRY_PASSWORD \
 --docker-email=workshop@example.com --docker-server=$REGISTRY_HOST \
 --dry-run=client -o yaml | kubectl apply -f - -n default
