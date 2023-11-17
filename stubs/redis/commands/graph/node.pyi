from ..helpers import quote_string as quote_string
from _typeshed import Incomplete

class Node:
    id: Incomplete
    alias: Incomplete
    label: Incomplete
    labels: Incomplete
    properties: Incomplete
    def __init__(self, node_id: Incomplete | None = ..., alias: Incomplete | None = ..., label: Incomplete | None = ..., properties: Incomplete | None = ...) -> None: ...
    def to_string(self): ...
    def __eq__(self, rhs): ...
