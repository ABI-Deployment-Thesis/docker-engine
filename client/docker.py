import docker

from config import CONTAINER_PREFIX, DOCKER_HOST

# client = docker.from_env() # Default initialization
client = docker.DockerClient(base_url=DOCKER_HOST)


def build_and_run_container(
    run_id,
    model_type,
    dockerfile_path,
    model_file,
    input_features,
    mem_limit,
    nano_cpus,
    custom_tag="docker-engine",
):
    image, _ = client.images.build(path=dockerfile_path, tag=custom_tag)
    print(f"Image built with id {image.id} and tags {image.tags}")

    container_name = f"{CONTAINER_PREFIX}{run_id}"

    command = None
    if model_type == "predictive":
        command = ["--model_file", model_file, "--input_features", input_features]
        print(f"Running command: {command}")

    container = client.containers.run(
        custom_tag,
        name=container_name,
        command=command,
        mem_limit=mem_limit,  # Set memory limit (e.g., '256M' for 256MB)
        nano_cpus=nano_cpus,  # Set nano CPUs (e.g., 500000000 for 50% of a single CPU)
        labels={"traefik.enable": "false"},
        detach=True,
        auto_remove=False,
    )
    print(f"Container started with id {container.id} and name {container.name}")
    return image, container
