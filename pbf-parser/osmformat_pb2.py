# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='osmformat.proto',
  package='OSMPBF',
  serialized_pb='\n\x0fosmformat.proto\x12\x06OSMPBF\"\x8d\x01\n\x0bHeaderBlock\x12 \n\x04\x62\x62ox\x18\x01 \x01(\x0b\x32\x12.OSMPBF.HeaderBBox\x12\x19\n\x11required_features\x18\x04 \x03(\t\x12\x19\n\x11optional_features\x18\x05 \x03(\t\x12\x16\n\x0ewritingprogram\x18\x10 \x01(\t\x12\x0e\n\x06source\x18\x11 \x01(\t\"F\n\nHeaderBBox\x12\x0c\n\x04left\x18\x01 \x02(\x12\x12\r\n\x05right\x18\x02 \x02(\x12\x12\x0b\n\x03top\x18\x03 \x02(\x12\x12\x0e\n\x06\x62ottom\x18\x04 \x02(\x12\"\xd2\x01\n\x0ePrimitiveBlock\x12(\n\x0bstringtable\x18\x01 \x02(\x0b\x32\x13.OSMPBF.StringTable\x12.\n\x0eprimitivegroup\x18\x02 \x03(\x0b\x32\x16.OSMPBF.PrimitiveGroup\x12\x18\n\x0bgranularity\x18\x11 \x01(\x05:\x03\x31\x30\x30\x12\x15\n\nlat_offset\x18\x13 \x01(\x03:\x01\x30\x12\x15\n\nlon_offset\x18\x14 \x01(\x03:\x01\x30\x12\x1e\n\x10\x64\x61te_granularity\x18\x12 \x01(\x05:\x04\x31\x30\x30\x30\"\xb7\x01\n\x0ePrimitiveGroup\x12\x1b\n\x05nodes\x18\x01 \x03(\x0b\x32\x0c.OSMPBF.Node\x12!\n\x05\x64\x65nse\x18\x02 \x01(\x0b\x32\x12.OSMPBF.DenseNodes\x12\x19\n\x04ways\x18\x03 \x03(\x0b\x32\x0b.OSMPBF.Way\x12#\n\trelations\x18\x04 \x03(\x0b\x32\x10.OSMPBF.Relation\x12%\n\nchangesets\x18\x05 \x03(\x0b\x32\x11.OSMPBF.ChangeSet\"\x18\n\x0bStringTable\x12\t\n\x01s\x18\x01 \x03(\x0c\"`\n\x04Info\x12\x13\n\x07version\x18\x01 \x01(\x05:\x02-1\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12\x11\n\tchangeset\x18\x03 \x01(\x03\x12\x0b\n\x03uid\x18\x04 \x01(\x05\x12\x10\n\x08user_sid\x18\x05 \x01(\r\"u\n\tDenseInfo\x12\x13\n\x07version\x18\x01 \x03(\x05\x42\x02\x10\x01\x12\x15\n\ttimestamp\x18\x02 \x03(\x12\x42\x02\x10\x01\x12\x15\n\tchangeset\x18\x03 \x03(\x12\x42\x02\x10\x01\x12\x0f\n\x03uid\x18\x04 \x03(\x11\x42\x02\x10\x01\x12\x14\n\x08user_sid\x18\x05 \x03(\x11\x42\x02\x10\x01\"\x17\n\tChangeSet\x12\n\n\x02id\x18\x01 \x02(\x03\"l\n\x04Node\x12\n\n\x02id\x18\x01 \x02(\x12\x12\x10\n\x04keys\x18\x02 \x03(\rB\x02\x10\x01\x12\x10\n\x04vals\x18\x03 \x03(\rB\x02\x10\x01\x12\x1a\n\x04info\x18\x04 \x01(\x0b\x32\x0c.OSMPBF.Info\x12\x0b\n\x03lat\x18\x08 \x02(\x12\x12\x0b\n\x03lon\x18\t \x02(\x12\"{\n\nDenseNodes\x12\x0e\n\x02id\x18\x01 \x03(\x12\x42\x02\x10\x01\x12$\n\tdenseinfo\x18\x05 \x01(\x0b\x32\x11.OSMPBF.DenseInfo\x12\x0f\n\x03lat\x18\x08 \x03(\x12\x42\x02\x10\x01\x12\x0f\n\x03lon\x18\t \x03(\x12\x42\x02\x10\x01\x12\x15\n\tkeys_vals\x18\n \x03(\x05\x42\x02\x10\x01\"c\n\x03Way\x12\n\n\x02id\x18\x01 \x02(\x03\x12\x10\n\x04keys\x18\x02 \x03(\rB\x02\x10\x01\x12\x10\n\x04vals\x18\x03 \x03(\rB\x02\x10\x01\x12\x1a\n\x04info\x18\x04 \x01(\x0b\x32\x0c.OSMPBF.Info\x12\x10\n\x04refs\x18\x08 \x03(\x12\x42\x02\x10\x01\"\xe0\x01\n\x08Relation\x12\n\n\x02id\x18\x01 \x02(\x03\x12\x10\n\x04keys\x18\x02 \x03(\rB\x02\x10\x01\x12\x10\n\x04vals\x18\x03 \x03(\rB\x02\x10\x01\x12\x1a\n\x04info\x18\x04 \x01(\x0b\x32\x0c.OSMPBF.Info\x12\x15\n\troles_sid\x18\x08 \x03(\x05\x42\x02\x10\x01\x12\x12\n\x06memids\x18\t \x03(\x12\x42\x02\x10\x01\x12.\n\x05types\x18\n \x03(\x0e\x32\x1b.OSMPBF.Relation.MemberTypeB\x02\x10\x01\"-\n\nMemberType\x12\x08\n\x04NODE\x10\x00\x12\x07\n\x03WAY\x10\x01\x12\x0c\n\x08RELATION\x10\x02\x42\x0f\n\rcrosby.binary')



_RELATION_MEMBERTYPE = descriptor.EnumDescriptor(
  name='MemberType',
  full_name='OSMPBF.Relation.MemberType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='NODE', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='WAY', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='RELATION', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1426,
  serialized_end=1471,
)


_HEADERBLOCK = descriptor.Descriptor(
  name='HeaderBlock',
  full_name='OSMPBF.HeaderBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='bbox', full_name='OSMPBF.HeaderBlock.bbox', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='required_features', full_name='OSMPBF.HeaderBlock.required_features', index=1,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='optional_features', full_name='OSMPBF.HeaderBlock.optional_features', index=2,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='writingprogram', full_name='OSMPBF.HeaderBlock.writingprogram', index=3,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='source', full_name='OSMPBF.HeaderBlock.source', index=4,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=28,
  serialized_end=169,
)


_HEADERBBOX = descriptor.Descriptor(
  name='HeaderBBox',
  full_name='OSMPBF.HeaderBBox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='left', full_name='OSMPBF.HeaderBBox.left', index=0,
      number=1, type=18, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='right', full_name='OSMPBF.HeaderBBox.right', index=1,
      number=2, type=18, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='top', full_name='OSMPBF.HeaderBBox.top', index=2,
      number=3, type=18, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bottom', full_name='OSMPBF.HeaderBBox.bottom', index=3,
      number=4, type=18, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=171,
  serialized_end=241,
)


_PRIMITIVEBLOCK = descriptor.Descriptor(
  name='PrimitiveBlock',
  full_name='OSMPBF.PrimitiveBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='stringtable', full_name='OSMPBF.PrimitiveBlock.stringtable', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='primitivegroup', full_name='OSMPBF.PrimitiveBlock.primitivegroup', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='granularity', full_name='OSMPBF.PrimitiveBlock.granularity', index=2,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=100,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='lat_offset', full_name='OSMPBF.PrimitiveBlock.lat_offset', index=3,
      number=19, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='lon_offset', full_name='OSMPBF.PrimitiveBlock.lon_offset', index=4,
      number=20, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='date_granularity', full_name='OSMPBF.PrimitiveBlock.date_granularity', index=5,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=244,
  serialized_end=454,
)


_PRIMITIVEGROUP = descriptor.Descriptor(
  name='PrimitiveGroup',
  full_name='OSMPBF.PrimitiveGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='nodes', full_name='OSMPBF.PrimitiveGroup.nodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dense', full_name='OSMPBF.PrimitiveGroup.dense', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ways', full_name='OSMPBF.PrimitiveGroup.ways', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='relations', full_name='OSMPBF.PrimitiveGroup.relations', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='changesets', full_name='OSMPBF.PrimitiveGroup.changesets', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=457,
  serialized_end=640,
)


_STRINGTABLE = descriptor.Descriptor(
  name='StringTable',
  full_name='OSMPBF.StringTable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='s', full_name='OSMPBF.StringTable.s', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=642,
  serialized_end=666,
)


_INFO = descriptor.Descriptor(
  name='Info',
  full_name='OSMPBF.Info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='version', full_name='OSMPBF.Info.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timestamp', full_name='OSMPBF.Info.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='changeset', full_name='OSMPBF.Info.changeset', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='uid', full_name='OSMPBF.Info.uid', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_sid', full_name='OSMPBF.Info.user_sid', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=668,
  serialized_end=764,
)


_DENSEINFO = descriptor.Descriptor(
  name='DenseInfo',
  full_name='OSMPBF.DenseInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='version', full_name='OSMPBF.DenseInfo.version', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='timestamp', full_name='OSMPBF.DenseInfo.timestamp', index=1,
      number=2, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='changeset', full_name='OSMPBF.DenseInfo.changeset', index=2,
      number=3, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='uid', full_name='OSMPBF.DenseInfo.uid', index=3,
      number=4, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='user_sid', full_name='OSMPBF.DenseInfo.user_sid', index=4,
      number=5, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=766,
  serialized_end=883,
)


_CHANGESET = descriptor.Descriptor(
  name='ChangeSet',
  full_name='OSMPBF.ChangeSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='OSMPBF.ChangeSet.id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=885,
  serialized_end=908,
)


_NODE = descriptor.Descriptor(
  name='Node',
  full_name='OSMPBF.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='OSMPBF.Node.id', index=0,
      number=1, type=18, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='keys', full_name='OSMPBF.Node.keys', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='vals', full_name='OSMPBF.Node.vals', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='info', full_name='OSMPBF.Node.info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='lat', full_name='OSMPBF.Node.lat', index=4,
      number=8, type=18, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='lon', full_name='OSMPBF.Node.lon', index=5,
      number=9, type=18, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=910,
  serialized_end=1018,
)


_DENSENODES = descriptor.Descriptor(
  name='DenseNodes',
  full_name='OSMPBF.DenseNodes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='OSMPBF.DenseNodes.id', index=0,
      number=1, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='denseinfo', full_name='OSMPBF.DenseNodes.denseinfo', index=1,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='lat', full_name='OSMPBF.DenseNodes.lat', index=2,
      number=8, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='lon', full_name='OSMPBF.DenseNodes.lon', index=3,
      number=9, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='keys_vals', full_name='OSMPBF.DenseNodes.keys_vals', index=4,
      number=10, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1020,
  serialized_end=1143,
)


_WAY = descriptor.Descriptor(
  name='Way',
  full_name='OSMPBF.Way',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='OSMPBF.Way.id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='keys', full_name='OSMPBF.Way.keys', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='vals', full_name='OSMPBF.Way.vals', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='info', full_name='OSMPBF.Way.info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='refs', full_name='OSMPBF.Way.refs', index=4,
      number=8, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1145,
  serialized_end=1244,
)


_RELATION = descriptor.Descriptor(
  name='Relation',
  full_name='OSMPBF.Relation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='OSMPBF.Relation.id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='keys', full_name='OSMPBF.Relation.keys', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='vals', full_name='OSMPBF.Relation.vals', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='info', full_name='OSMPBF.Relation.info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='roles_sid', full_name='OSMPBF.Relation.roles_sid', index=4,
      number=8, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='memids', full_name='OSMPBF.Relation.memids', index=5,
      number=9, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='types', full_name='OSMPBF.Relation.types', index=6,
      number=10, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RELATION_MEMBERTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1247,
  serialized_end=1471,
)


_HEADERBLOCK.fields_by_name['bbox'].message_type = _HEADERBBOX
_PRIMITIVEBLOCK.fields_by_name['stringtable'].message_type = _STRINGTABLE
_PRIMITIVEBLOCK.fields_by_name['primitivegroup'].message_type = _PRIMITIVEGROUP
_PRIMITIVEGROUP.fields_by_name['nodes'].message_type = _NODE
_PRIMITIVEGROUP.fields_by_name['dense'].message_type = _DENSENODES
_PRIMITIVEGROUP.fields_by_name['ways'].message_type = _WAY
_PRIMITIVEGROUP.fields_by_name['relations'].message_type = _RELATION
_PRIMITIVEGROUP.fields_by_name['changesets'].message_type = _CHANGESET
_NODE.fields_by_name['info'].message_type = _INFO
_DENSENODES.fields_by_name['denseinfo'].message_type = _DENSEINFO
_WAY.fields_by_name['info'].message_type = _INFO
_RELATION.fields_by_name['info'].message_type = _INFO
_RELATION.fields_by_name['types'].enum_type = _RELATION_MEMBERTYPE
_RELATION_MEMBERTYPE.containing_type = _RELATION;

class HeaderBlock(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEADERBLOCK
  
  # @@protoc_insertion_point(class_scope:OSMPBF.HeaderBlock)

class HeaderBBox(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEADERBBOX
  
  # @@protoc_insertion_point(class_scope:OSMPBF.HeaderBBox)

class PrimitiveBlock(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PRIMITIVEBLOCK
  
  # @@protoc_insertion_point(class_scope:OSMPBF.PrimitiveBlock)

class PrimitiveGroup(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PRIMITIVEGROUP
  
  # @@protoc_insertion_point(class_scope:OSMPBF.PrimitiveGroup)

class StringTable(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STRINGTABLE
  
  # @@protoc_insertion_point(class_scope:OSMPBF.StringTable)

class Info(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INFO
  
  # @@protoc_insertion_point(class_scope:OSMPBF.Info)

class DenseInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DENSEINFO
  
  # @@protoc_insertion_point(class_scope:OSMPBF.DenseInfo)

class ChangeSet(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHANGESET
  
  # @@protoc_insertion_point(class_scope:OSMPBF.ChangeSet)

class Node(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NODE
  
  # @@protoc_insertion_point(class_scope:OSMPBF.Node)

class DenseNodes(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DENSENODES
  
  # @@protoc_insertion_point(class_scope:OSMPBF.DenseNodes)

class Way(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WAY
  
  # @@protoc_insertion_point(class_scope:OSMPBF.Way)

class Relation(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RELATION
  
  # @@protoc_insertion_point(class_scope:OSMPBF.Relation)

# @@protoc_insertion_point(module_scope)
