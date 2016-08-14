import os
import tempfile
from docker import Client


def query_images():
    """ Return a list of images that are used by this machine to execute
    aribitary code. We return the language names. """
    cli = Client(base_url='unix://var/run/docker.sock', version='auto')
    images = cli.images()

    # only interested in the tag names
    tags = [image['RepoTags'][0] for image in images]
    tags = [tag for tag in tags if tag.startswith('quicktry-')]

    return tags


def execute(workdir, data, stdin):
    # create the client to the docker service
    cli = Client(base_url='unix://var/run/docker.sock', version='auto')

    # generate the temporary path for the worker
    with tempfile.TemporaryDirectory(dir=workdir) as dirpath:
        print(dirpath)

        # create the input file
        with open(os.path.join(dirpath, 'input.py'), 'w') as f:
            f.write(data)

        # define the docker container. mount a temporary directory for the
        # input file
        host_config = cli.create_host_config(
                binds=['{}/:/mnt/data'.format(dirpath)])

        # TODO: change the image and command appropriately for the type of
        # input file that we recieve
        # TODO: handle stdin
        container = cli.create_container(
                volumes=['/mnt/data'],
                image='quicktry-python2:latest',
                command='python /mnt/data/input.py',
                host_config=host_config )

        # run the script and read stdout
        # TODO: error handling
        c_id = container.get('Id')
        response = cli.start(container=c_id)
        output = cli.logs(container=c_id, stdout=True)

        return output


if __name__ == '__main__':
    workdir = os.path.join(os.getcwd(), 'tmp')
    script = 'for i in range(10):\n\tprint("hello")'
    stdin = None

    output = execute(workdir, script, stdin)
    print(output)
