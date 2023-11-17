from ._util import to_string as to_string
from _typeshed import Incomplete
from typing import Optional

class Suggestion:
    string: Incomplete
    payload: Incomplete
    score: Incomplete
    def __init__(self, string: str, score: float = ..., payload: Optional[str] = ...) -> None: ...

class SuggestionParser:
    with_scores: Incomplete
    with_payloads: Incomplete
    sugsize: int
    def __init__(self, with_scores: bool, with_payloads: bool, ret) -> None: ...
    def __iter__(self): ...
