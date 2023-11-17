from ..helpers import nativestr as nativestr
from .utils import list_to_dict as list_to_dict
from _typeshed import Incomplete

class TSInfo:
    rules: Incomplete
    labels: Incomplete
    sourceKey: Incomplete
    chunk_count: Incomplete
    memory_usage: Incomplete
    total_samples: Incomplete
    retention_msecs: Incomplete
    last_time_stamp: Incomplete
    first_time_stamp: Incomplete
    max_samples_per_chunk: Incomplete
    chunk_size: Incomplete
    duplicate_policy: Incomplete
    source_key: Incomplete
    last_timestamp: Incomplete
    first_timestamp: Incomplete
    def __init__(self, args) -> None: ...
    def get(self, item): ...
    def __getitem__(self, item): ...
