import time

import client.docker as docker
import client.grpc as grpc
from config import CONTAINER_PREFIX


def check_containers_state():
    while True:
        try:
            print("--- check_container_status() ---")
            for container in docker.client.containers.list(all=True):
                container_name = container.name
                if container_name.startswith(CONTAINER_PREFIX):
                    container_status = container.status
                    if container_status == "exited":
                        exit_code = container.attrs["State"]["ExitCode"]
                        logs = container.logs().decode("utf-8")
                        print(
                            f"Container {container.id} finished with exit code {exit_code}"
                        )
                        grpc.update_running_state(
                            "finished",
                            container.name.split("_")[1],
                            container.id,
                            exit_code=exit_code,
                            logs=logs,
                        )
                        container.remove()
            time.sleep(3)
        except Exception as e:
            print("Error:", str(e))
