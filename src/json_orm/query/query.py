import json
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Dict, Generator, List, Mapping, Union


class Query:
    def __init__(self, database_path: Union[str, Path]) -> None:
        self._database_path = database_path \
            if isinstance(database_path, Path) else Path(database_path)

    def get(self, table_name: str, id: str) -> Mapping[str, Any]:
        with self._get_session(table_name) as table:
            result = list(filter(lambda d: d['id'] == id, table))
        if len(result) == 0:
            raise ValueError('There is no entry with the given id.')
        if len(result) > 1:
            raise ValueError('There is more than one entry with the given id.')
        return result.pop()

    def create(self, table_name: str, **kwargs) -> None:
        with self._update_session(table_name) as table:
            self._validate_with_schema(table, kwargs)
            table.append(kwargs)

    def update(self, **kwargs) -> None:
        pass

    def delete(self) -> None:
        pass

    @contextmanager
    def _get_session(
        self, table_name: str
    ) -> Generator[List[Dict[str, Any]], None, None]:
        table_path = self._database_path / (table_name + '.json')
        json_file = open(table_path, 'r')
        json_obj = json.load(json_file)
        yield json_obj
        json_file.close()

    @contextmanager
    def _update_session(
        self, table_name: str
    ) -> Generator[List[Dict[str, Any]], None, None]:
        table_path = self._database_path / (table_name + '.json')
        json_file = open(table_path, 'r+')
        json_obj = json.load(json_file)
        yield json_obj
        json_file.seek(0)
        json.dump(json_obj, json_file)
        json_file.truncate()
        json_file.close()

    def _validate_with_schema(
        self, table: List[Dict[str, Any]], entry: Dict[str, Any]
    ) -> None:
        schema = self._get_schema(table)
        if set(entry.keys()) != set(schema.keys()):
            raise ValueError('The entry does not match the schema.')

    def _get_schema(self, table: List[Dict[str, Any]]) -> None:
        return table[0]
