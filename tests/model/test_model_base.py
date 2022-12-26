import json
from pathlib import Path

from json_orm.model import create_base
from pytest import raises


def test_get_method_should_raise_error_if_there_is_no_entry(
    tmp_path: Path
) -> None:
    # Arrange
    database_path = tmp_path / 'database'
    database_path.mkdir()

    table_path = database_path / 'table.json'
    table_path.touch()

    with open(table_path, 'w') as f:
        json.dump([{'id': 'str'}], f)

    Base = create_base(database_path)

    class Model(Base):
        table_name = 'table'

    # Act, Assert
    with raises(ValueError, match='no entry'):
        Model.get(id='dummy_id')


def test_get_method_should_return_entry_with_matching_id(
    tmp_path: Path
) -> None:
    # Arrange
    database_path = tmp_path / 'database'
    database_path.mkdir()

    table_path = database_path / 'table.json'
    table_path.touch()

    with open(table_path, 'w') as f:
        json.dump([{'id': 'str'}, {'id': 'existing_id'}], f)

    Base = create_base(database_path)

    class Model(Base):
        table_name = 'table'

    # Act
    entry = Model.get(id='existing_id')

    # Assert
    assert entry['id'] == 'existing_id'


def test_get_method_should_raise_error_if_there_is_more_than_one_matching_entry(  # noqa: E501
    tmp_path: Path
) -> None:
    # Arrange
    database_path = tmp_path / 'database'
    database_path.mkdir()

    table_path = database_path / 'table.json'
    table_path.touch()

    with open(table_path, 'w') as f:
        json.dump(
            [
                {'id': 'str'},
                {'id': 'repetitive_id'},
                {'id': 'repetitive_id'}
            ], f
        )

    Base = create_base(database_path)

    class Model(Base):
        table_name = 'table'

    # Act, Assert
    with raises(ValueError, match='more than one entry'):
        Model.get(id='repetitive_id')


def test_create_method_should_add_an_entry(tmp_path: Path) -> None:
    # Arrange
    database_path = tmp_path / 'database'
    database_path.mkdir()

    table_path = database_path / 'table.json'
    table_path.touch()

    with open(table_path, 'w') as f:
        json.dump([{'id': 'str'}], f)

    Base = create_base(database_path)

    class Model(Base):
        table_name = 'table'
        def __init__(self, id: str) -> None:
            self.id = id

    # Act
    model = Model(id='some_id')
    model.create()
    
    with open(table_path) as f:
        table = json.load(f)

    # Assert
    assert len(table) == 2
    assert table[-1] == {'id': 'some_id'}


def test_create_with_entry_not_matching_schema_should_raise_exception(
    tmp_path: Path
) -> None:
    # Arrange
    database_path = tmp_path / 'database'
    database_path.mkdir()

    table_path = database_path / 'table.json'
    table_path.touch()

    with open(table_path, 'w') as f:
        json.dump([{'id': 'str'}], f)

    Base = create_base(database_path)

    class Model(Base):
        table_name = 'table'
        def __init__(self, id: str) -> None:
            self.invalid_field_name = id

    # Act
    model = Model(id='some_value')

    # Assert
    with raises(ValueError, match='does not match the schema'):
        model.create()
