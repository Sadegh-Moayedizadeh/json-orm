from pathlib import Path
from json_orm.session import Session


def test_session(tmp_path: Path) -> None:
    # Arrange
    directory_path = tmp_path / 'directory'
    directory_path.mkdir()
    file_path = directory_path / 'file.json'
    file_path.touch()
    with open(file_path, 'w') as f:
        f.write('[]')

    # Act
    session = Session(directory_path)
    with session.json_update('file') as json_obj:
        json_obj.append('value')

    # Assert
    with session.json_read('file') as json_obj:
        assert json_obj == ['value']
