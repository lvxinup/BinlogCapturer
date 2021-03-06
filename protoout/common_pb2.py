# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common.proto',
  package='baikaldb.pb',
  syntax='proto2',
  serialized_options=_b('\200\001\001'),
  serialized_pb=_b('\n\x0c\x63ommon.proto\x12\x0b\x62\x61ikaldb.pb\"\x9b\x01\n\nSchemaConf\x12\x12\n\nneed_merge\x18\x01 \x01(\x08\x12 \n\x18storage_compute_separate\x18\x02 \x01(\x08\x12\x1c\n\x14select_index_by_cost\x18\x03 \x01(\x08\x12\x12\n\nop_version\x18\x04 \x01(\x03\x12\x0f\n\x07op_desc\x18\x05 \x01(\t\x12\x14\n\x0c\x66ilter_ratio\x18\x06 \x01(\x02\"\x97\x01\n\x0eSlotDescriptor\x12\x0f\n\x07slot_id\x18\x01 \x02(\x05\x12-\n\tslot_type\x18\x02 \x02(\x0e\x32\x1a.baikaldb.pb.PrimitiveType\x12\x10\n\x08tuple_id\x18\x03 \x02(\x05\x12\x10\n\x08table_id\x18\x04 \x01(\x03\x12\x10\n\x08\x66ield_id\x18\x05 \x01(\x05\x12\x0f\n\x07ref_cnt\x18\x06 \x01(\x05\"a\n\x0fTupleDescriptor\x12\x10\n\x08tuple_id\x18\x01 \x02(\x05\x12\x10\n\x08table_id\x18\x02 \x01(\x03\x12*\n\x05slots\x18\x03 \x03(\x0b\x32\x1b.baikaldb.pb.SlotDescriptor\"\xd0\x01\n\tExprValue\x12(\n\x04type\x18\x01 \x02(\x0e\x32\x1a.baikaldb.pb.PrimitiveType\x12\x10\n\x08\x62ool_val\x18\x02 \x01(\x08\x12\x11\n\tint32_val\x18\x03 \x01(\x05\x12\x12\n\nuint32_val\x18\x04 \x01(\r\x12\x11\n\tint64_val\x18\x05 \x01(\x03\x12\x12\n\nuint64_val\x18\x06 \x01(\x04\x12\x11\n\tfloat_val\x18\x07 \x01(\x02\x12\x12\n\ndouble_val\x18\x08 \x01(\x01\x12\x12\n\nstring_val\x18\t \x01(\x0c*\x87\x05\n\x07\x45rrCode\x12\x0b\n\x07SUCCESS\x10\x00\x12\x0e\n\nNOT_LEADER\x10\x01\x12\x16\n\x12PARSE_FROM_PB_FAIL\x10\x02\x12\x14\n\x10PARSE_TO_PB_FAIL\x10\x03\x12\x16\n\x12UNSUPPORT_REQ_TYPE\x10\x04\x12\x15\n\x11INPUT_PARAM_ERROR\x10\x05\x12\x12\n\x0eGET_VALUE_FAIL\x10\x06\x12\x12\n\x0ePUT_VALUE_FAIL\x10\x07\x12\x15\n\x11\x44\x45LETE_VALUE_FAIL\x10\x08\x12\x12\n\x0eINTERNAL_ERROR\x10\t\x12\x0f\n\x0bVERSION_OLD\x10\n\x12\x17\n\x13REGION_ERROR_STATUS\x10\x0b\x12\r\n\tEXEC_FAIL\x10\x0c\x12\x19\n\x15\x44ISABLE_WRITE_TIMEOUT\x10\r\x12\x11\n\rSPLIT_TIMEOUT\x10\x0e\x12\x18\n\x14REGION_ALREADY_EXIST\x10\x0f\x12\x14\n\x10REGION_NOT_EXIST\x10\x10\x12\x11\n\rHAVE_NOT_INIT\x10\x11\x12\x11\n\rTXN_FOLLOW_UP\x10\x12\x12\x13\n\x0f\x43\x41NNOT_ADD_PEER\x10\x13\x12\x12\n\x0ePEER_NOT_EQUAL\x10\x14\x12\x10\n\x0c\x43ONNECT_FAIL\x10\x15\x12\r\n\tCANCELLED\x10\x16\x12\x17\n\x13\x44\x44L_UNIQUE_KEY_FAIL\x10\x17\x12\x13\n\x0fTXN_IS_EXISTING\x10\x18\x12\x13\n\x0fTXN_IS_ROLLBACK\x10\x19\x12\x19\n\x15\x42\x41\x43KUP_SAME_LOG_INDEX\x10\x1a\x12\x10\n\x0c\x42\x41\x43KUP_ERROR\x10\x1b\x12\x0f\n\x0bRETRY_LATER\x10\x1c\x12\x17\n\x13LESS_THAN_OLDEST_TS\x10\x1d\x12\x0e\n\nIN_PROCESS\x10\x1e*\x8c\x02\n\rPrimitiveType\x12\x10\n\x0cINVALID_TYPE\x10\x00\x12\r\n\tNULL_TYPE\x10\x01\x12\x08\n\x04\x42OOL\x10\x02\x12\x08\n\x04INT8\x10\x03\x12\t\n\x05INT16\x10\x04\x12\t\n\x05INT32\x10\x05\x12\t\n\x05INT64\x10\x06\x12\t\n\x05UINT8\x10\x07\x12\n\n\x06UINT16\x10\x08\x12\n\n\x06UINT32\x10\t\x12\n\n\x06UINT64\x10\n\x12\t\n\x05\x46LOAT\x10\x0b\x12\n\n\x06\x44OUBLE\x10\x0c\x12\n\n\x06STRING\x10\r\x12\x0c\n\x08\x44\x41TETIME\x10\x0e\x12\r\n\tTIMESTAMP\x10\x0f\x12\x08\n\x04\x44\x41TE\x10\x10\x12\x07\n\x03HLL\x10\x11\x12\x08\n\x04TIME\x10\x12\x12\x10\n\x0cPLACE_HOLDER\x10\x13\x12\x07\n\x03HEX\x10\x14*%\n\nSchemaType\x12\x0b\n\x07\x44YNAMIC\x10\x01\x12\n\n\x06STATIC\x10\x02*@\n\x06\x45ngine\x12\x0b\n\x07ROCKSDB\x10\x01\x12\t\n\x05REDIS\x10\x02\x12\x12\n\x0eROCKSDB_CSTORE\x10\x03\x12\n\n\x06\x42INLOG\x10\x04\x42\x03\x80\x01\x01')
)

_ERRCODE = _descriptor.EnumDescriptor(
  name='ErrCode',
  full_name='baikaldb.pb.ErrCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_LEADER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARSE_FROM_PB_FAIL', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARSE_TO_PB_FAIL', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORT_REQ_TYPE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INPUT_PARAM_ERROR', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_VALUE_FAIL', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PUT_VALUE_FAIL', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE_VALUE_FAIL', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERSION_OLD', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGION_ERROR_STATUS', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXEC_FAIL', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISABLE_WRITE_TIMEOUT', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPLIT_TIMEOUT', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGION_ALREADY_EXIST', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGION_NOT_EXIST', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HAVE_NOT_INIT', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TXN_FOLLOW_UP', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_ADD_PEER', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PEER_NOT_EQUAL', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONNECT_FAIL', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCELLED', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DDL_UNIQUE_KEY_FAIL', index=23, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TXN_IS_EXISTING', index=24, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TXN_IS_ROLLBACK', index=25, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BACKUP_SAME_LOG_INDEX', index=26, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BACKUP_ERROR', index=27, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RETRY_LATER', index=28, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LESS_THAN_OLDEST_TS', index=29, number=29,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IN_PROCESS', index=30, number=30,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=652,
  serialized_end=1299,
)
_sym_db.RegisterEnumDescriptor(_ERRCODE)

ErrCode = enum_type_wrapper.EnumTypeWrapper(_ERRCODE)
_PRIMITIVETYPE = _descriptor.EnumDescriptor(
  name='PrimitiveType',
  full_name='baikaldb.pb.PrimitiveType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NULL_TYPE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOL', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT8', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT16', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT32', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT64', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT8', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT16', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT32', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT64', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATETIME', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMESTAMP', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATE', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HLL', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIME', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLACE_HOLDER', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEX', index=20, number=20,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1302,
  serialized_end=1570,
)
_sym_db.RegisterEnumDescriptor(_PRIMITIVETYPE)

PrimitiveType = enum_type_wrapper.EnumTypeWrapper(_PRIMITIVETYPE)
_SCHEMATYPE = _descriptor.EnumDescriptor(
  name='SchemaType',
  full_name='baikaldb.pb.SchemaType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DYNAMIC', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATIC', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1572,
  serialized_end=1609,
)
_sym_db.RegisterEnumDescriptor(_SCHEMATYPE)

SchemaType = enum_type_wrapper.EnumTypeWrapper(_SCHEMATYPE)
_ENGINE = _descriptor.EnumDescriptor(
  name='Engine',
  full_name='baikaldb.pb.Engine',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ROCKSDB', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REDIS', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROCKSDB_CSTORE', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BINLOG', index=3, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1611,
  serialized_end=1675,
)
_sym_db.RegisterEnumDescriptor(_ENGINE)

Engine = enum_type_wrapper.EnumTypeWrapper(_ENGINE)
SUCCESS = 0
NOT_LEADER = 1
PARSE_FROM_PB_FAIL = 2
PARSE_TO_PB_FAIL = 3
UNSUPPORT_REQ_TYPE = 4
INPUT_PARAM_ERROR = 5
GET_VALUE_FAIL = 6
PUT_VALUE_FAIL = 7
DELETE_VALUE_FAIL = 8
INTERNAL_ERROR = 9
VERSION_OLD = 10
REGION_ERROR_STATUS = 11
EXEC_FAIL = 12
DISABLE_WRITE_TIMEOUT = 13
SPLIT_TIMEOUT = 14
REGION_ALREADY_EXIST = 15
REGION_NOT_EXIST = 16
HAVE_NOT_INIT = 17
TXN_FOLLOW_UP = 18
CANNOT_ADD_PEER = 19
PEER_NOT_EQUAL = 20
CONNECT_FAIL = 21
CANCELLED = 22
DDL_UNIQUE_KEY_FAIL = 23
TXN_IS_EXISTING = 24
TXN_IS_ROLLBACK = 25
BACKUP_SAME_LOG_INDEX = 26
BACKUP_ERROR = 27
RETRY_LATER = 28
LESS_THAN_OLDEST_TS = 29
IN_PROCESS = 30
INVALID_TYPE = 0
NULL_TYPE = 1
BOOL = 2
INT8 = 3
INT16 = 4
INT32 = 5
INT64 = 6
UINT8 = 7
UINT16 = 8
UINT32 = 9
UINT64 = 10
FLOAT = 11
DOUBLE = 12
STRING = 13
DATETIME = 14
TIMESTAMP = 15
DATE = 16
HLL = 17
TIME = 18
PLACE_HOLDER = 19
HEX = 20
DYNAMIC = 1
STATIC = 2
ROCKSDB = 1
REDIS = 2
ROCKSDB_CSTORE = 3
BINLOG = 4



_SCHEMACONF = _descriptor.Descriptor(
  name='SchemaConf',
  full_name='baikaldb.pb.SchemaConf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='need_merge', full_name='baikaldb.pb.SchemaConf.need_merge', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='storage_compute_separate', full_name='baikaldb.pb.SchemaConf.storage_compute_separate', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='select_index_by_cost', full_name='baikaldb.pb.SchemaConf.select_index_by_cost', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='op_version', full_name='baikaldb.pb.SchemaConf.op_version', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='op_desc', full_name='baikaldb.pb.SchemaConf.op_desc', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter_ratio', full_name='baikaldb.pb.SchemaConf.filter_ratio', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=30,
  serialized_end=185,
)


_SLOTDESCRIPTOR = _descriptor.Descriptor(
  name='SlotDescriptor',
  full_name='baikaldb.pb.SlotDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='slot_id', full_name='baikaldb.pb.SlotDescriptor.slot_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slot_type', full_name='baikaldb.pb.SlotDescriptor.slot_type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tuple_id', full_name='baikaldb.pb.SlotDescriptor.tuple_id', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='table_id', full_name='baikaldb.pb.SlotDescriptor.table_id', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='field_id', full_name='baikaldb.pb.SlotDescriptor.field_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ref_cnt', full_name='baikaldb.pb.SlotDescriptor.ref_cnt', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=188,
  serialized_end=339,
)


_TUPLEDESCRIPTOR = _descriptor.Descriptor(
  name='TupleDescriptor',
  full_name='baikaldb.pb.TupleDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tuple_id', full_name='baikaldb.pb.TupleDescriptor.tuple_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='table_id', full_name='baikaldb.pb.TupleDescriptor.table_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slots', full_name='baikaldb.pb.TupleDescriptor.slots', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=341,
  serialized_end=438,
)


_EXPRVALUE = _descriptor.Descriptor(
  name='ExprValue',
  full_name='baikaldb.pb.ExprValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='baikaldb.pb.ExprValue.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bool_val', full_name='baikaldb.pb.ExprValue.bool_val', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int32_val', full_name='baikaldb.pb.ExprValue.int32_val', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uint32_val', full_name='baikaldb.pb.ExprValue.uint32_val', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int64_val', full_name='baikaldb.pb.ExprValue.int64_val', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uint64_val', full_name='baikaldb.pb.ExprValue.uint64_val', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_val', full_name='baikaldb.pb.ExprValue.float_val', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='double_val', full_name='baikaldb.pb.ExprValue.double_val', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_val', full_name='baikaldb.pb.ExprValue.string_val', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=441,
  serialized_end=649,
)

_SLOTDESCRIPTOR.fields_by_name['slot_type'].enum_type = _PRIMITIVETYPE
_TUPLEDESCRIPTOR.fields_by_name['slots'].message_type = _SLOTDESCRIPTOR
_EXPRVALUE.fields_by_name['type'].enum_type = _PRIMITIVETYPE
DESCRIPTOR.message_types_by_name['SchemaConf'] = _SCHEMACONF
DESCRIPTOR.message_types_by_name['SlotDescriptor'] = _SLOTDESCRIPTOR
DESCRIPTOR.message_types_by_name['TupleDescriptor'] = _TUPLEDESCRIPTOR
DESCRIPTOR.message_types_by_name['ExprValue'] = _EXPRVALUE
DESCRIPTOR.enum_types_by_name['ErrCode'] = _ERRCODE
DESCRIPTOR.enum_types_by_name['PrimitiveType'] = _PRIMITIVETYPE
DESCRIPTOR.enum_types_by_name['SchemaType'] = _SCHEMATYPE
DESCRIPTOR.enum_types_by_name['Engine'] = _ENGINE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SchemaConf = _reflection.GeneratedProtocolMessageType('SchemaConf', (_message.Message,), {
  'DESCRIPTOR' : _SCHEMACONF,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:baikaldb.pb.SchemaConf)
  })
_sym_db.RegisterMessage(SchemaConf)

SlotDescriptor = _reflection.GeneratedProtocolMessageType('SlotDescriptor', (_message.Message,), {
  'DESCRIPTOR' : _SLOTDESCRIPTOR,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:baikaldb.pb.SlotDescriptor)
  })
_sym_db.RegisterMessage(SlotDescriptor)

TupleDescriptor = _reflection.GeneratedProtocolMessageType('TupleDescriptor', (_message.Message,), {
  'DESCRIPTOR' : _TUPLEDESCRIPTOR,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:baikaldb.pb.TupleDescriptor)
  })
_sym_db.RegisterMessage(TupleDescriptor)

ExprValue = _reflection.GeneratedProtocolMessageType('ExprValue', (_message.Message,), {
  'DESCRIPTOR' : _EXPRVALUE,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:baikaldb.pb.ExprValue)
  })
_sym_db.RegisterMessage(ExprValue)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
