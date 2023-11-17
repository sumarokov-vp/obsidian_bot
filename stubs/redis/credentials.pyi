from _typeshed import Incomplete
from typing import Optional, Tuple, Union

class CredentialProvider:
    def get_credentials(self) -> Union[Tuple[str], Tuple[str, str]]: ...

class UsernamePasswordCredentialProvider(CredentialProvider):
    username: Incomplete
    password: Incomplete
    def __init__(self, username: Optional[str] = ..., password: Optional[str] = ...) -> None: ...
    def get_credentials(self): ...
