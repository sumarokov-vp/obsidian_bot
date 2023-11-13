from typing import Optional

def format_text(*args, separator: str = ...): ...
def escape_html(content: str) -> str: ...
def escape_markdown(content: str) -> str: ...
def mbold(content: str, escape: Optional[bool] = ...) -> str: ...
def hbold(content: str, escape: Optional[bool] = ...) -> str: ...
def mitalic(content: str, escape: Optional[bool] = ...) -> str: ...
def hitalic(content: str, escape: Optional[bool] = ...) -> str: ...
def munderline(content: str, escape: Optional[bool] = ...) -> str: ...
def hunderline(content: str, escape: Optional[bool] = ...) -> str: ...
def mstrikethrough(content: str, escape: Optional[bool] = ...) -> str: ...
def hstrikethrough(content: str, escape: Optional[bool] = ...) -> str: ...
def mspoiler(content: str, escape: Optional[bool] = ...) -> str: ...
def hspoiler(content: str, escape: Optional[bool] = ...) -> str: ...
def mlink(content: str, url: str, escape: Optional[bool] = ...) -> str: ...
def hlink(content: str, url: str, escape: Optional[bool] = ...) -> str: ...
def mcode(content: str, language: str = ..., escape: Optional[bool] = ...) -> str: ...
def hcode(content: str, escape: Optional[bool] = ...) -> str: ...
def hpre(content: str, escape: Optional[bool] = ..., language: str = ...) -> str: ...
def hide_link(url: str) -> str: ...