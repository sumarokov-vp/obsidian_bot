import abc
import asyncio
import enum
import ssl
from .._parsers import BaseParser as BaseParser, Encoder as Encoder, _AsyncHiredisParser, _AsyncRESP2Parser, _AsyncRESP3Parser
from _typeshed import Incomplete
from abc import abstractmethod
from redis.asyncio.retry import Retry as Retry
from redis.backoff import NoBackoff as NoBackoff
from redis.compat import Protocol as Protocol, TypedDict as TypedDict
from redis.connection import DEFAULT_RESP_VERSION as DEFAULT_RESP_VERSION
from redis.credentials import CredentialProvider as CredentialProvider, UsernamePasswordCredentialProvider as UsernamePasswordCredentialProvider
from redis.exceptions import AuthenticationError as AuthenticationError, AuthenticationWrongNumberOfArgsError as AuthenticationWrongNumberOfArgsError, ConnectionError as ConnectionError, DataError as DataError, RedisError as RedisError, ResponseError as ResponseError, TimeoutError as TimeoutError
from redis.typing import EncodableT as EncodableT
from redis.utils import HIREDIS_AVAILABLE as HIREDIS_AVAILABLE, get_lib_version as get_lib_version, str_if_bytes as str_if_bytes
from typing import Any, Callable, Iterable, List, Mapping, Optional, Tuple, Type, Union
from urllib.parse import ParseResult as ParseResult

SYM_STAR: bytes
SYM_DOLLAR: bytes
SYM_CRLF: bytes
SYM_LF: bytes
SYM_EMPTY: bytes

class _Sentinel(enum.Enum):
    sentinel: Incomplete

SENTINEL: Incomplete
DefaultParser: Type[Union[_AsyncRESP2Parser, _AsyncRESP3Parser, _AsyncHiredisParser]]

class ConnectCallbackProtocol(Protocol):
    def __call__(self, connection: AbstractConnection): ...

class AsyncConnectCallbackProtocol(Protocol):
    async def __call__(self, connection: AbstractConnection): ...
ConnectCallbackT = Union[ConnectCallbackProtocol, AsyncConnectCallbackProtocol]

class AbstractConnection(metaclass=abc.ABCMeta):
    db: Incomplete
    client_name: Incomplete
    lib_name: Incomplete
    lib_version: Incomplete
    credential_provider: Incomplete
    password: Incomplete
    username: Incomplete
    socket_timeout: Incomplete
    socket_connect_timeout: Incomplete
    retry_on_timeout: Incomplete
    retry_on_error: Incomplete
    retry: Incomplete
    health_check_interval: Incomplete
    next_health_check: int
    encoder: Incomplete
    redis_connect_func: Incomplete
    protocol: Incomplete
    def __init__(self, *, db: Union[str, int] = ..., password: Optional[str] = ..., socket_timeout: Optional[float] = ..., socket_connect_timeout: Optional[float] = ..., retry_on_timeout: bool = ..., retry_on_error: Union[list, _Sentinel] = ..., encoding: str = ..., encoding_errors: str = ..., decode_responses: bool = ..., parser_class: Type[BaseParser] = ..., socket_read_size: int = ..., health_check_interval: float = ..., client_name: Optional[str] = ..., lib_name: Optional[str] = ..., lib_version: Optional[str] = ..., username: Optional[str] = ..., retry: Optional[Retry] = ..., redis_connect_func: Optional[ConnectCallbackT] = ..., encoder_class: Type[Encoder] = ..., credential_provider: Optional[CredentialProvider] = ..., protocol: Optional[int] = ...) -> None: ...
    @abstractmethod
    def repr_pieces(self): ...
    @property
    def is_connected(self): ...
    def set_parser(self, parser_class: Type[BaseParser]) -> None: ...
    async def connect(self): ...
    async def on_connect(self) -> None: ...
    async def disconnect(self, nowait: bool = ...) -> None: ...
    async def check_health(self) -> None: ...
    async def send_packed_command(self, command: Union[bytes, str, Iterable[bytes]], check_health: bool = ...) -> None: ...
    async def send_command(self, *args: Any, **kwargs: Any) -> None: ...
    async def can_read_destructive(self): ...
    async def read_response(self, disable_decoding: bool = ..., timeout: Optional[float] = ..., *, disconnect_on_error: bool = ..., push_request: Optional[bool] = ...): ...
    def pack_command(self, *args: EncodableT) -> List[bytes]: ...
    def pack_commands(self, commands: Iterable[Iterable[EncodableT]]) -> List[bytes]: ...

class Connection(AbstractConnection):
    host: Incomplete
    port: Incomplete
    socket_keepalive: Incomplete
    socket_keepalive_options: Incomplete
    socket_type: Incomplete
    def __init__(self, *, host: str = ..., port: Union[str, int] = ..., socket_keepalive: bool = ..., socket_keepalive_options: Optional[Mapping[int, Union[int, bytes]]] = ..., socket_type: int = ..., **kwargs) -> None: ...
    def repr_pieces(self): ...

class SSLConnection(Connection):
    ssl_context: Incomplete
    def __init__(self, ssl_keyfile: Optional[str] = ..., ssl_certfile: Optional[str] = ..., ssl_cert_reqs: str = ..., ssl_ca_certs: Optional[str] = ..., ssl_ca_data: Optional[str] = ..., ssl_check_hostname: bool = ..., **kwargs) -> None: ...
    @property
    def keyfile(self): ...
    @property
    def certfile(self): ...
    @property
    def cert_reqs(self): ...
    @property
    def ca_certs(self): ...
    @property
    def ca_data(self): ...
    @property
    def check_hostname(self): ...

class RedisSSLContext:
    keyfile: Incomplete
    certfile: Incomplete
    cert_reqs: Incomplete
    ca_certs: Incomplete
    ca_data: Incomplete
    check_hostname: Incomplete
    context: Incomplete
    def __init__(self, keyfile: Optional[str] = ..., certfile: Optional[str] = ..., cert_reqs: Optional[str] = ..., ca_certs: Optional[str] = ..., ca_data: Optional[str] = ..., check_hostname: bool = ...) -> None: ...
    def get(self) -> ssl.SSLContext: ...

class UnixDomainSocketConnection(AbstractConnection):
    path: Incomplete
    def __init__(self, *, path: str = ..., **kwargs) -> None: ...
    def repr_pieces(self) -> Iterable[Tuple[str, Union[str, int]]]: ...

FALSE_STRINGS: Incomplete

def to_bool(value) -> Optional[bool]: ...

URL_QUERY_ARGUMENT_PARSERS: Mapping[str, Callable[..., object]]

class ConnectKwargs(TypedDict, total=False):
    username: str
    password: str
    connection_class: Type[AbstractConnection]
    host: str
    port: int
    db: int
    path: str

def parse_url(url: str) -> ConnectKwargs: ...

class ConnectionPool:
    @classmethod
    def from_url(cls, url: str, **kwargs) -> _CP: ...
    connection_class: Incomplete
    connection_kwargs: Incomplete
    max_connections: Incomplete
    encoder_class: Incomplete
    def __init__(self, connection_class: Type[AbstractConnection] = ..., max_connections: Optional[int] = ..., **connection_kwargs) -> None: ...
    def reset(self) -> None: ...
    def can_get_connection(self) -> bool: ...
    async def get_connection(self, command_name, *keys, **options): ...
    def get_encoder(self): ...
    def make_connection(self): ...
    async def ensure_connection(self, connection: AbstractConnection): ...
    async def release(self, connection: AbstractConnection): ...
    async def disconnect(self, inuse_connections: bool = ...): ...
    async def aclose(self) -> None: ...
    def set_retry(self, retry: Retry) -> None: ...

class BlockingConnectionPool(ConnectionPool):
    timeout: Incomplete
    def __init__(self, max_connections: int = ..., timeout: Optional[int] = ..., connection_class: Type[AbstractConnection] = ..., queue_class: Type[asyncio.Queue] = ..., **connection_kwargs) -> None: ...
    async def get_connection(self, command_name, *keys, **options): ...
    async def release(self, connection: AbstractConnection): ...
