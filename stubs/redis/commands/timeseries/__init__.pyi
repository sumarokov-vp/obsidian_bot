import abc
import redis
from ..helpers import get_protocol_version as get_protocol_version, parse_to_list as parse_to_list
from .commands import ALTER_CMD as ALTER_CMD, CREATERULE_CMD as CREATERULE_CMD, CREATE_CMD as CREATE_CMD, DELETERULE_CMD as DELETERULE_CMD, DEL_CMD as DEL_CMD, GET_CMD as GET_CMD, INFO_CMD as INFO_CMD, MGET_CMD as MGET_CMD, MRANGE_CMD as MRANGE_CMD, MREVRANGE_CMD as MREVRANGE_CMD, QUERYINDEX_CMD as QUERYINDEX_CMD, RANGE_CMD as RANGE_CMD, REVRANGE_CMD as REVRANGE_CMD, TimeSeriesCommands as TimeSeriesCommands
from .info import TSInfo as TSInfo
from .utils import parse_get as parse_get, parse_m_get as parse_m_get, parse_m_range as parse_m_range, parse_range as parse_range
from _typeshed import Incomplete
from redis._parsers.helpers import bool_ok as bool_ok

class TimeSeries(TimeSeriesCommands):
    client: Incomplete
    execute_command: Incomplete
    def __init__(self, client: Incomplete | None = ..., **kwargs) -> None: ...
    def pipeline(self, transaction: bool = ..., shard_hint: Incomplete | None = ...): ...

class ClusterPipeline(TimeSeriesCommands, redis.cluster.ClusterPipeline, metaclass=abc.ABCMeta): ...
class Pipeline(TimeSeriesCommands, redis.client.Pipeline): ...
