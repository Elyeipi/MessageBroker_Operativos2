# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: broker.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x62roker.proto\"\x1e\n\x0bmensaje_req\x12\x0f\n\x07topicID\x18\x01 \x01(\t\".\n\x0bmensaje_res\x12\x0f\n\x07mensaje\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\"!\n\x0f\x63rear_topic_req\x12\x0e\n\x06nombre\x18\x01 \x01(\t\"\x81\x01\n\x0f\x63rear_topic_res\x12\x13\n\x06nombre\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07topicId\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x12\n\x05razon\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x0e\n\x06\x63reado\x18\x04 \x01(\x08\x42\t\n\x07_nombreB\n\n\x08_topicIdB\x08\n\x06_razon\"8\n\x14publicar_mensaje_req\x12\x0f\n\x07mensaje\x18\x01 \x01(\t\x12\x0f\n\x07topicId\x18\x02 \x01(\t\")\n\x14publicar_mensaje_res\x12\x11\n\tpublicado\x18\x01 \x01(\x08\"\"\n\x0fsuscribirse_req\x12\x0f\n\x07topicId\x18\x01 \x01(\t\"I\n\x0fsuscribirse_res\x12\x0f\n\x07topicId\x18\x01 \x01(\t\x12\x13\n\x0bnombreTopic\x18\x02 \x01(\t\x12\x10\n\x08suscrito\x18\x03 \x01(\x08\"\x13\n\x11listar_topics_req\"_\n\x11listar_topics_res\x12\x0f\n\x07topicId\x18\x01 \x01(\t\x12\x13\n\x0bnombreTopic\x18\x02 \x01(\t\x12\x16\n\tsuscritos\x18\x03 \x01(\x05H\x00\x88\x01\x01\x42\x0c\n\n_suscritos\"\x13\n\x04ping\x12\x0b\n\x03msg\x18\x01 \x01(\t2\xc2\x02\n\x06\x42roker\x12\x33\n\x0b\x43rear_topic\x12\x10.crear_topic_req\x1a\x10.crear_topic_res\"\x00\x12/\n\rRecibir_topic\x12\x0c.mensaje_req\x1a\x0c.mensaje_res\"\x00\x30\x01\x12\x42\n\x10Publicar_mensaje\x12\x15.publicar_mensaje_req\x1a\x15.publicar_mensaje_res\"\x00\x12\x39\n\x11Suscribirse_topic\x12\x10.suscribirse_req\x1a\x10.suscribirse_res\"\x00\x12;\n\rListar_topics\x12\x12.listar_topics_req\x1a\x12.listar_topics_res\"\x00\x30\x01\x12\x16\n\x04Ping\x12\x05.ping\x1a\x05.ping\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'broker_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MENSAJE_REQ']._serialized_start=16
  _globals['_MENSAJE_REQ']._serialized_end=46
  _globals['_MENSAJE_RES']._serialized_start=48
  _globals['_MENSAJE_RES']._serialized_end=94
  _globals['_CREAR_TOPIC_REQ']._serialized_start=96
  _globals['_CREAR_TOPIC_REQ']._serialized_end=129
  _globals['_CREAR_TOPIC_RES']._serialized_start=132
  _globals['_CREAR_TOPIC_RES']._serialized_end=261
  _globals['_PUBLICAR_MENSAJE_REQ']._serialized_start=263
  _globals['_PUBLICAR_MENSAJE_REQ']._serialized_end=319
  _globals['_PUBLICAR_MENSAJE_RES']._serialized_start=321
  _globals['_PUBLICAR_MENSAJE_RES']._serialized_end=362
  _globals['_SUSCRIBIRSE_REQ']._serialized_start=364
  _globals['_SUSCRIBIRSE_REQ']._serialized_end=398
  _globals['_SUSCRIBIRSE_RES']._serialized_start=400
  _globals['_SUSCRIBIRSE_RES']._serialized_end=473
  _globals['_LISTAR_TOPICS_REQ']._serialized_start=475
  _globals['_LISTAR_TOPICS_REQ']._serialized_end=494
  _globals['_LISTAR_TOPICS_RES']._serialized_start=496
  _globals['_LISTAR_TOPICS_RES']._serialized_end=591
  _globals['_PING']._serialized_start=593
  _globals['_PING']._serialized_end=612
  _globals['_BROKER']._serialized_start=615
  _globals['_BROKER']._serialized_end=937
# @@protoc_insertion_point(module_scope)
