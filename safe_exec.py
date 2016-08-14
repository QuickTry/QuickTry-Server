import os
import tempfile
from docker import Client


def execute(workdir, data, stdin):
    # create the client to the docker service
    cli = Client(base_url='unix://var/run/docker.sock')

    # generate the temporary path for the worker
    with tempfile.TemporaryDirectory(dir=workdir) as dirpath:
        print(dirpath)

        # create the input file
        with open(os.path.join(dirpath, 'input.py'), 'w') as f:
            f.write(data)

        host_config = cli.create_host_config(
                binds=['{}/:/mnt/data'.format(dirpath)])

        container = cli.create_container(
                volumes=['/mnt/data'],
                image='alpine-python2:latest',
                command='python /mnt/data/input.py',
                host_config=host_config )

        c_id = container.get('Id')
        response = cli.start(container=c_id)
        output = cli.logs(container=c_id, stdout=True)
        print(output)


if __name__ == '__main__':
    workdir = os.path.join(os.getcwd(), 'tmp')
    script = 'for i in range(10):\n\tprint("hello")'
    stdin = None

    execute(workdir, script, stdin)
