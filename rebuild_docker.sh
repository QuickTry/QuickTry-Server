#!/bin/bash

for path in docker-images/*; do
    # skip if not directory
    [ -d "${path}" ] || continue

    # building docker images
    dirname=`basename ${path}`
    docker build -t quicktry-${dirname}:latest ${path}
done
