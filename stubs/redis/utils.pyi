from _typeshed import Incomplete
from collections.abc import Generator
from typing import Any, Dict, Mapping, Union

HIREDIS_AVAILABLE: Incomplete
HIREDIS_PACK_AVAILABLE: Incomplete
SSL_AVAILABLE: bool
CRYPTOGRAPHY_AVAILABLE: bool

def from_url(url, **kwargs): ...
def pipeline(redis_obj) -> Generator[Incomplete, None, None]: ...
def str_if_bytes(value: Union[str, bytes]) -> str: ...
def safe_str(value): ...
def dict_merge(*dicts: Mapping[str, Any]) -> Dict[str, Any]: ...
def list_keys_to_dict(key_list, callback): ...
def merge_result(command, res): ...
def warn_deprecated(name, reason: str = ..., version: str = ..., stacklevel: int = ...) -> None: ...
def deprecated_function(reason: str = ..., version: str = ..., name: Incomplete | None = ...): ...
def get_lib_version(): ...
