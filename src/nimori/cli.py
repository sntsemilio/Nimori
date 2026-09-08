"""The command boundary is small; domain functions are reusable by the future TUI."""

import argparse
import json
import sys
from pathlib import Path

from nimori import __version__
from nimori.catalog import items, lookup
from nimori.doctor import inspect_environment
from nimori.workspace import initialize


def json_flag(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--json", action="store_true", default=argparse.SUPPRESS, help="Salida JSON sin mensajes de personalidad.")


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(prog="nimori", description=f"Pequeños modelos. Grandes preguntas. Versión {__version__}.")
    root.add_argument("--version", action="version", version=f"Nimori {__version__}")
    json_flag(root)
    commands = root.add_subparsers(dest="command")
    doctor = commands.add_parser("doctor", help="Inspeccionar entorno sin descargar modelos.")
    json_flag(doctor)
    for kind, label in (("models", "Modelos candidatos"), ("labs", "Prácticas planificadas"), ("papers", "Referencias bibliográficas")):
        group = commands.add_parser(kind, help=label)
        json_flag(group)
        actions = group.add_subparsers(dest="action", required=True)
        listing = actions.add_parser("list", help=label)
        json_flag(listing)
        if kind == "models":
            listing.add_argument("--capability", help="Filtrar una capacidad prevista; no implica soporte validado.")
        if kind == "labs":
            listing.add_argument("--model", help="Filtrar por modelo candidato.")
        detail = actions.add_parser("show" if kind == "papers" else "info", help="Mostrar la ficha completa.")
        detail.add_argument("id")
        json_flag(detail)
    lab = commands.add_parser("lab", help="Preparar el directorio de una práctica.")
    json_flag(lab)
    actions = lab.add_subparsers(dest="action", required=True)
    init = actions.add_parser("init", help="Crear un plan y notas en un directorio nuevo.")
    init.add_argument("id", help="Identificador del catálogo, por ejemplo serving/prefill-decode.")
    init.add_argument("--path", type=Path, required=True, help="Nuevo directorio de trabajo.")
    init.add_argument("--model", help="Modelo candidato; omitir para usar el de la práctica.")
    json_flag(init)
    return root


def dispatch(args: argparse.Namespace) -> tuple[object, str]:
    if args.command is None:
        return {"name": "Nimori", "version": __version__, "stage": "destello-development", "tagline": "Pequeños modelos. Grandes preguntas."}, "welcome"
    if args.command == "doctor":
        return inspect_environment(), "detail"
    if args.command == "lab":
        return initialize(args.id, args.path, args.model), "workspace"
    kind = args.command
    if args.action != "list":
        return lookup(kind, args.id), "detail"
    rows = items(kind)
    capability = getattr(args, "capability", None)
    if capability:
        known = {value for item in items("models") for value in item["planned_capabilities"]}
        if capability not in known:
            raise ValueError(f"Capacidad desconocida: {capability}. Opciones: {', '.join(sorted(known))}.")
        rows = [item for item in rows if capability in item["planned_capabilities"]]
    model = getattr(args, "model", None)
    if model:
        lookup("models", model)
        rows = [item for item in rows if model in item["candidate_models"]]
    return {"schema_version": 1, "kind": kind, "items": rows}, "list"


def display(data: object, view: str) -> None:
    if view == "welcome":
        print(f"Nimori {__version__}\nPequeños modelos. Grandes preguntas.\n")
        print("¿Qué quieres poner a prueba?\n")
        print("  nimori doctor\n  nimori models list\n  nimori labs list\n  nimori papers show smollm2\n")
        print("CLI disponible. Prueba la base visual con: python -m nimori.tui")
    elif view == "list":
        for item in data["items"]:
            print(f"{item['id']:<32} {item.get('status', 'reference'):<12} {item.get('title', item.get('name', ''))}")
        if data["kind"] != "papers":
            print("\nCatálogo de planificación: todavía no hay modelos ni prácticas de inferencia validados.")
        elif not data["items"]:
            print("Sin referencias.")
    elif view == "workspace":
        print(f"Práctica preparada en {data['path']}\nEscribe tu predicción en NOTES.md.")
        print(f"Ejecución prevista para v{data['target_release']}; esta versión solo prepara el directorio.")
    else:
        print(json.dumps(data, ensure_ascii=False, indent=2))


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    output_json = getattr(args, "json", False)
    try:
        data, view = dispatch(args)
        if output_json:
            print(json.dumps(data, ensure_ascii=False, indent=2))
        else:
            display(data, view)
    except (ValueError, OSError) as error:
        payload = {"error": str(error), "exit_code": 1}
        print(json.dumps(payload, ensure_ascii=False) if output_json else f"Nimori: {error}", file=sys.stderr)
        return 1
    return 0
