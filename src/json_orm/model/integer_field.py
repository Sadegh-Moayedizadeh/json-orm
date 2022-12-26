from typing import Any


class IntegerField:
    def __get__(self, obj, obj_type=None) -> str:
        return obj._integer_field

    def __set__(self, obj, value: Any) -> None:
        obj._integer_field = int(value)
