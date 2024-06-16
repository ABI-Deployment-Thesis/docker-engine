import os

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE", "docker_queue")
GRPC_MODEL_RUNNER_HOST = os.getenv("GRPC_MODEL_RUNNER_HOST", "127.0.0.1:50052")
DOCKER_HOST = os.getenv("DOCKER_HOST", "tcp://127.0.0.1:2375")
DOCKER_TAG = os.getenv("DOCKER_TAG", "docker-engine")
CONTAINER_PREFIX = os.getenv("CONTAINER_PREFIX", "run_")
