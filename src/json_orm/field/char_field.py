from typing import Any

from json_orm.field.field_base import FieldBase


class CharField(FieldBase[str]):
    def type_factory(self, value: Any) -> str:
        return str(value)
