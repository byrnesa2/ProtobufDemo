# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: interface-values.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='interface-values.proto',
  package='interfacevalues',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16interface-values.proto\x12\x0finterfacevalues\"\x94\x02\n\tDroneInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x35\n\x08location\x18\x02 \x03(\x0b\x32#.interfacevalues.DroneInfo.Location\x12\x39\n\nsearcharea\x18\x03 \x03(\x0b\x32%.interfacevalues.DroneInfo.SearchArea\x1a*\n\x08Location\x12\x0e\n\x06xcoord\x18\x01 \x01(\x05\x12\x0e\n\x06ycoord\x18\x02 \x01(\x05\x1a[\n\nSearchArea\x12\x12\n\nupperbound\x18\x01 \x01(\x05\x12\x11\n\tleftbound\x18\x02 \x01(\x05\x12\x12\n\nlowerbound\x18\x03 \x01(\x05\x12\x12\n\nrightbound\x18\x04 \x01(\x05\"8\n\x07MapInfo\x12-\n\tdroneinfo\x18\x01 \x03(\x0b\x32\x1a.interfacevalues.DroneInfo'
)




_DRONEINFO_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='interfacevalues.DroneInfo.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='xcoord', full_name='interfacevalues.DroneInfo.Location.xcoord', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ycoord', full_name='interfacevalues.DroneInfo.Location.ycoord', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=185,
  serialized_end=227,
)

_DRONEINFO_SEARCHAREA = _descriptor.Descriptor(
  name='SearchArea',
  full_name='interfacevalues.DroneInfo.SearchArea',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='upperbound', full_name='interfacevalues.DroneInfo.SearchArea.upperbound', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='leftbound', full_name='interfacevalues.DroneInfo.SearchArea.leftbound', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lowerbound', full_name='interfacevalues.DroneInfo.SearchArea.lowerbound', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rightbound', full_name='interfacevalues.DroneInfo.SearchArea.rightbound', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=229,
  serialized_end=320,
)

_DRONEINFO = _descriptor.Descriptor(
  name='DroneInfo',
  full_name='interfacevalues.DroneInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='interfacevalues.DroneInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='interfacevalues.DroneInfo.location', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='searcharea', full_name='interfacevalues.DroneInfo.searcharea', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DRONEINFO_LOCATION, _DRONEINFO_SEARCHAREA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=320,
)


_MAPINFO = _descriptor.Descriptor(
  name='MapInfo',
  full_name='interfacevalues.MapInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='droneinfo', full_name='interfacevalues.MapInfo.droneinfo', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=322,
  serialized_end=378,
)

_DRONEINFO_LOCATION.containing_type = _DRONEINFO
_DRONEINFO_SEARCHAREA.containing_type = _DRONEINFO
_DRONEINFO.fields_by_name['location'].message_type = _DRONEINFO_LOCATION
_DRONEINFO.fields_by_name['searcharea'].message_type = _DRONEINFO_SEARCHAREA
_MAPINFO.fields_by_name['droneinfo'].message_type = _DRONEINFO
DESCRIPTOR.message_types_by_name['DroneInfo'] = _DRONEINFO
DESCRIPTOR.message_types_by_name['MapInfo'] = _MAPINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DroneInfo = _reflection.GeneratedProtocolMessageType('DroneInfo', (_message.Message,), {

  'Location' : _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
    'DESCRIPTOR' : _DRONEINFO_LOCATION,
    '__module__' : 'interface_values_pb2'
    # @@protoc_insertion_point(class_scope:interfacevalues.DroneInfo.Location)
    })
  ,

  'SearchArea' : _reflection.GeneratedProtocolMessageType('SearchArea', (_message.Message,), {
    'DESCRIPTOR' : _DRONEINFO_SEARCHAREA,
    '__module__' : 'interface_values_pb2'
    # @@protoc_insertion_point(class_scope:interfacevalues.DroneInfo.SearchArea)
    })
  ,
  'DESCRIPTOR' : _DRONEINFO,
  '__module__' : 'interface_values_pb2'
  # @@protoc_insertion_point(class_scope:interfacevalues.DroneInfo)
  })
_sym_db.RegisterMessage(DroneInfo)
_sym_db.RegisterMessage(DroneInfo.Location)
_sym_db.RegisterMessage(DroneInfo.SearchArea)

MapInfo = _reflection.GeneratedProtocolMessageType('MapInfo', (_message.Message,), {
  'DESCRIPTOR' : _MAPINFO,
  '__module__' : 'interface_values_pb2'
  # @@protoc_insertion_point(class_scope:interfacevalues.MapInfo)
  })
_sym_db.RegisterMessage(MapInfo)


# @@protoc_insertion_point(module_scope)