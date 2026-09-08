# Primeras versiones de Nimori

Estado al 8 de septiembre de 2026. Las versiones siguientes son entregables, no fechas prometidas. El corte actual es v0.1.0.dev1: NIM-101 y NIM-102 están implementados; Destello todavía no está cerrado.

| Versión | Nombre | Entrega | Criterio para cerrar |
|---|---|---|---|
| 0.0.1 | Semilla | CLI, diagnóstico, catálogo y preparación de prácticas | Instalación local y comandos comprobados; sin soporte de modelos declarado |
| 0.1.0 | Destello | TUI con paneles, gráfica, fórmula y PDF local | Navegar, redimensionar y cancelar una tarea de demostración sin bloquear las vistas |
| 0.2.0 | Pulso | Una inferencia real con SmolLM2-135M y fases explícitas | Equivalencia con referencia, eventos persistidos, gráfica y replay etiquetado |
| 0.3.0 | Flujo | Carga, cola y prefill fragmentado | Comparación reproducible entre políticas; máscaras, posiciones y caché correctas |
| 0.4.0 | Lupa | Pythia e intervenciones; análisis de un bloque nuevo | Modificación observable y estimaciones con supuestos; pesos nuevos identificados |
| 0.5.0 | Brújula | Harnesses y agente local | Recuperación ante fallo programado y evaluación en escenario nuevo; luego prueba con modelo real |
| 0.6.0 | Constelación | Extensiones, Mamba y adaptador vLLM opcional | Práctica añadida por contrato y capacidades comprobadas por backend |

## v0.1.0: siguiente sesión de desarrollo

Estado del corte actual:

| Ticket | Estado | Evidencia |
|---|---|---|
| NIM-101 | Implementado | Textual 8.2.8 resuelto en `uv.lock`; CLI y catálogo conservados |
| NIM-102 | Implementado | Cuatro regiones, tres pestañas, foco, ampliación y modo compacto con pruebas headless |
| NIM-103–NIM-107 | Pendiente | No forman parte de v0.1.0.dev1 |

| Ticket | Trabajo | Depende de | Prueba de aceptación |
|---|---|---|---|
| NIM-101 | Añadir Textual y fijar entorno resuelto | Base 0.0.1 | Instalación repetible; catálogo sigue funcionando sin cargar modelos |
| NIM-102 | TUI con guía, código, referencias y logs | NIM-101 | Foco y pestañas navegables; modo de panel único para pantalla pequeña |
| NIM-103 | Worker de demostración y cancelación | NIM-102 | Navegación responde durante la tarea; eventos identificados como `scripted` |
| NIM-104 | Imagen Matplotlib y fórmula Mathtext | NIM-102 | Reescalado limpio en la terminal de referencia; fuente y datos disponibles |
| NIM-105 | PDF local con pypdfium2 | NIM-104 | Abrir documento, cambiar página y ajustar al ancho; error claro si falta el archivo |
| NIM-106 | Entrada `nimori` a la TUI y diagnóstico gráfico | NIM-102–105 | Entrada interactiva abre paneles; salida redirigida conserva CLI; capabilities comprobadas |
| NIM-107 | Guía, comandos y nota de versión | NIM-106 | Otra persona puede repetir la sesión y conoce qué se ejecutó |

La sesión inicial termina con los cuatro paneles y contenido local etiquetado. Tectonic completo, buscador PDF, marcas, zoom fino y editor avanzado tienen tareas posteriores; el corte inicial mantiene lectura de página, ecuación y gráfico integrados.

## v0.2.0: primera sesión sobre un modelo

| Ticket | Trabajo | Prueba de aceptación |
|---|---|---|
| NIM-201 | Resolver un checkpoint/tokenizer y revisión inmutable | Registrar revisión, licencia, tamaño y perfil real; descarga mediante acción explícita |
| NIM-202 | Adaptador SmolLM2 con prefill/decode | Comparar logits con tolerancia y tokens greedy contra una referencia |
| NIM-203 | Run inmutable y secuencia de eventos | Guardar configuración, relojes, pesos, semilla y eventos; completar/cancelar/fallar coherentemente |
| NIM-204 | Streaming local y mediciones | Distinguir tiempo de cola, prefill, GPU y TTFT; manejar cero y un token |
| NIM-205 | Guía enlazada a código y paper | Anclas revisadas sobre la versión concreta del PDF |
| NIM-206 | Replay | Reabrir resultados sin inferencia; conservar `evidence_kind` y procedencia del origen |

## v0.3.0: primera comparación de serving

Implementar primero una cola explícita. Después prefill completo frente a fragmentado con el mismo calendario de llegada. El trabajo por solicitud se etiqueta como tal hasta implementar batches reales; una lista procesada secuencialmente no demuestra batching continuo.

El criterio de salida exige un caso donde se conserve la corrección del caché y se puedan interpretar las latencias de solicitudes cortas cuando llega un prompt largo. No se exige obtener una mejora predeterminada.

## Política de entrega

Cada versión actualiza README, catálogo de capacidades y nota de validación. Documentar entorno y límites observados. Conservar configuración y datos de las figuras. Un modelo pasa de candidato a validado únicamente para las capacidades y dispositivos probados. El catálogo no hereda soporte de una familia entera por haber probado un checkpoint.

La base usa Python estándar y se administra con uv. Al introducir dependencias, actualizar el `uv.lock` existente con uv y probar el entorno resuelto; no escribir manualmente hashes o revisiones supuestamente comprobadas.
