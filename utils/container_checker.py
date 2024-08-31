import time

import client.docker as docker
import client.grpc as grpc
from config import CONTAINER_PREFIX


def process_container(container):
    # Processes a single container, updating its state and removing it
    container_exit_code = container.attrs["State"]["ExitCode"]
    container_logs = container.logs().decode("utf-8")

    run_id = container.name.split("_")[1]
    state = "finished" if container_exit_code == 0 else "failed"
    result = container_logs if container_exit_code == 0 else ""
    logs = "" if container_exit_code == 0 else container_logs

    print(
        f"run_id={run_id}: Container {container.id} finished with exit code {container_exit_code}"
    )

    grpc.update_running_state(
        run_id=run_id,
        state=state,
        result=result,
        logs=logs,
    )
    container.remove()


def check_containers_state():
    while True:
        try:
            print("--- check_container_status() ---")
            containers = docker.client.containers.list(all=True)
            for container in containers:
                if (
                    container.name.startswith(CONTAINER_PREFIX)
                    and container.status == "exited"
                ):
                    process_container(container)
            time.sleep(3)
        except Exception as e:
            print("check_containers_state error:", str(e))
