import json
from typing import Union, List, Dict, Any
from pathlib import Path


class Query:
    def __init__(self, database_address: Union[Path, str]) -> None:
        self._database_address = database_address if \
            isinstance(database_address, Path) else Path(database_address)

    def create(self, table_name: str, **kwargs) -> None:
        table_name += '.json'
        table_address = self._database_address / table_name
        with open(table_address, 'r+') as json_file:
            table: List[Dict[Any, Any]] = json.load(json_file)
            table.append(kwargs)
            json_file.seek(0)
            json.dump(table, json_file)
            json_file.truncate()
