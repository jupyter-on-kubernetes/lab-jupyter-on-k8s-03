```execute
<ctrl-c>
```

```execute
pip install jupyterhub-kubespawner
```

```execute
cat hub-v3/jupyterhub_config.py
```

```execute
jupyterhub -f hub-v3/jupyterhub_config.py
```

{{ingress_protocol}}://{{session_namespace}}-local-8000.{{ingress_domain}}/
