from .commands import *
from ..helpers import get_protocol_version as get_protocol_version, parse_to_list as parse_to_list
from .info import BFInfo as BFInfo, CFInfo as CFInfo, CMSInfo as CMSInfo, TDigestInfo as TDigestInfo, TopKInfo as TopKInfo
from _typeshed import Incomplete
from redis._parsers.helpers import bool_ok as bool_ok

class AbstractBloom:
    @staticmethod
    def append_items(params, items) -> None: ...
    @staticmethod
    def append_error(params, error) -> None: ...
    @staticmethod
    def append_capacity(params, capacity) -> None: ...
    @staticmethod
    def append_expansion(params, expansion) -> None: ...
    @staticmethod
    def append_no_scale(params, noScale) -> None: ...
    @staticmethod
    def append_weights(params, weights) -> None: ...
    @staticmethod
    def append_no_create(params, noCreate) -> None: ...
    @staticmethod
    def append_items_and_increments(params, items, increments) -> None: ...
    @staticmethod
    def append_values_and_weights(params, items, weights) -> None: ...
    @staticmethod
    def append_max_iterations(params, max_iterations) -> None: ...
    @staticmethod
    def append_bucket_size(params, bucket_size) -> None: ...

class CMSBloom(CMSCommands, AbstractBloom):
    client: Incomplete
    commandmixin: Incomplete
    execute_command: Incomplete
    def __init__(self, client, **kwargs) -> None: ...

class TOPKBloom(TOPKCommands, AbstractBloom):
    client: Incomplete
    commandmixin: Incomplete
    execute_command: Incomplete
    def __init__(self, client, **kwargs) -> None: ...

class CFBloom(CFCommands, AbstractBloom):
    client: Incomplete
    commandmixin: Incomplete
    execute_command: Incomplete
    def __init__(self, client, **kwargs) -> None: ...

class TDigestBloom(TDigestCommands, AbstractBloom):
    client: Incomplete
    commandmixin: Incomplete
    execute_command: Incomplete
    def __init__(self, client, **kwargs) -> None: ...

class BFBloom(BFCommands, AbstractBloom):
    client: Incomplete
    commandmixin: Incomplete
    execute_command: Incomplete
    def __init__(self, client, **kwargs) -> None: ...
