import client.protos.ModelRunnerService_pb2 as model_pb2
import client.protos.ModelRunnerService_pb2_grpc as model_pb2_grpc
import grpc
from config import GRPC_MODEL_RUNNER_HOST


def update_running_state(state, run_id, container_id=None, exit_code=None, logs=None):
    channel = grpc.insecure_channel(GRPC_MODEL_RUNNER_HOST)
    stub = model_pb2_grpc.ModelRunnerServiceStub(channel)

    state_request = model_pb2.StateRequest(
        run_id=run_id,
        state=state,
    )
    if container_id is not None:
        state_request.container_id = container_id
    if exit_code is not None:
        state_request.container_exit_code = exit_code
    if logs is not None:
        state_request.logs = str(logs)

    res = stub.UpdateRunninState(state_request)
    print(f"gRPC Response: resolved={res.resolved}, error={res.err}")
