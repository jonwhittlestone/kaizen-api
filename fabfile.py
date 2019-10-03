from fabric.contrib.files import exists
from fabric.operations import _prefix_commands, _prefix_env_vars, require
from fabric.api import *

SERVER_PROJECT_PATH = '/var/www'
GIT_REMOTE = 'git@github.com:jonwhittlestone/kaizen-api.git'

env.roledefs = {
    'linode_vps': ['109.74.205.44']
}
env.user = 'jonwhittlestone'

@roles('linode_vps')
def deploy():
    # with cd(SERVER_PROJECT_PATH):
    pull_git_repo()

    with cd('%s/kaizen-api' % SERVER_PROJECT_PATH):
        run('docker-compose down')
        run('docker-compose up -d --build')


def pull_git_repo(git_branch='master'):
    with cd(SERVER_PROJECT_PATH):
        run(f'git clone --quiet {GIT_REMOTE}')
    with cd('%s/kaizen-api' % SERVER_PROJECT_PATH):
        run('git fetch --all')
        print(f'git checkout {git_branch}')
        run(f'git checkout {git_branch}')
        run('git log -1') # show latest commit message


'''
docker-comopose down
docker-compose up --build



'''
