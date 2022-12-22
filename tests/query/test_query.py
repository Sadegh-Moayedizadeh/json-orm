from json_orm.query import Query
import json
from pathlib import Path


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
