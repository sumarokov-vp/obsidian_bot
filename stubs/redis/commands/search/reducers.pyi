from .aggregation import Asc as Asc, Desc as Desc, Reducer as Reducer, SortDirection as SortDirection
from typing import Union

class FieldOnlyReducer(Reducer):
    def __init__(self, field: str) -> None: ...

class count(Reducer):
    NAME: str
    def __init__(self) -> None: ...

class sum(FieldOnlyReducer):
    NAME: str
    def __init__(self, field: str) -> None: ...

class min(FieldOnlyReducer):
    NAME: str
    def __init__(self, field: str) -> None: ...

class max(FieldOnlyReducer):
    NAME: str
    def __init__(self, field: str) -> None: ...

class avg(FieldOnlyReducer):
    NAME: str
    def __init__(self, field: str) -> None: ...

class tolist(FieldOnlyReducer):
    NAME: str
    def __init__(self, field: str) -> None: ...

class count_distinct(FieldOnlyReducer):
    NAME: str
    def __init__(self, field: str) -> None: ...

class count_distinctish(FieldOnlyReducer):
    NAME: str

class quantile(Reducer):
    NAME: str
    def __init__(self, field: str, pct: float) -> None: ...

class stddev(FieldOnlyReducer):
    NAME: str
    def __init__(self, field: str) -> None: ...

class first_value(Reducer):
    NAME: str
    def __init__(self, field: str, *byfields: Union[Asc, Desc]) -> None: ...

class random_sample(Reducer):
    NAME: str
    def __init__(self, field: str, size: int) -> None: ...
