```execute
cd ~/exercises/jupyterhub-v4
```

```execute
skaffold build
```

```execute
skopeo inspect docker://{{session_namespace}}-registry.{{ingress_domain}}/jupyterhub:latest
```

```execute
tree resources -P '*.yaml'
```

```execute
kubectl apply -f resources
```

```execute
kubectl rollout status deployment/jupyterhub
```

http://{{session_namespace}}-jupyterhub.{{ingress_domain}}/
