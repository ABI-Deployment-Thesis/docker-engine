import docker
from config import CONTAINER_PREFIX, DOCKER_HOST

client = docker.DockerClient(base_url=DOCKER_HOST)


def build_and_run_container(
    run_id, dockerfile_path, model_file, input_features, custom_tag="docker-engine"
):
    image, logs = client.images.build(path=dockerfile_path, tag=custom_tag)
    print(f"Image built with id {image.id} and tags {image.tags}")

    container_name = f"{CONTAINER_PREFIX}{run_id}"

    command = ["--model_file", model_file, "--input_features", input_features]
    print(command)
    container = client.containers.run(
        custom_tag, name=container_name, command=command, detach=True, auto_remove=False
    )
    print(f"Container started with id {container.id} and name {container.name}")
    return image, container
