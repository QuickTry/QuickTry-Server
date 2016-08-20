from flask import Flask
from quicktry.sandbox import Sandbox
import yaml


# Load the connection to the docker manager
with open('languages.yml') as f:
    config = yaml.load(f)
sandbox = Sandbox(config['languages'])


# Create the flask application
app = Flask(__name__)
app.config.from_object(__name__)

import quicktry.views