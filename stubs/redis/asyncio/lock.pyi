from _typeshed import Incomplete
from redis.asyncio import Redis as Redis, RedisCluster as RedisCluster
from redis.exceptions import LockError as LockError, LockNotOwnedError as LockNotOwnedError
from typing import Awaitable, Optional, Union

class Lock:
    lua_release: Incomplete
    lua_extend: Incomplete
    lua_reacquire: Incomplete
    LUA_RELEASE_SCRIPT: str
    LUA_EXTEND_SCRIPT: str
    LUA_REACQUIRE_SCRIPT: str
    redis: Incomplete
    name: Incomplete
    timeout: Incomplete
    sleep: Incomplete
    blocking: Incomplete
    blocking_timeout: Incomplete
    thread_local: Incomplete
    local: Incomplete
    def __init__(self, redis: Union['Redis', 'RedisCluster'], name: Union[str, bytes, memoryview], timeout: Optional[float] = ..., sleep: float = ..., blocking: bool = ..., blocking_timeout: Optional[float] = ..., thread_local: bool = ...) -> None: ...
    def register_scripts(self) -> None: ...
    async def __aenter__(self): ...
    async def __aexit__(self, exc_type, exc_value, traceback) -> None: ...
    async def acquire(self, blocking: Optional[bool] = ..., blocking_timeout: Optional[float] = ..., token: Optional[Union[str, bytes]] = ...): ...
    async def do_acquire(self, token: Union[str, bytes]) -> bool: ...
    async def locked(self) -> bool: ...
    async def owned(self) -> bool: ...
    def release(self) -> Awaitable[None]: ...
    async def do_release(self, expected_token: bytes) -> None: ...
    def extend(self, additional_time: float, replace_ttl: bool = ...) -> Awaitable[bool]: ...
    async def do_extend(self, additional_time, replace_ttl) -> bool: ...
    def reacquire(self) -> Awaitable[bool]: ...
    async def do_reacquire(self) -> bool: ...
