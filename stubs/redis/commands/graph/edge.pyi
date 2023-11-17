from ..helpers import quote_string as quote_string
from .node import Node as Node
from _typeshed import Incomplete

class Edge:
    id: Incomplete
    relation: Incomplete
    properties: Incomplete
    src_node: Incomplete
    dest_node: Incomplete
    def __init__(self, src_node, relation, dest_node, edge_id: Incomplete | None = ..., properties: Incomplete | None = ...) -> None: ...
    def to_string(self): ...
    def __eq__(self, rhs): ...
