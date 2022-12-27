from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, Type, TypeVar

from json_orm.model.model_base import ModelBase

FieldType = TypeVar('FieldType')


class FieldBase(ABC, Generic[FieldType]):
    def __init__(
        self,
        nullable: bool = True,
        default: Optional[FieldType] = None,
        unique: bool = False,
        primary_key: bool = False
    ) -> None:
        self._public_name = None
        self._obj_to_value = {}

    @abstractmethod
    def type_factory(self, value: Any) -> FieldType:
        pass

    def __get__(self, obj: ModelBase, obj_type: Type[ModelBase]) -> FieldType:
        return self._obj_to_value[obj]

    def __set__(self, obj: ModelBase, value: Any) -> None:
        self._obj_to_value[obj] = self.type_factory(value)

    def __set_name__(self, owner: ModelBase, name: str) -> None:
        self._public_name = name
