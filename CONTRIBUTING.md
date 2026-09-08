# Contribuir a Nimori

Gracias por ayudar a construir Nimori. El proyecto está en desarrollo activo y todavía no ofrece una versión estable. Conviene acordar cambios grandes en un issue antes de implementarlos.

## Preparar el entorno

Necesitas uv y Python 3.11 o posterior. El entorno de referencia usa Python 3.12.

```bash
git clone https://github.com/sntsemilio/Nimori.git
cd Nimori
uv sync --locked
uv run python -m unittest discover -s tests -v
```

Para abrir la base TUI:

```bash
uv run python -m nimori.tui
```

## Flujo de trabajo

1. Elige un ticket acotado del roadmap o abre un issue explicando el problema.
2. Crea una rama desde `main`.
3. Mantén cada cambio dentro de un módulo o comportamiento verificable.
4. Actualiza las pruebas y la documentación que describen ese comportamiento.
5. Ejecuta la suite completa y `uv build` antes de abrir el pull request.

Al cambiar dependencias usa `uv add` o `uv remove` y versiona juntos `pyproject.toml` y `uv.lock`. No edites manualmente el lockfile.

## Criterios del proyecto

- La CLI y la TUI comparten servicios; la presentación no debe contener la lógica del laboratorio.
- Los datos medidos, estimados, reproducidos y programados deben distinguirse explícitamente.
- No presentes detección de hardware como validación de inferencia.
- No incluyas pesos, datasets, PDFs con restricciones ni resultados pesados en Git.
- Los mensajes visibles al usuario se escriben en español claro; identificadores y código siguen las convenciones de Python.
- Una operación lenta debe mantenerse fuera del hilo de interfaz y poder cerrarse limpiamente.

## Pull requests

Describe el problema, el comportamiento resultante y las comprobaciones realizadas. Si el cambio afecta la TUI, indica el tamaño y la terminal probados. Si una validación depende de GPU, Kitty u otro entorno no disponible, déjala registrada como pendiente en vez de afirmar compatibilidad.

Los mantenedores pueden pedir que un cambio se divida si mezcla módulos o versiones del roadmap.
