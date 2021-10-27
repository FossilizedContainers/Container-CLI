## CLI Using Click and Docker API

Command line interface that shows how to use the Docker API

```bash
# how to pull a specific image from dockerhub 
$ python clickLibrary.py pull-image ubuntu

# create a container using the alpine image that returns hello world
$ python clickLibrary.py hello-world

# create a detached container that returns hello world
$ python clickLibrary.py detached-hello
```