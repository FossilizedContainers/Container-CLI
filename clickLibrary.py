import click
import docker

# creating a group of commands that can be run
@click.group()
def cli():
    pass


# Requires: Initialized docker client
# TO DO:    Check if docker client is initialized, if not then pass an error
# adding the pull image command to the group and taking the name an image to pull
@cli.command()
@click.argument('image')
def pull_image(image):
    print(f"Pulling {image} image...")

    # Pull the specified image from dockerhub
    # Equivalent to: docker pull <image>
    image = client.images.pull(image)
    print(image.id + '\n')

# Requires: Initialized docker client,
#           Alpine image pulled and/or available
# TO DO:    Check if docker client is initialized, if not then pass an error
# TO DO:    Check if the image is available, if not then pass an error
# adding the hello-world command to the group
@cli.command()
def hello_world():
    print("\nStarting new container...")

    print("\nContainer Logs:")
    # Run the hello world container
    # Equivalent to: docker run alpine echo hello world
    print(client.containers.run("alpine", "echo hello world").decode("utf-8"))

# Requires: Initialized docker client,
#           Alpine image pulled and/or available
# TO DO:    Check if docker client is initialized, if not then pass an error
# TO DO:    Check if the image is available, if not then pass an error
# adding the detached-hello command to the group
@cli.command()
def detached_hello():
    #pull_alpine_img(client)
    print("\nStarting new detached container...")
    # Run the hellow world container, but this time we detach it and get the logs after
    # Equivalent to: docker run -d alpine echo hello world
    alpine_cont = client.containers.run("alpine", "echo hello world",
                                        detach=True)
    print("\nContainer Logs:")

    # print of the logs of the container
    # Equivalent to: docker logs <container_id>
    print(alpine_cont.logs().decode("utf-8"))

@cli.command()
@click.argument('filepath')
@click.argument('tagname')
def build(filepath, tagname):
    client.images.build(path=filepath, tag=tagname)

@cli.command()
@click.argument('filepath')
@click.argument('tagname')
def http_server(filepath, tagname):
    # Build the image first
    print('Building http server image if not built already...\n')
    client.images.build(path=filepath, tag=tagname)
    #build(filepath, tagname)
    print('Finished building the image...\n')
    # Running the container now
    #The port number, as an integer. For example, {'2222/tcp': 3333}
    #will expose port 2222 inside the container as port 3333 on the host.
    print('Now running the container...\n')
    port = {'80/tcp':4000}
    cont = client.containers.run('http-server', ports=port, tty=True, stdin_open=True, detach=True)
    print(cont.logs().decode('utf-8'))

# command mostly for testing
# will stop all containers and prune them
@cli.command()
def clean():
    for container in client.containers.list():
        container.stop()

    client.containers.prune()

# main to initiate variables and group
def main():
    global client
    client = docker.from_env()
    cli()

if __name__ == '__main__':
    main()
