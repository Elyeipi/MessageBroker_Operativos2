from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class mensaje_req(_message.Message):
    __slots__ = ("topicID",)
    TOPICID_FIELD_NUMBER: _ClassVar[int]
    topicID: str
    def __init__(self, topicID: _Optional[str] = ...) -> None: ...

class mensaje_res(_message.Message):
    __slots__ = ("mensaje", "status")
    MENSAJE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    mensaje: str
    status: str
    def __init__(self, mensaje: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class crear_topic_req(_message.Message):
    __slots__ = ("nombre",)
    NOMBRE_FIELD_NUMBER: _ClassVar[int]
    nombre: str
    def __init__(self, nombre: _Optional[str] = ...) -> None: ...

class crear_topic_res(_message.Message):
    __slots__ = ("nombre", "topicId", "razon", "creado")
    NOMBRE_FIELD_NUMBER: _ClassVar[int]
    TOPICID_FIELD_NUMBER: _ClassVar[int]
    RAZON_FIELD_NUMBER: _ClassVar[int]
    CREADO_FIELD_NUMBER: _ClassVar[int]
    nombre: str
    topicId: str
    razon: str
    creado: bool
    def __init__(self, nombre: _Optional[str] = ..., topicId: _Optional[str] = ..., razon: _Optional[str] = ..., creado: bool = ...) -> None: ...

class publicar_mensaje_req(_message.Message):
    __slots__ = ("mensaje", "topicId")
    MENSAJE_FIELD_NUMBER: _ClassVar[int]
    TOPICID_FIELD_NUMBER: _ClassVar[int]
    mensaje: str
    topicId: str
    def __init__(self, mensaje: _Optional[str] = ..., topicId: _Optional[str] = ...) -> None: ...

class publicar_mensaje_res(_message.Message):
    __slots__ = ("publicado",)
    PUBLICADO_FIELD_NUMBER: _ClassVar[int]
    publicado: bool
    def __init__(self, publicado: bool = ...) -> None: ...

class suscribirse_req(_message.Message):
    __slots__ = ("topicId",)
    TOPICID_FIELD_NUMBER: _ClassVar[int]
    topicId: str
    def __init__(self, topicId: _Optional[str] = ...) -> None: ...

class suscribirse_res(_message.Message):
    __slots__ = ("topicId", "nombreTopic", "suscrito")
    TOPICID_FIELD_NUMBER: _ClassVar[int]
    NOMBRETOPIC_FIELD_NUMBER: _ClassVar[int]
    SUSCRITO_FIELD_NUMBER: _ClassVar[int]
    topicId: str
    nombreTopic: str
    suscrito: bool
    def __init__(self, topicId: _Optional[str] = ..., nombreTopic: _Optional[str] = ..., suscrito: bool = ...) -> None: ...

class listar_topics_req(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class listar_topics_res(_message.Message):
    __slots__ = ("topicId", "nombreTopic", "suscritos")
    TOPICID_FIELD_NUMBER: _ClassVar[int]
    NOMBRETOPIC_FIELD_NUMBER: _ClassVar[int]
    SUSCRITOS_FIELD_NUMBER: _ClassVar[int]
    topicId: str
    nombreTopic: str
    suscritos: int
    def __init__(self, topicId: _Optional[str] = ..., nombreTopic: _Optional[str] = ..., suscritos: _Optional[int] = ...) -> None: ...

class ping(_message.Message):
    __slots__ = ("msg",)
    MSG_FIELD_NUMBER: _ClassVar[int]
    msg: str
    def __init__(self, msg: _Optional[str] = ...) -> None: ...
