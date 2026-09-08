# Changelog

## 0.1.0.dev1 — Base TUI de Destello — 2026-09-08

- Textual 8.2.8 incorporado al entorno reproducible de uv.
- Espacio de trabajo con regiones de guía, código, referencias y logs.
- Pestañas Paper, Fórmulas y Gráficos con contenido pendiente explícito.
- Navegación por foco, selección directa de regiones y ampliación reversible.
- Modo compacto de una región para terminales menores de 100 columnas.
- Pruebas headless de composición, pestañas, ampliación y redimensionado.
- README público, CI para Python 3.11/3.12 y archivos de colaboración de GitHub.

Pendientes para cerrar v0.1.0: worker cancelable, renderizado Matplotlib/Mathtext, lector PDF, integración del comando principal y validación visual en Kitty.

## 0.0.1 — Semilla — 2026-09-08

- Identidad Nimori y ejecutable `nimori`.
- CLI instalable sin dependencias de ejecución externas.
- Diagnóstico del entorno y detección opcional mediante `nvidia-smi`.
- Catálogo de checkpoints candidatos, papers y prácticas planificadas.
- Preparación de directorios con configuración y preguntas de aprendizaje.
- Especificación, roadmap y encargo para v0.1.0.

Pendientes: TUI, renderizado de imágenes/LaTeX/PDF, descarga de recursos, inferencia, serving, arquitecturas, harnesses y agentes. Los nombres de los futuros comandos se encuentran en docs/SPEC.md.
