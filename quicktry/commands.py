import click
from quicktry import app

@app.cli.command()
def rebuild():
    """ Rebuild all the docker images from quicktry/docker-images """
    click.echo("Rebuild all docker images")