```execute
cd ~/hub-v3
```

```execute
ytt -f . | kbld -f - > /tmp/resources.yaml
```

```execute
kapp deploy -a jupyterhub -y -f /tmp/resources.yaml
```
