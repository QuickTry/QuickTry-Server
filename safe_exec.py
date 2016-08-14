import os
import tempfile
from docker import Client

def execute(workdir, data, stdin):
    # create the client to the docker service
    cli = Client(base_url='unix://var/run/docker.sock')

    # generate the temporary path for the worker
    with tempfile.TemporaryDirectory(dir=workdir) as dirpath:
        print(dirpath)
        return
        # create the input file
        with open(os.path.join(dirpath, 'input.py'), 'w') as f:
            f.write(data)

        host_config = cli.create_host_config(
                binds=['{}:/tmp'.format(dirpath)])

        container = cli.create_container(
                volumes=['/tmp'],
                image='alpine-python2:latest',
                command='python /tmp/input.py > /tmp/output.txt',
                host_config=host_config )

        response = cli.start(container=container.get('Id'))
        with open(os.path.join(dirpath, 'output.txt')) as f:
                print(f.read())


if __name__ == '__main__':
    workdir = os.path.join(os.getcwd(), 'tmp')
    script = 'print("hello")'
    stdin = None

    execute(workdir, script, stdin)
