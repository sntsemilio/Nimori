# Validación de Nimori

## Base TUI v0.1.0.dev1 — 2026-09-08

Entorno: Linux/WSL, Python 3.12.14, uv 0.12.5 y Textual 8.2.8.

- La suite completa ejecutó nueve pruebas: cinco contratos anteriores y cuatro contratos nuevos de TUI.
- En 140×42, las cuatro regiones permanecen visibles y las tres pestañas pueden activarse.
- La región enfocada puede ampliarse y restaurarse con `z`.
- En 80×24, la aplicación muestra una región a la vez y permite cambiarla con `1`–`4`.
- El cambio simulado entre 140×42 y 80×24 actualiza el modo compacto sin reiniciar la aplicación.
- Se exportó una captura SVG headless de 140×42 para revisar la composición generada.
- El wheel se instaló en un entorno temporal con Python 3.11.16 y las mismas nueve pruebas pasaron, cubriendo las dos versiones incluidas en CI.

La prueba headless verifica el árbol de widgets y su estado, pero no certifica color, legibilidad ni interacción en Kitty real. No se probaron protocolo gráfico, imágenes, Mathtext ni PDF porque pertenecen a NIM-104 y NIM-105. No se ejecutó un worker ni se declaró inferencia.

## Base CLI v0.0.1 — 2026-09-08

## Integración del repositorio con uv — 2026-09-08

El starter se integró en la raíz del repositorio, conservando `src/`, `tests/` y `docs/`. Se añadió `.python-version` con Python 3.12 y se generó `uv.lock` con uv 0.12.5. El entorno `.venv` usa Python 3.12.14 en Linux/WSL y el paquete está instalado en modo editable.

Comprobaciones de esta integración:

- `uv sync --locked`: entorno sincronizado con el lockfile.
- `uv run --locked python -m unittest discover -s tests -v`: las cinco pruebas pasaron.
- `uv run --locked nimori --version`: Nimori 0.0.1.
- `uv run --offline nimori doctor --json`: diagnóstico ejecutado sin conexión; detectó una NVIDIA GeForce RTX 4070 Laptop GPU mediante el driver.
- `uv build`: wheel y distribución fuente generados en `dist/`.

La detección del driver no valida inferencia CUDA. Las funciones visuales y de modelos continúan pendientes según el roadmap. El flujo de desarrollo actualizado está en `README.md`.

## Comprobación original del starter

Entorno de comprobación: Linux x86_64, Python 3.12.13. La base no requiere GPU.

Se construyó un wheel desde `pyproject.toml`, se instaló sin dependencias en un entorno virtual limpio y se invocó el ejecutable `nimori` fuera del repositorio. Se comprobaron bienvenida, versión, diagnóstico JSON, filtro del catálogo, referencia SmolLM2 y listado de prácticas.

Pasaron las cinco pruebas de integración:

1. Catálogo empaquetado accesible fuera del repositorio, sin crear archivos ni declarar capacidades validadas.
2. Inicialización de una práctica y rechazo de una segunda inicialización que reemplazaría notas del usuario.
3. Modelo incompatible rechazado antes de crear el directorio de trabajo.
4. Práctica de harness preparada con modelo nulo para su futura modalidad programada.
5. Comando de ejecución todavía no implementado termina con error de argumento.

La instalación comprobada usa el wheel; la instalación editable del README utiliza el mismo proyecto y queda como ruta de desarrollo. El paquete incluye el wheel en `dist/` para repetir la instalación comprobada.

No había `nvidia-smi` disponible y el entorno no era una terminal gráfica interactiva. No se ejecutaron modelos ni se verificaron GPU, TUI, protocolos gráficos o sistemas Windows/macOS. Esas comprobaciones pertenecen a las versiones que añadan dichas funciones.
