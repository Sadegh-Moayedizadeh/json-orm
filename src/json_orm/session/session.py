import json
from contextlib import contextmanager
from pathlib import Path
from typing import Union


class Session:
    def __init__(self, directory_path: Union[str, Path]) -> None:
        self._directory_path = directory_path \
            if isinstance(directory_path, Path) else Path(directory_path)

    @contextmanager
    def json_read(self, file_name: str):
        file_name = self._ensure_file_name_endswith_json(file_name)
        file_path = self._directory_path / file_name
        json_file = open(file_path, 'r')
        json_obj = json.load(json_file)
        yield json_obj
        json_file.close()

    @contextmanager
    def json_update(self, file_name: str):
        file_name = self._ensure_file_name_endswith_json(file_name)
        file_path = self._directory_path / file_name
        json_file = open(file_path, 'r+')
        json_obj = json.load(json_file)
        yield json_obj
        json_file.seek(0)
        json.dump(json_obj, json_file)
        json_file.truncate()
        json_file.close()

    def _ensure_file_name_endswith_json(self, file_name: str) -> str:
        if file_name.endswith('.json'):
            return file_name
        return file_name + '.json'
