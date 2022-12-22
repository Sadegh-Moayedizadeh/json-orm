from pathlib import Path
from typing import Union, Dict, Any, List

from json_orm.session import Session


class Query:
    def __init__(self, database_address: Union[Path, str]) -> None:
        self._session = Session(database_address)

    def create(self, table_name: str, **kwargs) -> None:
        with self._session.json_update(table_name) as table:
            self._validate_against_schema(kwargs, table)
            table.append(kwargs)

    def _validate_against_schema(
        self,
        insert_data: Dict[str, Any],
        table: List[Dict[str, Any]]
    ) -> None:
        if not set(table[0].keys()) == set(insert_data.keys()):
            raise ValueError('The insert row does not match schema.')
