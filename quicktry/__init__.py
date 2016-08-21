from flask import Flask
from quicktry.sandbox import Sandbox
import yaml


# Create the flask application
app = Flask(__name__)
app.config.from_envvar('QUICKTRY_SETTINGS')


# Load the connection to the docker manager
with open(app.config['LANGUAGE_CONFIG']) as f:
    config = yaml.load(f)
sandbox = Sandbox(config['languages'])


import quicktry.views
import quicktry.commands
