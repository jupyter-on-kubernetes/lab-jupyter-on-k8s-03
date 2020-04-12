```execute
cd ~/hub-v3
```

```execute
podman build -t custom-jupyterhub .
```

```execute
podman tag custom-jupyterhub {{REGISTRY_HOST}}/custom-jupyterhub:latest
```

```execute
podman push {{REGISTRY_HOST}}/custom-jupyterhub:latest
```

```execute
ytt -f . | kbld -f - | kapp deploy -a jupyterhub -y -f -
```

http://{{session_namespace}}-jupyterhub.{{ingress_domain}}
