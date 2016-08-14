# quicktry-lib

Library for sandboxing arbitrary script execution

# Getting started
This project requires docker and python3 to be installed. Using virtualenv is
encouraged.

Create and activate the project environment.
```
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

If this is your first time running the project or if there have been changes to
the list of supported languages, update the list of docker images.
```
$ ./rebuild_docker.sh
```

You can verify that everything is working by running a validation script (a
python script with various tests).
```
$ python test.py
```

We can then run the service locally.
```
$ ./run.sh
```

Alternatively, if you prefer to run things by hand, make sure that the
FLASK_APP variable is set to the top level app.py.
```
$ export FLASK_APP=app.py
$ flask run
```

You will now be able to access the locally hosted service by browsing to
`localhost:5000`.

Try running something simple to test the endpoints.

Using cURL:
```
$ curl -H "Content-Type: application/json" \
       -X POST -d '{"lang": "python2", "code":"print(\"hello world\")"}' \
       localhost:5000/run
```

Using httpie:
```
$ http GET localhost:5000/run code="print('hello')" lang="python2"
```

# Deployment
Deployment for this project hasn't been considered as of yet and has only been
tested locally. Use with caution whenever exposing your service to the world
wide web, docker isn't the be all end all for task isolation.

## Localhost deployment
Follow the `getting started` portion of the README. This should give you an
instance that is accesible to `localhost:5000`.

## Ngrok to tunnel localhost to a public endpoint
To determine that this application suits your needs, you can
reproduce a publically accessible instance quickly using ngrok to tunnel
localhost traffic to a public endpoint.

First set up ngrok by following the [getting started
documentation](https://dashboard.ngrok.com/get-started). Once you have
installed your authentication token, run the following command to tunnel all
traffic against localhost:5000 to a public endpoint.

```
$ ./ngrok http 5000
```

Port 5000 is the default port for flask development; adjust the value for your
specific usecase.

# Docker image sources
The docker images have been sourced from a variety of places, so we have
aggregated them here so you can view them from the source.

* [jfloff/alpine-python](https://github.com/jfloff/alpine-python)
* [frol/docker-alpine-python3](https://github.com/frol/docker-alpine-python3)
* [nodejs/docker-node/6.3](https://github.com/nodejs/docker-node)
