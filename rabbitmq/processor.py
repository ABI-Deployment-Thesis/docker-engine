import json

import client.docker as docker
import client.grpc as grpc


def process_message(ch, method, properties, body):
    try:
        message = json.loads(body)
        run_id = message["run_id"]
        model_type = message["type"]
        folder_path = message["folder_path"]
        model_filename = message.get("model_filename")
        input_features = message.get("input_features")
        mem_limit = message.get("mem_limit", "256M")
        nano_cpus = message.get("cpu_percentage", 500000000)

        grpc.update_running_state(run_id, "building")
        _, _ = docker.build_and_run_container(
            run_id,
            model_type,
            folder_path,
            model_filename,
            input_features,
            mem_limit,
            nano_cpus,
        )
        grpc.update_running_state(run_id, "running")

    except Exception as e:
        grpc.update_running_state(
            run_id=run_id,
            state="failed",
            logs=f"Container build/run failed: {e.args[0]}",
        )
        print(f"run_id={run_id}: Container build/run failed:\n{str(e)}")
    finally:
        ch.basic_ack(delivery_tag=method.delivery_tag)
