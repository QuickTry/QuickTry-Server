import click
import os
import json
import re
from quicktry import app
from docker import Client


@app.cli.command()
def rebuild():
    """ Rebuild all the docker images. """
    click.echo("Rebuilding all docker images")

    docker_url='unix://var/run/docker.sock'
    cli = Client(base_url=docker_url, version='auto')

    path = app.config.get('DOCKERFILE_PATH')
    if not path:
        click.ClickException("Path to dockerfiles does not exist.")

    languages = os.listdir(path)

    for lang in languages:
        click.echo("building image for {}".format(lang))
        dockerfile = os.path.join(path, lang, 'Dockerfile')
        with open(dockerfile, 'rb') as f:
            # NOTE: using the build output is surprisingly hard because
            # it's formatted as a (sometimes inconsistent) list of json.
            # https://github.com/docker/docker-py/issues/255
            cli.build(fileobj=f, rm=True, tag='{}:latest'.format(lang))