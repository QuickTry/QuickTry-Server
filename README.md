# quicktry-lib

Library for sandboxing arbitrary script execution

# Running
This project requires docker and python3 to be installed.

First generate the images that will be used for isolated code execution.
```
$ ./rebuild_docker.sh
```

Once these are available, make sure that the library runs against the `test.py`
script. 

# Docker image sources
* [jfloff/alpine-python](https://github.com/jfloff/alpine-python)
* [frol/docker-alpine-python3](https://github.com/frol/docker-alpine-python3)

