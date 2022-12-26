import json
from pathlib import Path

from pytest import raises

from json_orm.query import Query


def test_create(tmp_path: Path) -> None:
    # Arrange
    database = tmp_path / 'database'
    database.mkdir()
    table = database / 'table.json'
    table.touch()
        
    schema = '{"first_field": "str", "second_field": "str"}'
    with open(table, 'w') as f:
        f.write('[{}]'.format(schema))

    # Act
    Query(database).create('table', first_field='a', second_field='b') 
    with open(table, 'r') as f:
        table_josn = json.load(f)

    # Assert
    assert table_josn == [
        {'first_field': 'str', 'second_field': 'str'},
        {'first_field': 'a', 'second_field': 'b'}
    ]


def test_create_with_redundant_fields_should_not_be_allowed(
    tmp_path: Path
) -> None:
    # Arrange
    database = tmp_path / 'database'
    database.mkdir()
    table = database / 'table.json'
    table.touch()
        
    schema = '{"first_field": "str", "second_field": "str"}'
    with open(table, 'w') as f:
        f.write('[{}]'.format(schema))

    # Act, Assert
    with raises(ValueError):
        Query(database).create('table', first_field='a') 
