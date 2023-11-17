from _typeshed import Incomplete

class VersionMismatchException(Exception):
    version: Incomplete
    def __init__(self, version) -> None: ...
