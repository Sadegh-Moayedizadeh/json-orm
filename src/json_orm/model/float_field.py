from typing import Any


class FloatField:
    def __get__(self, obj, obj_type=None) -> str:
        return obj._float_field

    def __set__(self, obj, value: Any) -> None:
        obj._float_field = float(value)
