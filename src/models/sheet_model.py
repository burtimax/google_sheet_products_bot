import json
from dataclasses import dataclass, asdict
from typing import List


@dataclass
class SheetModel:
    gpt_model: str
    admin_username: str
    timeout_sec: int
    active_key: int
    keys: List[str]
    prompt: str
    products_short_info: List[str]
    products_info: List[str]

    def to_json(self) -> str:
        """
        Преобразует объект SheetModel в JSON строку.
        """
        return json.dumps(asdict(self), indent=4)