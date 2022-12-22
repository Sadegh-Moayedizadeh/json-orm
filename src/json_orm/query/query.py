from pathlib import Path
from typing import Union

from json_orm.session import Session


class Query:
    def __init__(self, database_address: Union[Path, str]) -> None:
        self._session = Session(database_address)

    def create(self, table_name: str, **kwargs) -> None:
        with self._session.json_update(table_name) as table:
            table.append(kwargs)
