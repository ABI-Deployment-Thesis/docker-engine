# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: client/protos/ModelRunnerService.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&client/protos/ModelRunnerService.proto\"K\n\x0cStateRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\t\x12\r\n\x05state\x18\x02 \x01(\t\x12\x0e\n\x06result\x18\x03 \x01(\t\x12\x0c\n\x04logs\x18\x04 \x01(\t\".\n\rStateResponse\x12\x10\n\x08resolved\x18\x01 \x01(\x08\x12\x0b\n\x03\x65rr\x18\x02 \x01(\t2H\n\x12ModelRunnerService\x12\x32\n\x11UpdateRunninState\x12\r.StateRequest\x1a\x0e.StateResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client.protos.ModelRunnerService_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_STATEREQUEST']._serialized_start=42
  _globals['_STATEREQUEST']._serialized_end=117
  _globals['_STATERESPONSE']._serialized_start=119
  _globals['_STATERESPONSE']._serialized_end=165
  _globals['_MODELRUNNERSERVICE']._serialized_start=167
  _globals['_MODELRUNNERSERVICE']._serialized_end=239
# @@protoc_insertion_point(module_scope)
