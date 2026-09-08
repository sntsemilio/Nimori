# Nimori

[![CI](https://github.com/sntsemilio/Nimori/actions/workflows/ci.yml/badge.svg)](https://github.com/sntsemilio/Nimori/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status: WIP](https://img.shields.io/badge/status-WIP-orange.svg)](docs/ROADMAP.md)

**Pequeños modelos. Grandes preguntas.**

Un laboratorio educativo de IA que vive en tu terminal. Nimori tendrá paneles para código, papers, fórmulas y gráficos, con prácticas de modelos pequeños, arquitecturas, serving, harnesses y agentes. Su personaje es una pequeña luciérnaga curiosa que invita a observar y comprobar.

> [!IMPORTANT]
> **Proyecto en desarrollo activo (WIP).** La API, los comandos y el formato de datos pueden cambiar. Nimori todavía no ejecuta modelos ni debe usarse para producir benchmarks.

**Corte actual: v0.1.0.dev1, Destello en desarrollo.** Conserva la CLI Semilla y añade la base navegable de la TUI: cuatro regiones, pestañas de referencias, foco por teclado, ampliación y modo compacto. El worker, las imágenes, el lector PDF y la inferencia todavía no están implementados. No se incluyen pesos, métricas simuladas ni descargas automáticas.

## Estado

| Área | Disponible | Siguiente paso |
|---|---|---|
| CLI y catálogo | Diagnóstico, fichas y preparación de prácticas | Mantener contratos al ampliar el producto |
| TUI | Paneles, pestañas, foco, ampliación y modo compacto | Worker `scripted` cancelable |
| Visualización | Vistas preparadas y contenido pendiente identificado | Matplotlib, Mathtext y PDF local |
| Modelos | Catálogo de candidatos sin soporte declarado | SmolLM2-135M en v0.2.0 |

## Comenzar

Requisitos: [uv](https://docs.astral.sh/uv/getting-started/installation/) y Python 3.12, seleccionado en `.python-version`. El paquete mantiene compatibilidad declarada con Python 3.11 o posterior. Ejecuta los comandos desde la raíz de este repositorio, donde están este README y `pyproject.toml`.

Linux, macOS, WSL o Windows PowerShell:

```bash
uv sync --locked
uv run nimori
uv run nimori doctor
uv run nimori models list
uv run nimori papers show smollm2
uv run nimori lab init serving/prefill-decode --path my-first-lab
uv run python -m nimori.tui
```

`uv sync --locked` crea `.venv` e instala el proyecto en modo editable respetando `uv.lock`. `uv run` utiliza ese entorno sin necesidad de activarlo; los cambios en `src/` se reflejan al ejecutar la CLI. Si Python 3.12 no está instalado, uv puede descargarlo.

La instalación inicial puede necesitar conexión para obtener Python, `setuptools`, Textual y sus dependencias. No descarga modelos ni recursos de prácticas. Después de sincronizar puedes ejecutar, por ejemplo, `uv run --offline nimori`. El proyecto se instala desde esta carpeta: **no está publicado en PyPI**. Los detalles de las comprobaciones están en `docs/VALIDATION.md`.

La TUI usa `1`–`4` para enfocar sus regiones, `Tab` para recorrer controles, `z` para ampliar o restaurar el panel actual y `q` para salir. Por debajo de 100 columnas muestra una región a la vez; las mismas teclas numéricas cambian de región.

## Superficie disponible en el corte actual

| Comando | Resultado |
|---|---|
| `nimori` | Bienvenida y siguientes acciones |
| `nimori --version` | Versión del programa |
| `nimori doctor --json` | Entorno, paquetes y detección NVIDIA cuando `nvidia-smi` está disponible |
| `nimori models list` | Siete checkpoints candidatos, sin afirmar soporte |
| `nimori models list --capability prefill_decode` | Filtra capacidades previstas |
| `nimori models info smollm2-135m` | Identificador, paper, capacidades y validación pendiente |
| `nimori labs list --model smollm2-135m` | Prácticas previstas para el modelo |
| `nimori labs info serving/prefill-decode` | Pregunta, requisito y versión objetivo |
| `nimori papers list` | Índice bibliográfico |
| `nimori papers show smollm2` | Enlaces y alcance del paper; el visor PDF llegará en v0.1.0 |
| `nimori lab init serving/prefill-decode --path my-first-lab` | Crea `lab.yaml` y `NOTES.md` en un directorio nuevo |
| `python -m nimori.tui` | Abre la base visual de desarrollo con contenido local etiquetado |

`--json` ofrece datos sin mensajes de personalidad. `--help` explica cada grupo. También puedes usar `python -m nimori` dentro del entorno instalado.

El diagnóstico detecta pistas de terminal; no certifica que las imágenes funcionen. La presencia de un driver no certifica que PyTorch pueda ejecutar un modelo. Crear una práctica prepara tu predicción y configuración; no ejecuta todavía inferencia.

## Qué construir ahora

1. Construir NIM-103: worker de demostración `scripted`, eventos y cancelación.
2. Construir NIM-104: gráfico Matplotlib y fórmula Mathtext.
3. Construir NIM-105 y NIM-106: PDF local e integración con el comando `nimori`.
4. Cerrar v0.1.0 antes de añadir el modelo y prefill/decode de v0.2.0.

La primera meta de uso real será v0.2.0. La comparación de políticas de serving llegará en v0.3.0. El diseño completo conserva arquitecturas editables, harnesses y agentes.

## Desarrollo y comprobación

```bash
uv run python -m unittest discover -s tests -v
uv build
```

`uv build` genera el wheel y el archivo fuente en `dist/`.

## Estructura

```text
src/nimori/       CLI, servicios y módulo TUI
tests/            contratos de comportamiento y navegación headless
docs/             especificación, roadmap, marca, alcance y validación
pyproject.toml    metadatos y dependencias del paquete
uv.lock           resolución reproducible del entorno
```

Para [administrar dependencias con uv](https://docs.astral.sh/uv/guides/projects/#managing-dependencies):

```bash
uv add nombre-del-paquete
uv add --dev nombre-de-la-herramienta
uv remove nombre-del-paquete
uv lock --upgrade
uv sync --locked
```

Los nombres anteriores son marcadores: reemplázalos por el paquete que necesites. Versiona `pyproject.toml`, `uv.lock` y `.python-version`; `.venv/` y los artefactos de compilación quedan fuera de Git. Después de cambiar dependencias, ejecuta las pruebas y revisa el diff del lockfile antes de guardar los cambios.

La CLI usa `argparse` y servicios pequeños independientes de la presentación. La base TUI usa Textual y mantiene su entrada separada hasta NIM-106. Agrega las dependencias de imágenes y renderizado con `uv add` en sus módulos. PyTorch/CUDA se valida al añadir inferencia. Las pruebas actuales usan `unittest`, incluido en Python.

Archivos principales: `src/nimori/cli.py`, `catalog.py`, `doctor.py`, `workspace.py`, `data/catalog.json` y `tui/`. El alcance exacto de la primera base visual está en `docs/SCOPE_TUI_BASE.md`. No añadas pesos ni resultados pesados al repositorio.

## Contribuir

Nimori está en una etapa temprana. Antes de proponer cambios, lee [CONTRIBUTING.md](CONTRIBUTING.md), la [especificación](docs/SPEC.md) y el [roadmap](docs/ROADMAP.md). Los reportes de fallos y propuestas pueden abrirse con las plantillas del repositorio.

Código original bajo MIT; modelos, datasets y papers conservan sus propias condiciones. Los enlaces de referencia no incluyen copias de esos recursos.
