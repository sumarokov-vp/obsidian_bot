from _typeshed import Incomplete
from datetime import datetime, timedelta
from redis._parsers import Encoder as Encoder
from redis.asyncio.connection import ConnectionPool as AsyncConnectionPool
from redis.compat import Protocol as Protocol
from redis.connection import ConnectionPool as ConnectionPool
from typing import Any, Awaitable, Iterable, Mapping, Type, TypeVar, Union

Number = Union[int, float]
EncodedT = Union[bytes, memoryview]
DecodedT = Union[str, int, float]
EncodableT = Union[EncodedT, DecodedT]
AbsExpiryT = Union[int, datetime]
ExpiryT = Union[int, timedelta]
ZScoreBoundT = Union[float, str]
BitfieldOffsetT = Union[int, str]
KeyT: Incomplete
PatternT: Incomplete
FieldT = EncodableT
KeysT = Union[KeyT, Iterable[KeyT]]
ChannelT: Incomplete
GroupT: Incomplete
ConsumerT: Incomplete
StreamIdT: Incomplete
ScriptTextT: Incomplete
TimeoutSecT: Incomplete
AnyKeyT = TypeVar('AnyKeyT', bytes, str, memoryview)
AnyFieldT = TypeVar('AnyFieldT', bytes, str, memoryview)
AnyChannelT = TypeVar('AnyChannelT', bytes, str, memoryview)
ExceptionMappingT = Mapping[str, Union[Type[Exception], Mapping[str, Type[Exception]]]]

class CommandsProtocol(Protocol):
    connection_pool: Union['AsyncConnectionPool', 'ConnectionPool']
    def execute_command(self, *args, **options): ...

class ClusterCommandsProtocol(CommandsProtocol, Protocol):
    encoder: Encoder
    def execute_command(self, *args, **options) -> Union[Any, Awaitable]: ...
