"""Metadata only: listing an item does not load or validate a model."""

import json
from importlib.resources import files


def catalog() -> dict:
    return json.loads(files("nimori").joinpath("data/catalog.json").read_text(encoding="utf-8"))


def items(kind: str) -> list[dict]:
    return catalog()[kind]


def lookup(kind: str, item_id: str) -> dict:
    for item in items(kind):
        if item["id"] == item_id:
            return item
    raise ValueError(f"No encuentro {item_id!r} en {kind}. Consulta 'nimori {kind} list'.")
