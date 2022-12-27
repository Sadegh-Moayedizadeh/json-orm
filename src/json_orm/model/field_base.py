from typing import TypeVar, Optional, Generic, Type, Any
from json_orm.model.model_base import ModelBase
from abc import ABC, abstractmethod


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
        self._value = None

    @abstractmethod
    def type_factory(self, value: Any) -> FieldType:
        pass

    def __get__(self, obj: ModelBase, obj_type: Type[ModelBase]) -> FieldType:
        return self._value

    def __set__(self, obj: ModelBase, value: Any) -> None:
        self._value = self.type_factory(value)

    def __set_name__(self, owner: ModelBase, name: str) -> None:
        self._public_name = name
