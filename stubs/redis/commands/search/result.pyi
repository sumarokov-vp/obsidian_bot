from ._util import to_string as to_string
from .document import Document as Document
from _typeshed import Incomplete

class Result:
    total: Incomplete
    duration: Incomplete
    docs: Incomplete
    def __init__(self, res, hascontent, duration: int = ..., has_payload: bool = ..., with_scores: bool = ...) -> None: ...
