from redis.backoff import AbstractBackoff as AbstractBackoff
from redis.exceptions import ConnectionError as ConnectionError, RedisError as RedisError, TimeoutError as TimeoutError
from typing import Any, Awaitable, Callable, Tuple, Type, TypeVar

T = TypeVar('T')

class Retry:
    def __init__(self, backoff: AbstractBackoff, retries: int, supported_errors: Tuple[Type[RedisError], ...] = ...) -> None: ...
    def update_supported_errors(self, specified_errors: list): ...
    async def call_with_retry(self, do: Callable[[], Awaitable[T]], fail: Callable[[RedisError], Any]) -> T: ...
