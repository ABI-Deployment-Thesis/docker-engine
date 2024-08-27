<div align="center">
    <a href="https://www.eng.uminho.pt" target="_blank"><img src="https://i.imgur.com/mOynow9.png" alt="Engineering School"/></a>
    <a href="https://www.uminho.pt" target="_blank"><img src="https://i.imgur.com/1gtSAGM.png" alt="University Of Minho"/></a>
    <br/>
    <a href="http://www.dsi.uminho.pt" target="_blank">
        <strong>Information Systems Department</strong>
    </a>
    <br/>
    <br/>
    <a href="https://github.com/ABI-Deployment-Thesis/docker-engine/actions"><img alt="Tests Status" src="https://github.com/ABI-Deployment-Thesis/docker-engine/actions/workflows/tests.yaml/badge.svg"></a>
    <a href="https://github.com/ABI-Deployment-Thesis/docker-engine/releases"><img alt="GitHub Release" src="https://img.shields.io/github/v/release/ABI-Deployment-Thesis/docker-engine"></a>
    <a href="https://github.com/ABI-Deployment-Thesis/docker-engine/blob/main/LICENSE"><img alt="GitHub License" src="https://img.shields.io/github/license/ABI-Deployment-Thesis/docker-engine"></a>
</div>

<h2 align="center">ABI Deployment Thesis - Docker Engine</h2>

Welcome to the docker-engine repository! This project is a key part of a master's thesis at the University of Minho. It's a Proof of Concept for a proposed architecture designed to deploy and integrate intelligent models within Adaptive Business Intelligence (ABI) systems.

**This repository provides a microservice for running intelligent models through the Docker daemon.**

For a detailed explanation of the proposed architecture and its deployment strategy, please refer to the published article: [Architecture proposal for deploying and integrating intelligent models in ABI](https://www.sciencedirect.com/science/article/pii/S1877050923022445).

## Quick Start

- For setup instructions and initial configuration, please follow the guidelines provided in the [infrastructure repository](https://github.com/ABI-Deployment-Thesis/component-core?tab=readme-ov-file#quick-start).

## Networking

- Ingress
    - Consumes data from a RabbitMQ queue.
    - Retrieves data from storage.
- Egress
    - Communicates with the model-runner microservice to send data about intelligent model runs.
- Both
    - Communicates with the Docker daemon to build and retrieve information about images.

## Development

```sh
# Generate gRPC client and server code
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./client/protos/ModelRunnerService.proto

# Start RabbitMQ
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management-alpine
```

## Author

- Rui Gomes ([LinkedIn](https://www.linkedin.com/in/ruigomes99))

## License

- [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/)