from _typeshed import Incomplete
from fastapi.requests import Request as Request
from telebot.types import Update as Update
from typing import Optional

fastapi_installed: bool

class SyncWebhookListener:
    app: Incomplete
    def __init__(self, bot, secret_token: str, host: Optional[str] = ..., port: Optional[int] = ..., ssl_context: Optional[tuple] = ..., url_path: Optional[str] = ...) -> None: ...
    def process_update(self, request: Request, update: dict): ...
    def run_app(self) -> None: ...
