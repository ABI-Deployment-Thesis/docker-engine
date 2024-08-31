import grpc

import client.protos.ModelRunnerService_pb2 as model_pb2
import client.protos.ModelRunnerService_pb2_grpc as model_pb2_grpc
from config import GRPC_MODEL_RUNNER_HOST


def update_running_state(run_id, state, result=None, logs=None):
    channel = grpc.insecure_channel(GRPC_MODEL_RUNNER_HOST)
    stub = model_pb2_grpc.ModelRunnerServiceStub(channel)

    state_request = model_pb2.StateRequest(
        run_id=run_id,
        state=state,
    )
    if result is not None:
        state_request.result = str(result)
    if logs is not None:
        state_request.logs = str(logs)

    res = stub.UpdateRunninState(state_request)
    print(
        f"run_id={run_id}: Attempting to update state={state}\n"
        f"grpc_response: resolved={res.resolved}, error={res.err}"
    )
