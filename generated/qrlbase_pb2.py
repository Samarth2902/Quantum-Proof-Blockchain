# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qrlbase.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='qrlbase.proto',
  package='qrl',
  syntax='proto3',
  serialized_pb=_b('\n\rqrlbase.proto\x12\x03qrl\"\x10\n\x0eGetNodeInfoReq\"5\n\x0fGetNodeInfoResp\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x11\n\tgrpcProto\x18\x02 \x01(\t2B\n\x04\x42\x61se\x12:\n\x0bGetNodeInfo\x12\x13.qrl.GetNodeInfoReq\x1a\x14.qrl.GetNodeInfoResp\"\x00\x62\x06proto3')
)




_GETNODEINFOREQ = _descriptor.Descriptor(
  name='GetNodeInfoReq',
  full_name='qrl.GetNodeInfoReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=38,
)


_GETNODEINFORESP = _descriptor.Descriptor(
  name='GetNodeInfoResp',
  full_name='qrl.GetNodeInfoResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='qrl.GetNodeInfoResp.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grpcProto', full_name='qrl.GetNodeInfoResp.grpcProto', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=93,
)

DESCRIPTOR.message_types_by_name['GetNodeInfoReq'] = _GETNODEINFOREQ
DESCRIPTOR.message_types_by_name['GetNodeInfoResp'] = _GETNODEINFORESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetNodeInfoReq = _reflection.GeneratedProtocolMessageType('GetNodeInfoReq', (_message.Message,), dict(
  DESCRIPTOR = _GETNODEINFOREQ,
  __module__ = 'qrlbase_pb2'
  # @@protoc_insertion_point(class_scope:qrl.GetNodeInfoReq)
  ))
_sym_db.RegisterMessage(GetNodeInfoReq)

GetNodeInfoResp = _reflection.GeneratedProtocolMessageType('GetNodeInfoResp', (_message.Message,), dict(
  DESCRIPTOR = _GETNODEINFORESP,
  __module__ = 'qrlbase_pb2'
  # @@protoc_insertion_point(class_scope:qrl.GetNodeInfoResp)
  ))
_sym_db.RegisterMessage(GetNodeInfoResp)



_BASE = _descriptor.ServiceDescriptor(
  name='Base',
  full_name='qrl.Base',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=95,
  serialized_end=161,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetNodeInfo',
    full_name='qrl.Base.GetNodeInfo',
    index=0,
    containing_service=None,
    input_type=_GETNODEINFOREQ,
    output_type=_GETNODEINFORESP,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BASE)

DESCRIPTOR.services_by_name['Base'] = _BASE

# @@protoc_insertion_point(module_scope)
