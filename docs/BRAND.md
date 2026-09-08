# Identidad de Nimori

**Nombre:** Nimori. **Pronunciación propuesta:** ni-MO-ri. **Comando:** `nimori`.

Es un nombre inventado que busca sonar cercano y recordable. La elección evoca la escala pequeña y la curiosidad; no se le atribuye una traducción ni un origen lingüístico real.

**Lema:** Pequeños modelos. Grandes preguntas.

**Descripción breve:** Tu laboratorio de IA en la terminal.

## Personaje

Una pequeña luciérnaga de laboratorio: cuerpo redondeado, dos antenas y luz cálida. Ilumina una parte del sistema para que puedas examinarla. Este archivo define la dirección de diseño; el logotipo y las ilustraciones todavía no están producidos.

## Voz

Curiosa, tranquila y precisa. Habla al usuario como alguien que está aprendiendo a investigar. Propone observar, cambiar una cosa y buscar evidencia. Explica símbolos matemáticos al introducirlos. Cuando una prueba falla, describe lo ocurrido y propone una acción concreta.

| Situación | Texto de producto propuesto |
|---|---|
| Bienvenida | ¿Qué quieres poner a prueba? |
| Antes de una práctica | Cambia una pieza. Predice qué pasará. |
| Resultado disponible | Ya tenemos una observación. Compárala con tu predicción. |
| Intervención incompatible | El bloque produce 128 valores; el siguiente espera 64. Revisa la proyección de salida. |
| Estimación | Estimación estructural: todavía no ejecutamos este modelo. |
| Falta una dependencia | Falta el renderizador PDF. Instala el extra visual indicado en la guía de esta versión. |

Personalidad en la bienvenida, las guías y la retroalimentación. Logs, métricas y errores mantienen precisión. El modo JSON omite adornos. La luciérnaga es un recurso de identidad; no requiere un agente generativo para existir.

## Dirección visual para la TUI

| Uso | Color inicial |
|---|---|
| Fondo | `#121722` |
| Texto | `#E7ECF4` |
| Foco y enlaces | `#A8E6CF` |
| Luz del personaje | `#FFD88A` |
| Selección secundaria | `#C2B7F5` |

Son decisiones de diseño, pendientes de QA visual. Cada estado tendrá etiqueta textual además de color. Respetar `NO_COLOR`, reducción de movimiento y terminal sin imágenes al desarrollar las vistas.

## Identificadores

| Elemento | Nombre |
|---|---|
| Producto | Nimori |
| Ejecutable | `nimori` |
| Distribución Python local | `nimori-lab` |
| Módulo Python | `nimori` |
| Repositorio previsto | `nimori` |
| Variable futura para ubicación de datos | `NIMORI_DATA_DIR` |

La distribución se entrega como proyecto local. No se ha publicado ni reservado el nombre del paquete o un dominio. La búsqueda preliminar de nombre sirve para orientar la elección, sin certificar exclusividad.
