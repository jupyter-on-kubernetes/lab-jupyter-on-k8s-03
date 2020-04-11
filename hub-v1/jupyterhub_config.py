from jupyterhub.spawner import LocalProcessSpawner

class SingleUserLocalProcessSpawner(LocalProcessSpawner):

    def user_env(self, env):
        env['USER'] = 'eduk8s'
        env['HOME'] = '/home/eduk8s'
        env['SHELL'] = '/bin/bash'
        return env

    def make_preexec_fn(self, name):
        def preexec():
            pass
        return preexec

c.JupyterHub.spawner_class = SingleUserLocalProcessSpawner

c.JupyterHub.authenticator_class = 'tmpauthenticator.TmpAuthenticator'
