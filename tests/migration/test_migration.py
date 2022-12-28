import json
from pathlib import Path

from pytest import raises

from json_orm.migration import create_table, drop_table
from json_orm.model import CharField, create_base


def test_create_table(tmp_path: Path) -> None:
    # Arrange
    database_path = tmp_path / 'database'
    database_path.mkdir()

    Base = create_base(database_path)

    class Model(Base):
        table_name = 'table'
        first_field = CharField()
        second_field = CharField()

    # Act
    create_table(Model, database_path)
    with open(database_path / 'table.json', 'r') as f:
        table_json = json.load(f)

    # Assert
    assert table_json == \
        [{'first_field': 'CharField', 'second_field': 'CharField'}]


def test_drop_table(tmp_path: Path) -> None:
    # Arrange
    database_path = tmp_path / 'database'
    database_path.mkdir()

    table_path = database_path / 'table.json'
    table_path.touch()

    with open(table_path, 'w') as f:
        json.dump([{'some_field': 'field_type'}], f)

    class ModelMock:
        table_name = 'table'

    # Act
    drop_table(ModelMock, database_path)

    # Assert
    with raises(FileNotFoundError):
        open(table_path)
