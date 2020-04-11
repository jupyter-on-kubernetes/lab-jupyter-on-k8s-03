import os

from jupyterhub.spawner import LocalProcessSpawner

class SingleUserLocalProcessSpawner(LocalProcessSpawner):

    def user_env(self, env):
        env["USER"] = "eduk8s"
        env["HOME"] = f"/home/eduk8s/sessions/{self.user.name}"
        env["SHELL"] = "/bin/bash"
        return env

    def make_preexec_fn(self, name):
        def preexec():
            home = f"/home/eduk8s/sessions/{name}"
            os.makedirs(home, exist_ok=True)
            os.chdir(home)
        return preexec

c.JupyterHub.spawner_class = SingleUserLocalProcessSpawner

c.JupyterHub.authenticator_class = "tmpauthenticator.TmpAuthenticator"
