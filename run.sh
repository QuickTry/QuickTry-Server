#!/bin/bash

# This is a run script for development. This assumes that you are running the
# correct python environment, along with the docker service.
# `rebuild_docker.sh` should be called before running this script to ensure
# that the correct docker images exist for all supported languages. We run the
# flask application as localhost with debug enabled and forward the traffic
# over ngrok. This is not suggested for anything more rigorous than a
# hackathon!

set -o errexit
set -o xtrace

tmpdir="tmp"

# perform cleanup on interrupt
# TODO: kill all running docker containers containing quicktry
trap cleanup INT
function cleanup() {
    rm -r $tmpdir
}

# create the working directory for mounting docker volumes
if [ ! -d "$tmpdir" ]; then
    mkdir $tmpdir
fi

# run the flask application
export FLASK_APP=quicktry
export FLASK_DEBUG=1
python -m flask run
