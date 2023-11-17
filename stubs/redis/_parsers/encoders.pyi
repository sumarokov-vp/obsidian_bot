from ..exceptions import DataError as DataError
from _typeshed import Incomplete

class Encoder:
    encoding: Incomplete
    encoding_errors: Incomplete
    decode_responses: Incomplete
    def __init__(self, encoding, encoding_errors, decode_responses) -> None: ...
    def encode(self, value): ...
    def decode(self, value, force: bool = ...): ...
