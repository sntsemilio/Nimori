# Alcance obtenido: base TUI de Nimori

Versión de desarrollo: `0.1.0.dev1` · Módulo elegido: NIM-102 · Dependencia cubierta: NIM-101

## Objetivo del corte

Establecer el espacio de trabajo visual sobre el que se conectarán ejecución y renderizadores, manteniendo intactos la CLI, el catálogo y la preparación de prácticas de v0.0.1.

## Capacidades disponibles

- Aplicación Textual ejecutable con `uv run python -m nimori.tui`.
- Cuatro regiones: guía, código, referencias y ejecución/logs.
- Pestañas Paper, Fórmulas y Gráficos dentro de referencias.
- Vista de código local, de solo lectura, con numeración y sintaxis Python.
- Navegación con `Tab`; acceso directo a regiones con `1`, `2`, `3` y `4`.
- Ampliación y restauración de la región enfocada con `z`.
- Modo compacto automático por debajo de 100 columnas, con una región visible.
- Paleta inicial de Nimori y estados pendientes expresados también en texto.
- Contenido local que distingue una vista preliminar de una medición o inferencia.

## Contratos preservados

- `nimori`, `doctor`, consultas de catálogo y `lab init` mantienen su comportamiento.
- No se descargan modelos al abrir la TUI.
- No se generan métricas ni resultados que puedan confundirse con una medición real.
- El entry point principal continúa mostrando la CLI hasta completar NIM-106.

## Fuera del alcance

- Worker asíncrono, eventos progresivos y cancelación (NIM-103).
- Figuras Matplotlib y fórmulas Mathtext renderizadas (NIM-104).
- Apertura, navegación y ajuste de PDF local (NIM-105).
- Detección del protocolo gráfico e integración automática con `nimori` (NIM-106).
- Inferencia, PyTorch, CUDA, pesos de modelos, persistencia de runs y replay.

## Evidencia y límites de validación

Nueve pruebas automatizadas pasan en el entorno uv. Cuatro cubren la TUI en modo headless: regiones y pestañas, ampliación, vista compacta y cambio de tamaño. También se generó una captura SVG headless para inspección estructural.

Queda pendiente abrir la aplicación en una sesión Kitty real para validar apariencia, foco visible y respuesta del teclado. Una prueba headless no valida el protocolo gráfico de la terminal. Los detalles reproducibles están en `docs/VALIDATION.md`.

## Siguiente módulo recomendado

NIM-103: definir el contrato mínimo de eventos `scripted`, emitirlos desde un worker sin bloquear la interfaz y cancelar limpiamente. Ese módulo puede conectarse a la región de logs ya creada sin introducir todavía modelos ni métricas GPU.
