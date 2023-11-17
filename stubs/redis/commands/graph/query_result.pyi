from .edge import Edge as Edge
from .exceptions import VersionMismatchException as VersionMismatchException
from .node import Node as Node
from .path import Path as Path
from _typeshed import Incomplete
from redis import ResponseError as ResponseError

LABELS_ADDED: str
LABELS_REMOVED: str
NODES_CREATED: str
NODES_DELETED: str
RELATIONSHIPS_DELETED: str
PROPERTIES_SET: str
PROPERTIES_REMOVED: str
RELATIONSHIPS_CREATED: str
INDICES_CREATED: str
INDICES_DELETED: str
CACHED_EXECUTION: str
INTERNAL_EXECUTION_TIME: str
STATS: Incomplete

class ResultSetColumnTypes:
    COLUMN_UNKNOWN: int
    COLUMN_SCALAR: int
    COLUMN_NODE: int
    COLUMN_RELATION: int

class ResultSetScalarTypes:
    VALUE_UNKNOWN: int
    VALUE_NULL: int
    VALUE_STRING: int
    VALUE_INTEGER: int
    VALUE_BOOLEAN: int
    VALUE_DOUBLE: int
    VALUE_ARRAY: int
    VALUE_EDGE: int
    VALUE_NODE: int
    VALUE_PATH: int
    VALUE_MAP: int
    VALUE_POINT: int

class QueryResult:
    graph: Incomplete
    header: Incomplete
    result_set: Incomplete
    def __init__(self, graph, response, profile: bool = ...) -> None: ...
    def parse_results(self, raw_result_set) -> None: ...
    statistics: Incomplete
    def parse_statistics(self, raw_statistics) -> None: ...
    def parse_header(self, raw_result_set): ...
    def parse_records(self, raw_result_set): ...
    def parse_entity_properties(self, props): ...
    def parse_string(self, cell): ...
    def parse_node(self, cell): ...
    def parse_edge(self, cell): ...
    def parse_path(self, cell): ...
    def parse_map(self, cell): ...
    def parse_point(self, cell): ...
    def parse_null(self, cell) -> None: ...
    def parse_integer(self, cell): ...
    def parse_boolean(self, value): ...
    def parse_double(self, cell): ...
    def parse_array(self, value): ...
    def parse_unknown(self, cell) -> None: ...
    def parse_scalar(self, cell): ...
    def parse_profile(self, response) -> None: ...
    def is_empty(self): ...
    @property
    def labels_added(self): ...
    @property
    def labels_removed(self): ...
    @property
    def nodes_created(self): ...
    @property
    def nodes_deleted(self): ...
    @property
    def properties_set(self): ...
    @property
    def properties_removed(self): ...
    @property
    def relationships_created(self): ...
    @property
    def relationships_deleted(self): ...
    @property
    def indices_created(self): ...
    @property
    def indices_deleted(self): ...
    @property
    def cached_execution(self): ...
    @property
    def run_time_ms(self): ...
    @property
    def parse_scalar_types(self): ...
    @property
    def parse_record_types(self): ...

class AsyncQueryResult(QueryResult):
    def __init__(self) -> None: ...
    graph: Incomplete
    header: Incomplete
    result_set: Incomplete
    async def initialize(self, graph, response, profile: bool = ...): ...
    async def parse_node(self, cell): ...
    async def parse_scalar(self, cell): ...
    async def parse_records(self, raw_result_set): ...
    async def parse_results(self, raw_result_set) -> None: ...
    async def parse_entity_properties(self, props): ...
    async def parse_edge(self, cell): ...
    async def parse_path(self, cell): ...
    async def parse_map(self, cell): ...
    async def parse_array(self, value): ...