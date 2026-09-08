"""Create an editable lab plan. Execution is introduced in a later release."""

import json
import shutil
from pathlib import Path

from nimori import __version__
from nimori.catalog import lookup


def initialize(lab_id: str, destination: Path, model_id: str | None = None) -> dict:
    lab = lookup("labs", lab_id)
    selected = model_id or lab["default_model"]
    if selected is not None:
        lookup("models", selected)
        if selected not in lab["candidate_models"]:
            raise ValueError(f"{selected!r} no está previsto para esta práctica. Consulta su ficha.")
    target = destination.expanduser().absolute()
    # Refuse any existing directory, including an empty one, to avoid replacing user work.
    try:
        target.mkdir(parents=True, exist_ok=False)
    except FileExistsError as error:
        raise ValueError(f"{target} ya existe. Elige un directorio nuevo para conservar su contenido.") from error
    config = {
        "schema_version": 1,
        "lab_id": lab_id,
        "lab_version": lab["version"],
        "execution_status": "planned",
        "model": selected,
        "model_revision": None,
        "seed": 42,
    }
    notes = f"""# {lab['title']}

Estado: plan editable. Nimori {__version__} todavía no ejecuta esta práctica.

{lab['question']}

## Antes de ejecutar

- Mi predicción:
- Qué cambiaré:
- Qué mantendré constante:
- Qué medición podría refutar mi predicción:

## Resultado y explicación

Pendientes de una ejecución real en la versión indicada por el catálogo.

## Reto de transferencia

{lab['transfer_challenge']}
"""
    try:
        (target / "lab.yaml").write_text(
            "# Plan generado por Nimori; no es una ejecución ni resuelve una revisión de pesos.\n"
            + "\n".join(f"{key}: {json.dumps(value, ensure_ascii=False)}" for key, value in config.items()) + "\n",
            encoding="utf-8",
        )
        (target / "NOTES.md").write_text(notes, encoding="utf-8")
    except OSError:
        # Only this newly created directory belongs to the operation.
        shutil.rmtree(target)
        raise
    return {"schema_version": 1, "path": str(target), "files": ["lab.yaml", "NOTES.md"],
            "execution_status": "planned", "target_release": lab["target_release"]}
