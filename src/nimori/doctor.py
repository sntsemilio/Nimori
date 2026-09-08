"""Small, read-only environment report. No downloads and no torch import."""

import csv
import importlib.metadata
import io
import os
import platform
import shutil
import subprocess
import sys

from nimori import __version__


def inspect_environment() -> dict:
    packages = {}
    for name in ("torch", "transformers", "textual", "textual-image", "matplotlib", "pypdfium2"):
        try:
            packages[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            packages[name] = None
    gpu = {"status": "not_detected", "devices": [], "note": "nvidia-smi no está disponible; otros backends quedan sin comprobar."}
    binary = shutil.which("nvidia-smi")
    if binary:
        try:
            result = subprocess.run(
                [binary, "--query-gpu=name,memory.total,memory.free,driver_version", "--format=csv,noheader,nounits"],
                capture_output=True, text=True, timeout=5, check=False,
            )
            if result.returncode:
                gpu = {"status": "query_failed", "devices": [], "note": f"nvidia-smi terminó con código {result.returncode}."}
            else:
                devices = []
                for row in csv.reader(io.StringIO(result.stdout)):
                    if len(row) != 4:
                        continue
                    name, total, free, driver = (part.strip() for part in row)
                    devices.append({"name": name, "memory_total_mib": total, "memory_free_mib": free, "driver": driver})
                gpu = {"status": "detected" if devices else "not_detected", "devices": devices,
                       "note": "Detección del driver; inferencia CUDA y uso de memoria por modelo pendientes de validar."}
        except (OSError, subprocess.TimeoutExpired) as error:
            gpu = {"status": "query_failed", "devices": [], "note": f"No se pudo completar la consulta ({type(error).__name__})."}
    size = shutil.get_terminal_size(fallback=(80, 24))
    kitty_hint = bool(os.environ.get("KITTY_WINDOW_ID")) or os.environ.get("TERM") == "xterm-kitty"
    return {
        "schema_version": 1,
        "nimori_version": __version__,
        "status": "inspection_completed_validation_pending",
        "python": platform.python_version(),
        "platform": {"system": platform.system(), "machine": platform.machine(),
                     "wsl_hint": "microsoft" in platform.release().lower()},
        "terminal": {"term": os.environ.get("TERM", ""), "program": os.environ.get("TERM_PROGRAM", ""),
                     "interactive": sys.stdout.isatty(), "columns": size.columns, "rows": size.lines,
                     "graphics_hint": "kitty" if kitty_hint else "unknown", "graphics_validated": False},
        "packages": packages,
        "nvidia": gpu,
        "next_step": "Validar paneles e imágenes en v0.1.0; validar inferencia PyTorch en v0.2.0.",
    }
