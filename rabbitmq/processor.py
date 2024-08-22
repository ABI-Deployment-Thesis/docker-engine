import json
import logging

import client.docker as docker
import client.grpc as grpc

logger = logging.getLogger(__name__)


def process_message(ch, method, properties, body):
    try:
        message = json.loads(body)
        run_id = message["run_id"]
        model_type = message["type"]
        folder_path = message["folder_path"]
        model_filename = message.get("model_filename")
        input_features = message.get("input_features")

        grpc.update_running_state("building", run_id)

    except json.JSONDecodeError as e:
        logger.error("JSON decoding failed:", str(e))
    except KeyError as e:
        logger.error(f"Missing key in message: {str(e)}")
    except Exception as e:
        logger.error("Unexpected error:", str(e))
    finally:
        ch.basic_ack(delivery_tag=method.delivery_tag)

    try:
        # ACK needs to be sent first, otherwise if the build takes too long, the RabbitMQ connection will be broken
        _, container = docker.build_and_run_container(
            run_id, model_type, folder_path, model_filename, input_features
        )
        grpc.update_running_state("running", run_id, container.id)
    except Exception as e:
        grpc.update_running_state(
            state="failed",
            run_id=run_id,
            logs=f"Container build/run failed: {e.args[0]}",
        )
        logger.error("Container build/run failed:", str(e))
