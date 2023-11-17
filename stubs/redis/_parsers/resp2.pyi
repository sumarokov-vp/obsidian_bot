from ..exceptions import ConnectionError as ConnectionError, InvalidResponse as InvalidResponse, ResponseError as ResponseError
from ..typing import EncodableT as EncodableT
from .base import _AsyncRESPBase, _RESPBase
from .socket import SERVER_CLOSED_CONNECTION_ERROR as SERVER_CLOSED_CONNECTION_ERROR

class _RESP2Parser(_RESPBase):
    def read_response(self, disable_decoding: bool = ...): ...

class _AsyncRESP2Parser(_AsyncRESPBase):
    async def read_response(self, disable_decoding: bool = ...): ...
