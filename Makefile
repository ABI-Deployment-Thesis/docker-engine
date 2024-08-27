ifneq (,$(wildcard .env.development))
    include .env.development
    export
endif

# Variables
IMAGE_NAME ?= abi-deployment-thesis/docker-engine
TAG ?= dev

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME):$(TAG) .

generate-protos:
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./client/protos/ModelRunnerService.proto