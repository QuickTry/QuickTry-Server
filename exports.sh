#!/bin/bash

# Useful exports to have while running quicktry locally. This can be used by
# sourcing the file.

# This tells the flask cli where to look for the current application
export PYTHONPATH=`pwd`

# Define the location of the flask appliction
export FLASK_APP=quicktry

# This is the location to the default configuration file. This configuration
# file is important because it also points to the location of the language
# configuration.
export QUICKTRY_SETTINGS=$(pwd)/config.cfg
