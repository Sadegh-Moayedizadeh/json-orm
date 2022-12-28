from typing import Any

from json_orm.field.field_base import FieldBase


class IntegerField(FieldBase[int]):
    def type_factory(self, value: Any) -> int:
        return int(value)
