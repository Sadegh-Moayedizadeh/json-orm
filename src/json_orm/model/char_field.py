from typing import Any


class CharField:
    def __init__(self) -> None:
        pass

    def __get__(self, obj, obj_type=None) -> str:
        return obj._char_field

    def __set__(self, obj, value: Any) -> None:
        obj._char_field = str(value)
