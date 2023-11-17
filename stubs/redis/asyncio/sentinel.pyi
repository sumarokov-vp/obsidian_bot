from _typeshed import Incomplete
from redis.asyncio.client import Redis as Redis
from redis.asyncio.connection import Connection as Connection, ConnectionPool as ConnectionPool, EncodableT as EncodableT, SSLConnection as SSLConnection
from redis.commands import AsyncSentinelCommands as AsyncSentinelCommands
from redis.exceptions import ConnectionError as ConnectionError, ReadOnlyError as ReadOnlyError, ResponseError as ResponseError, TimeoutError as TimeoutError
from redis.utils import str_if_bytes as str_if_bytes
from typing import AsyncIterator, Iterable, Mapping, Optional, Sequence, Tuple, Type

class MasterNotFoundError(ConnectionError): ...
class SlaveNotFoundError(ConnectionError): ...

class SentinelManagedConnection(Connection):
    connection_pool: Incomplete
    def __init__(self, **kwargs) -> None: ...
    async def connect_to(self, address) -> None: ...
    async def connect(self): ...
    async def read_response(self, disable_decoding: bool = ..., timeout: Optional[float] = ..., *, disconnect_on_error: Optional[float] = ..., push_request: Optional[bool] = ...): ...

class SentinelManagedSSLConnection(SentinelManagedConnection, SSLConnection): ...

class SentinelConnectionPool(ConnectionPool):
    is_master: Incomplete
    check_connection: Incomplete
    service_name: Incomplete
    sentinel_manager: Incomplete
    master_address: Incomplete
    slave_rr_counter: Incomplete
    def __init__(self, service_name, sentinel_manager, **kwargs) -> None: ...
    def reset(self) -> None: ...
    def owns_connection(self, connection: Connection): ...
    async def get_master_address(self): ...
    async def rotate_slaves(self) -> AsyncIterator: ...

class Sentinel(AsyncSentinelCommands):
    sentinel_kwargs: Incomplete
    sentinels: Incomplete
    min_other_sentinels: Incomplete
    connection_kwargs: Incomplete
    def __init__(self, sentinels, min_other_sentinels: int = ..., sentinel_kwargs: Incomplete | None = ..., **connection_kwargs) -> None: ...
    async def execute_command(self, *args, **kwargs): ...
    def check_master_state(self, state: dict, service_name: str) -> bool: ...
    async def discover_master(self, service_name: str): ...
    def filter_slaves(self, slaves: Iterable[Mapping]) -> Sequence[Tuple[EncodableT, EncodableT]]: ...
    async def discover_slaves(self, service_name: str) -> Sequence[Tuple[EncodableT, EncodableT]]: ...
    def master_for(self, service_name: str, redis_class: Type[Redis] = ..., connection_pool_class: Type[SentinelConnectionPool] = ..., **kwargs): ...
    def slave_for(self, service_name: str, redis_class: Type[Redis] = ..., connection_pool_class: Type[SentinelConnectionPool] = ..., **kwargs): ...