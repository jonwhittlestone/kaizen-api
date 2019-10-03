from fabric import task

# the directory of your project on your VPS
code_dir = '/home/jonwhittlestone/kaizen-api'

# here, you can provide a default hostname
# (from your .ssh/config)
default_hosts = ["109.74.205.44"]

# to perform the task on your default hosts, you
# have to pass them in each task decorator
@task(hosts=default_hosts)
def update(c):
    c.run("cd {} && git pull".format(code_dir))
    c.run("cd {} && docker-compose up --build -d".format(code_dir))