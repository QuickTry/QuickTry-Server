""" A set of functions to interact with code execution in an isolated docker
sandbox."""
from docker import Client
import os
import tempfile

class Sandbox:

    def __init__(self, config, docker_url='unix://var/run/docker.sock'):
        # maps a language to a command and filename extension
        self.config = config
        self.cli = Client(base_url=docker_url, version='auto')

    def query_images(self):
        """ Return a list of images that are used by this machine to execute
        aribitary code. We return the language names. """
        images = self.cli.images()

        # only interested in the tag names
        tags = [image['RepoTags'][0] for image in images]
        tags = [tag for tag in tags if tag.startswith('quicktry-')]

        return tags

    def get_languages(self):
        return list(self.config.keys())

    def execute(self, language, data, stdin, workdir):
        options = self.config.get(language)
        if not options:
            msg = "{} is not a supported language".format(language)
            return -1, msg

        # generate the temporary path for the worker
        with tempfile.TemporaryDirectory(dir=workdir) as dirpath:
            # create the input file
            input_file="input.{}".format(options["ext"])
            with open(os.path.join(dirpath, input_file), 'w') as f:
                f.write(data.encode().decode('unicode_escape'))

            # define the docker container. mount a temporary directory for the
            # input file
            host_config = self.cli.create_host_config(
                    binds=['{}/:/mnt/data'.format(dirpath)])

            # TODO: handle stdin
            container = self.cli.create_container(
                    volumes = ['/mnt/data'],
                    host_config = host_config,
                    image = "quicktry-{}:latest".format(language),
                    command = options['command'])

            # run the script and read stdout
            c_id = container.get('Id')
            self.cli.start(container=c_id)

            # wait on the container to finish, 30 second timeout
            try:
                ret = self.cli.wait(container=c_id, timeout=30)
            except:
                self.cli.stop(container=c_id)
                return -1, "execution timed out after 30s"

            output = self.cli.logs(container=c_id, stdout=True).decode()

            return ret, output
