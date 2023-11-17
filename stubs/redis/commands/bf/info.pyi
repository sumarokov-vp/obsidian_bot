from ..helpers import nativestr as nativestr
from _typeshed import Incomplete

class BFInfo:
    capacity: Incomplete
    size: Incomplete
    filterNum: Incomplete
    insertedNum: Incomplete
    expansionRate: Incomplete
    def __init__(self, args) -> None: ...
    def get(self, item): ...
    def __getitem__(self, item): ...

class CFInfo:
    size: Incomplete
    bucketNum: Incomplete
    filterNum: Incomplete
    insertedNum: Incomplete
    deletedNum: Incomplete
    bucketSize: Incomplete
    expansionRate: Incomplete
    maxIteration: Incomplete
    def __init__(self, args) -> None: ...
    def get(self, item): ...
    def __getitem__(self, item): ...

class CMSInfo:
    width: Incomplete
    depth: Incomplete
    count: Incomplete
    def __init__(self, args) -> None: ...
    def __getitem__(self, item): ...

class TopKInfo:
    k: Incomplete
    width: Incomplete
    depth: Incomplete
    decay: Incomplete
    def __init__(self, args) -> None: ...
    def __getitem__(self, item): ...

class TDigestInfo:
    compression: Incomplete
    capacity: Incomplete
    merged_nodes: Incomplete
    unmerged_nodes: Incomplete
    merged_weight: Incomplete
    unmerged_weight: Incomplete
    total_compressions: Incomplete
    memory_usage: Incomplete
    def __init__(self, args) -> None: ...
    def get(self, item): ...
    def __getitem__(self, item): ...
