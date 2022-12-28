from pathlib import Path
from json_orm.model import create_base, CharField
from json_orm.migration import create_table
import json


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
    pass
