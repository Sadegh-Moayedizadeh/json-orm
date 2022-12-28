from pathlib import Path
from typing import Union, Type, Dict
import json

from json_orm.model import ModelBase, FieldBase


def create_table(
    model_class: Type[ModelBase],
    database_path: Union[str, Path]
) -> None:
    schema = _create_schema_from_model(model_class)
    database_path = database_path if isinstance(database_path, Path) \
        else Path(database_path)
    table_path = database_path / (model_class.table_name + '.json')
    with open(table_path, 'w') as table:
        json.dump([schema], table)


def _create_schema_from_model(model_class: Type[ModelBase]) -> Dict[str, str]:
    return {
        field_name: field.__class__.__name__
        for field_name, field in model_class.__dict__.items()
        if isinstance(field, FieldBase)
    }


def drop_table(model_class: Type[ModelBase]) -> None:
    pass
