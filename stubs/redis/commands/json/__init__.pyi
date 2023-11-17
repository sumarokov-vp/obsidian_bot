import abc
import redis
from ..helpers import get_protocol_version as get_protocol_version, nativestr as nativestr
from .commands import JSONCommands as JSONCommands
from .decoders import bulk_of_jsons as bulk_of_jsons, decode_list as decode_list
from _typeshed import Incomplete

class JSON(JSONCommands):
    client: Incomplete
    execute_command: Incomplete
    MODULE_VERSION: Incomplete
    __encoder__: Incomplete
    __decoder__: Incomplete
    def __init__(self, client, version: Incomplete | None = ..., decoder=..., encoder=...) -> None: ...
    def pipeline(self, transaction: bool = ..., shard_hint: Incomplete | None = ...): ...

class ClusterPipeline(JSONCommands, redis.cluster.ClusterPipeline, metaclass=abc.ABCMeta): ...
class Pipeline(JSONCommands, redis.client.Pipeline): ...
