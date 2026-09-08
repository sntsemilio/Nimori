# Nimori — Especificación y plan de construcción

Revisión del documento 0.2 · 8 de septiembre de 2026 · Producto: Nimori · Base de código: v0.0.1 (Semilla)

**Estado:** especificación de producto y base instalable v0.0.1 disponibles. La base incluye el comando `nimori`, diagnóstico, un catálogo de planificación y creación de directorios de práctica. La TUI, las imágenes, el lector PDF y la inferencia todavía deben implementarse. Ningún modelo está marcado como validado. Los contratos y comandos futuros están identificados por versión.

> Nota de implementación del 8 de septiembre de 2026: el repositorio avanzó a `0.1.0.dev1`. NIM-101 y NIM-102 ya aportan Textual y una base TUI navegable; el resto de v0.1.0 continúa pendiente. Esta revisión 0.2 se conserva como especificación objetivo y el alcance efectivo se registra en `docs/SCOPE_TUI_BASE.md`.

## 0. Identidad y punto de partida

**Nimori — Pequeños modelos. Grandes preguntas.**

Nimori se pronuncia *ni-MO-ri* y se invoca como `nimori`. Es un nombre inventado, corto y sin acentos en el ejecutable. Su descripción breve es «Tu laboratorio de IA en la terminal». La identidad representa una pequeña luciérnaga curiosa que ilumina un componente para examinarlo. Esta es una dirección de personaje; aún no se ha producido un logotipo.

La voz es cercana, tranquila y precisa: invita a predecir, intervenir, observar y explicar. La bienvenida pregunta «¿Qué quieres poner a prueba?». Una guía propone «Cambia una pieza. Predice qué pasará». Los mensajes de error explican qué ocurrió y la siguiente acción. Las métricas y la salida JSON conservan datos claros. La personalidad se implementa como contenido editorial y diseño; no necesita un tutor generativo.

| Elemento | Decisión |
|---|---|
| Producto / ejecutable | Nimori / `nimori` |
| Distribución Python local / módulo | `nimori-lab` / `nimori` |
| Repositorio previsto | `nimori` |
| Lema | Pequeños modelos. Grandes preguntas. |
| Personaje | Luciérnaga pequeña, curiosa, de luz cálida |
| Paleta inicial | Fondo `#121722`, texto `#E7ECF4`, foco `#A8E6CF`, luz `#FFD88A`, secundario `#C2B7F5` |
| Licencia del código original | MIT; recursos externos conservan sus propias condiciones |

El nombre se adopta para comenzar el desarrollo. El paquete y un dominio no se han publicado ni reservado. Los colores y la representación del personaje se verificarán al construir la TUI; cada estado tendrá texto además de color.

### Entrega que acompaña este documento

`Nimori_Starter_v0.0.1.zip` contiene la carpeta `nimori/` con el proyecto instalable, README, catálogo, pruebas de comportamiento, este documento en `docs/SPEC.md`, identidad en `docs/BRAND.md`, versiones en `docs/ROADMAP.md` y el primer encargo en `docs/FIRST_VERSION_TASK.md`.

La base puede consultar siete checkpoints candidatos, cinco papers y seis prácticas planificadas. `papers show` presenta una ficha bibliográfica; el lector integrado corresponde a v0.1.0. `lab init` crea configuración y notas; la primera inferencia corresponde a v0.2.0.

**Comienza en la sección 17.** El primer trabajo nuevo es v0.1.0: paneles, un gráfico, una fórmula y una página PDF local.

## 1. Definición del producto

Nimori es un laboratorio educativo open source, autohosteado y operado desde la terminal. Permite estudiar, modificar y evaluar modelos y sistemas de IA a pequeña escala mediante prácticas guiadas, modelos pequeños, escenarios controlados, papers y visualizaciones.

**Promesa:** instala un laboratorio en tu equipo, abre un sistema de IA, cambia una pieza y aprende a evaluar qué ocurrió.

El usuario principal es un estudiante, ingeniero o investigador que sabe programar y quiere conectar teoría, implementación y medición sin preparar infraestructura de gran escala. El entorno de referencia es una laptop con GPU; la interfaz también debe permitir leer guías y analizar resultados sin GPU.

El producto reúne cinco objetos: modelos, arquitecturas, laboratorios, ejecuciones y referencias. Un laboratorio conecta los otros cuatro alrededor de una pregunta verificable.

## 2. Requisitos acordados

| ID | Requisito | Consecuencia de diseño |
|---|---|---|
| R01 | Autohosteado y local | Ejecución, progreso y resultados en el equipo del usuario; sin servicio administrado obligatorio |
| R02 | Todo desde terminal | CLI automatizable y TUI interactiva; ningún navegador obligatorio |
| R03 | Paneles laterales y pestañas | Guía, código, papers, fórmulas, gráficos y ejecución visibles en un espacio de trabajo |
| R04 | Gráficos, LaTeX y lector PDF integrado | Renderizado local e integración con una terminal gráfica compatible |
| R05 | Modelos muy pequeños | Descargas bajo demanda y límites de contexto, generación y memoria por práctica |
| R06 | Catálogo con papers | Cada checkpoint tiene ficha, referencias y capacidades de laboratorio explícitas |
| R07 | Arquitecturas editables y nuevas | Adaptadores de arquitectura separados de checkpoints y motores de serving |
| R08 | Explorar sin repetir entrenamientos completos | Intervenciones de inferencia, análisis estructural y ejecuciones precalculadas |
| R09 | Agentes y harnesses | Herramientas locales, escenarios de fallo, trazas y evaluadores |
| R10 | Laboratorios de serving | Prefill, decode, KV cache, carga, scheduler y métricas observables |
| R11 | Catálogo que crezca | Paquetes versionados para incorporar modelos, prácticas y evaluadores |
| R12 | Aprendizaje técnico comprensible | Intuición, fórmulas con cada símbolo definido, código y evidencia conectados |

La instalación inicial descargará dependencias y los recursos seleccionados. Una práctica podrá funcionar sin conexión después de preparar todos sus recursos; la ficha debe declarar cualquier dependencia de red restante.

## 3. Límites científicos que forman parte del producto

Cada resultado tendrá un campo visible `evidence_kind`:

| Valor | Significado | Conclusión permitida |
|---|---|---|
| `measured` | Ejecución real sobre hardware y pesos identificados | Qué ocurrió con esa configuración y ese conjunto de entradas |
| `estimated` | Análisis de estructura o modelo de costos | Dimensiones, parámetros y costos bajo supuestos declarados |
| `replayed` | Resultado de una ejecución anterior | Qué ocurrió en la ejecución de origen |
| `scripted` | Respuestas o fallos programados | Comportamiento del programa ante el escenario definido |

Reglas:

- Cambiar una arquitectura y ejecutar sus pesos disponibles mide el efecto inmediato. No predice su calidad después de entrenarla.
- Los bloques nuevos deben identificarse como no entrenados o con pesos transferidos; la compatibilidad de dimensiones no implica equivalencia funcional.
- Un modelo pequeño permite estudiar mecanismos. Sus capacidades y cuellos de botella no se extrapolan automáticamente a modelos grandes.
- Dos checkpoints entrenados con datos distintos no permiten atribuir una diferencia únicamente a la arquitectura.
- Un resultado guardado nunca aparecerá como una medición en vivo.
- La comparación debe preservar o declarar hardware, pesos, precisión, datos, contexto, generación y política de caché.

## 4. Experiencia educativa

Cada práctica sigue esta secuencia:

1. Pregunta concreta y prerrequisitos.
2. Intuición con un ejemplo pequeño.
3. Predicción del usuario antes de ejecutar.
4. Fórmula y definición de cada variable, símbolo y subíndice, cuando corresponda.
5. Inspección de la implementación.
6. Ejecución de referencia.
7. Modificación de una variable o componente.
8. Comparación y explicación del resultado.
9. Reto de transferencia con una entrada o escenario diferente.

Las explicaciones esenciales estarán escritas, revisadas y versionadas. Un tutor generativo podrá añadirse después como ayuda opcional. El modelo diminuto bajo estudio no será la autoridad encargada de explicar su propia arquitectura.

Las comprobaciones automáticas verificarán propiedades observables: corrección de máscaras, forma de tensores, terminación, uso de herramientas, coherencia de métricas. Las respuestas conceptuales tendrán rúbrica y solución comentada; una coincidencia textual no demostrará comprensión.

## 5. CLI y espacio de trabajo TUI

La misma capa de aplicación debe servir a ambas interfaces. La CLI acepta configuraciones, produce resultados y expone salida JSON. La TUI controla esas mismas operaciones y visualiza sus eventos.

### Distribución

| Región | Pestañas | Contenido |
|---|---|---|
| Izquierda | Guía / Conceptos / Archivos | Objetivos, progreso, navegación y explicación |
| Centro | Código / Arquitectura / Comparación | Código editable, estructura y diferencias entre variantes |
| Derecha | Paper / Fórmulas / Gráficos | PDF original, derivaciones y resultados |
| Inferior | Ejecución / Logs / Traza | Estado del proceso, métricas y acciones del agente |

Paneles plegables, ampliables y redimensionables; persistencia de posición del paper, pestaña activa y selección del gráfico. En pantallas pequeñas se muestra una región ampliada y se alterna con teclado. Las tareas largas no deben bloquear la navegación.

Propuesta de interacción: Tab para mover foco, Ctrl+P para paleta, una acción para ampliar el panel actual, `/` para buscar en la vista activa y teclas de página para el PDF. Los atajos definitivos se validarán para evitar conflictos con el editor y la terminal.

Los vínculos entre explicación, código y paper serán anclas mantenidas por los autores de las prácticas. Una referencia debe identificar revisión del PDF, página y, si aplica, región o ecuación. No se generarán ubicaciones inventadas a partir de una explicación automática.

### Renderizado

- **Terminal de referencia:** Kitty en Linux para la primera validación visual. Otras terminales se incorporan mediante pruebas de capacidades, sin presumir compatibilidad completa.
- **Gráficos:** Matplotlib genera figuras; un widget de imagen las muestra. Los controles de capa, cabeza, token, escala y zoom pertenecen a la aplicación.
- **Matemáticas:** Mathtext para expresiones compatibles; Tectonic para contenido LaTeX más completo. Caché por fuente, configuración y resolución. Mantener texto fuente copiable y descripción accesible.
- **PDF:** PDFium mediante pypdfium2 renderiza páginas visibles. Navegación, zoom, búsqueda sobre texto extraíble, índice disponible y marcadores. Texto y coordenadas se gestionan además de la imagen; documentos escaneados no son buscables sin OCR.
- **Actualización:** limitar la frecuencia de redibujado; no renderizar un mapa completo por cada token. Los resultados conservarán los datos subyacentes para exportar PNG, SVG, PDF o JSON según el caso.

La TUI ofrecerá inicialmente edición básica de texto y diferencias. Integrar un editor completo o un terminal PTY incrustado requiere una decisión y trabajo específicos; no es una capacidad implícita de Textual. El usuario puede abrir su editor externo, guardar y volver sin perder la sesión.

## 6. Entorno y decisiones técnicas

| Área | Elección inicial | Motivo / validación pendiente |
|---|---|---|
| Lenguaje | Python 3.11+ para la base; validación actual en 3.12.13/Linux | Revalidar compatibilidad al incorporar Textual y PyTorch |
| Dependencias | pyproject.toml y uv.lock; base sin dependencias de ejecución externas | Actualizar el lockfile con uv al resolver las dependencias visuales y de inferencia; no inventar una combinación CUDA |
| CLI | argparse en v0.0.1; servicios independientes de la presentación | Instalación ligera y contrato reutilizable por la futura TUI |
| TUI | Textual + Rich + adaptador de imágenes | Paneles, controles, texto y figuras |
| Motor didáctico | PyTorch, con adaptadores de modelos de Transformers | Exponer operaciones y estado |
| Serving optimizado | vLLM opcional en una fase posterior | Comparación contra un motor existente |
| Gráficos y documentos | Matplotlib, pypdfium2, Tectonic | Renderizado local |
| Persistencia | SQLite para índice/progreso; archivos para artefactos | Simplicidad local y resultados exportables |
| Comunicación | Eventos estructurados entre worker y frontend | La interfaz permanece receptiva |
| Evaluaciones de agentes | Integración opcional con Inspect AI | Reutilizar herramientas existentes después de validar el contrato básico |

El primer objetivo GPU es Linux con NVIDIA/CUDA. Windows con WSL2, acceso por SSH, multiplexores y otras GPU tendrán estado explícito pendiente de validación. No se asume que la terminal de referencia esté disponible nativamente en todos los sistemas.

El comando de diagnóstico debe detectar GPU, VRAM disponible, driver, PyTorch/CUDA, terminal y capacidades gráficas, motores opcionales y espacio para recursos. Los tamaños de descarga y memoria se comprobarán para cada checkpoint; el nombre comercial del modelo no es una medición de memoria.

## 7. Catálogo inicial de modelos

Todos son candidatos, no soporte implementado. Descargar únicamente el modelo elegido. El catálogo guarda el identificador exacto y resuelve una revisión concreta antes de ejecutar.

| Candidato | Identificador inicial | Prácticas previstas | Referencia |
|---|---|---|---|
| TinyStories-1M | `roneneldan/TinyStories-1M` | Generación básica, probabilidades y transformer diminuto sobre historias sencillas en inglés | [TinyStories](https://arxiv.org/abs/2305.07759) |
| Pythia-14M | `EleutherAI/pythia-14m` | Capas, intervenciones, evolución entre checkpoints | [Pythia](https://arxiv.org/abs/2304.01373), [ficha 14M](https://huggingface.co/EleutherAI/pythia-14m) |
| Pythia-70M | `EleutherAI/pythia-70m` | Extensión de interpretabilidad y comparación de tamaños | [Pythia](https://github.com/EleutherAI/pythia) |
| SmolLM2-135M | `HuggingFaceTB/SmolLM2-135M` | Primer laboratorio de serving e inferencia | [Modelo](https://huggingface.co/HuggingFaceTB/SmolLM2-135M), [paper](https://arxiv.org/abs/2502.02737) |
| SmolLM2-135M-Instruct | `HuggingFaceTB/SmolLM2-135M-Instruct` | Base frente a instrucciones y evaluaciones acotadas | [Modelo](https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct) |
| Qwen3-0.6B | `Qwen/Qwen3-0.6B` | Candidato para agentes y herramientas en tareas simples | [Modelo](https://huggingface.co/Qwen/Qwen3-0.6B), [paper](https://arxiv.org/abs/2505.09388) |
| Mamba-130M | `state-spaces/mamba-130m-hf` | Estado recurrente y contraste de mecanismos con atención | [Modelo](https://huggingface.co/state-spaces/mamba-130m-hf), [paper y código](https://github.com/state-spaces/mamba) |

Pythia-14M se incorporó después de la suite original. El paper SmolLM2 centra su descripción en 1.7B. La ficha distinguirá familia, checkpoint y alcance de las afirmaciones. Los sufijos de tamaño son etiquetas; el catálogo contará parámetros reales y detallará su convención.

Cada combinación modelo/motor declara capacidades como `generate`, `prefill_decode`, `activation_hooks`, `checkpoint_replay`, `structural_analysis`, `tool_scenarios` y `optimized_serving`. Para cada capacidad se registra estado experimental/validado, backend, dispositivo y pruebas. La capacidad de generar texto no equivale a soporte de intervenciones ni a capacidad fiable de usar herramientas.

## 8. Familias de laboratorios

| Familia | Ejemplos | Prioridad |
|---|---|---|
| Fundamentos | Tokenización, sampling, logits, máscara causal | Primeras ampliaciones |
| Internals | Cabezas, residuales, activaciones, ablaciones | Primeras ampliaciones |
| Arquitecturas | Atención local, bloques nuevos, posiciones, recurrencia, routing MoE didáctico | Tras estabilizar adaptadores |
| Inferencia | KV cache, cuantización, contexto y batching | Núcleo inicial |
| Serving | Prefill/decode, colas, streaming, chunking, cachés, carga | Demostración principal |
| Evaluación | Datos reservados, métricas, semillas, contaminación y errores de evaluación | Transversal |
| Harnesses | Contexto, reintentos, presupuesto, selección de herramientas y parada | Primer laboratorio con escenarios programados |
| Agentes | Herramientas, memoria, búsqueda local, código y recuperación ante fallos | Ampliación posterior |
| Varios agentes | Delegación, mensajes, coordinación y trabajo duplicado | Posterior, manteniendo mediciones de utilidad y costo |

Una nueva familia no debe obligar a modificar la TUI completa. Los laboratorios declaran vistas, controles y eventos compatibles.

## 9. Laboratorio principal: serving en una GPU

### Objetivo

Levantar un servidor local y estudiar cómo la carga, las fases de inferencia y el scheduler afectan la experiencia de cada solicitud. El modelo inicial propuesto es SmolLM2-135M, sujeto a validación local.

### Fases y estado

**Prefill** procesa la entrada y construye el KV cache. En el flujo autoregresivo habitual, los logits finales permiten seleccionar el primer token. **Decode** incorpora el token generado y usa el estado previo para producir el siguiente. El scheduler admite trabajo y decide su orden.

Estados visibles: `queued`, `prefill`, `decode`, `completed`, `cancelled`, `failed`. Un prefill fragmentado conserva cuánto prompt se ha procesado y sus posiciones. Las iteraciones mixtas registran qué solicitudes y tokens componen el batch.

Separar fases lógicamente no requiere separar GPUs. Dos procesos en una GPU siguen compartiendo recursos; no se presentarán como una demostración de aislamiento físico. La desagregación con recursos dedicados queda como extensión. Una simulación de transferencia debe mostrar su modelo de costos y no producir un benchmark de red ficticio.

### Progresión de prácticas

1. **Una solicitud:** tokenización, prefill, primer token, decode y memoria.
2. **Cola secuencial:** solicitudes simultáneas, espera y streaming.
3. **Batching continuo didáctico:** admitir nuevas solicitudes entre iteraciones y retirar las completadas.
4. **Prefill fragmentado:** comparar prefills completos y fragmentados bajo una carga idéntica.
5. **Presupuesto y caché:** KV cache, prefijos compartidos y límites de admisión.
6. **Motor optimizado:** repetir prácticas compatibles con vLLM y documentar diferencias.

Un motor que recorre solicitudes una por una no se llamará batching continuo hasta que realmente agrupe el trabajo correspondiente. El backend didáctico puede ser menos eficiente; debe exponer con honestidad su ejecución.

### Controles

Longitudes de entrada y salida; concurrencia; ritmo de llegada; semilla de la carga; tamaño máximo del batch; presupuesto de tokens por iteración; prioridad del scheduler; tamaño de fragmento; estado frío/caliente de caché; precisión y presupuesto de memoria cuando el motor lo soporte.

Generar dos tipos de carga: concurrencia fija, donde se repone una solicitud al terminar otra; y llegadas programadas, independientes de las finalizaciones. Registrar la política, porque responden a preguntas distintas. Las longitudes solicitadas deben respetar el contexto real del modelo.

### Métricas y procedencia

| Métrica | Definición operativa |
|---|---|
| TTFT cliente | Desde enviar la solicitud hasta recibir la primera salida no vacía |
| Intervalos de streaming | Tiempo entre fragmentos recibidos; registrar cuántos tokens contiene cada uno |
| Intervalos de tokens servidor | Separación entre eventos de generación de tokens en el motor |
| TPOT por solicitud | Tiempo entre primer y último token dividido por el número de tokens posteriores al primero; indefinido si solo hay uno |
| Cola | Tiempo desde entrada al servidor hasta primera admisión de trabajo |
| GPU prefill/decode | Intervalos de cómputo medidos; indicar alcance de batch o solicitud |
| Throughput de salida | Tokens de salida completados durante una ventana definida por segundo |
| Memoria | GPU disponible, memoria asignada/reservada del framework y estimación/medición separada del KV cache |
| p50 / p95 | Percentiles sobre una población y número de muestras declarados |

TTFT incluye más que prefill. Los eventos del scheduler no son por sí solos mediciones de kernels. El tiempo de un batch no se asigna entero como tiempo exclusivo a cada solicitud. No sumar intervalos solapados como si fueran etapas secuenciales.

El benchmark hace calentamiento y conserva su política de caché. Registra revisión de modelo, software, GPU, precisión, contexto, entradas, semilla, salidas, parámetros y estado térmico/energético si es accesible. Los eventos CUDA se recogen sin una sincronización global por cada token que altere innecesariamente el comportamiento. Se separa modo inspección, con instrumentación rica, de modo benchmark, con sobrecarga acotada y documentada.

### Experimento de referencia

Varias solicitudes cortas generan texto; llega un prompt largo. Comparar latencias y fairness con prefill completo y fragmentado. Reutilizar exactamente el calendario de llegadas y entradas; registrar terminación por EOS o por límite. No prometer una mejora: el usuario interpreta lo que se observa en su laptop.

## 10. Arquitecturas modificables

El adaptador debe exponer carga, configuración, puntos de intervención, formas, estado y capacidades. La interfaz general no asumirá que todos los modelos tienen cabezas o KV cache; Mamba expone estado recurrente mediante su adaptador.

Tres operaciones diferentes:

- **Intervenir:** modificar activaciones o componentes compatibles y medir la salida inmediata.
- **Analizar:** comprobar estructura, número de parámetros y costos estimados sin pesos entrenados; usar operaciones meta cuando sean compatibles.
- **Reproducir:** examinar checkpoints y trazas con procedencia conocida.

Al incorporar un bloque, declarar política de pesos: conservar, transferir con transformación explícita o inicializar. Validar máscara, posiciones, forma de salida, estado y precisión. El soporte de arquitecturas propias en el motor didáctico no implica soporte automático en vLLM.

## 11. Harnesses y agentes

Un harness es el programa que construye contexto, llama al modelo, ejecuta herramientas, administra presupuestos y decide cuándo terminar. El laboratorio registra entrada, salida, estado observable, acciones y errores. No presenta esas trazas como acceso al razonamiento interno del modelo.

Primera práctica: un agente busca un dato en archivos locales, recibe un fallo de herramienta y entra en un bucle. El usuario cambia reintentos, presupuesto o parada y evalúa la recuperación. Primero se valida con respuestas programadas; después con un modelo real capaz de la tarea.

Escenarios: timeout, resultado vacío, JSON inválido, herramienta no disponible, repetición y contexto insuficiente. Métricas: tarea resuelta, llamadas, tokens, pasos, errores, latencia y condición de parada.

Los escenarios serán reiniciables y las herramientas operarán dentro del directorio de la práctica. Para ejecutar código arbitrario de agentes se añadirá un entorno aislado explícito; un subprocess por sí solo no constituye aislamiento. Los ejemplos iniciales no necesitan credenciales ni servicios personales.

## 12. Arquitectura de software

| Componente | Responsabilidad | No debe asumir |
|---|---|---|
| CLI/TUI | Entrada del usuario, vistas y control de tareas | Detalles internos de cada arquitectura |
| Servicio de aplicación | Resolver práctica, recursos y ejecución | Que siempre existe GPU |
| Registro | Modelos, papers, labs y capacidades | Que todos los candidatos están validados |
| Worker | Ejecutar modelo, evaluador o escenario | Que el frontend permanezca conectado |
| Motor didáctico | Prefill, decode, estado e intervenciones | Compatibilidad automática con serving optimizado |
| Adaptador optimizado | Integrar el motor y capacidades disponibles | Telemetría interna que el motor no exponga |
| Renderizadores | Figuras, ecuaciones y páginas | Que la terminal soporte imágenes |
| Almacén de runs | Configuración, eventos, resultados y procedencia | Que un replay sea una ejecución nueva |

Una ejecución tiene ID estable y configuración inmutable. Cada variante nueva produce otro ID, enlazado a su referencia. El frontend recibe eventos por un canal local; los eventos se persisten en JSONL. SQLite guarda índices y progreso; los artefactos grandes permanecen como archivos.

### Contrato de eventos propuesto

Campos comunes: `schema_version`, `run_id`, `sequence`, `event_type`, `evidence_kind`, `timestamp_monotonic_ns`, `request_id` opcional, `batch_id` opcional y `payload`. El reloj monotónico mide duraciones dentro de un proceso/reloj identificado; no restar relojes arbitrarios entre máquinas.

Eventos iniciales: `run.started`, `request.queued`, `request.admitted`, `prefill.started`, `prefill.completed`, `token.generated`, `request.completed`, `request.failed`, `run.completed`. Después: composición de batch, métricas GPU, herramientas y artefactos. Los tiempos GPU se almacenan como mediciones propias, no como timestamps CPU disfrazados.

### Manifiesto de laboratorio propuesto

```yaml
schema_version: 1
id: serving/prefill-decode
version: 0.1.0
title: Observar prefill y decode
language: es
required_capabilities:
  - generate
  - prefill_decode
default_model: smollm2-135m
supported_modes:
  - measured
  - replayed
entrypoint: nimori.labs.serving.prefill_decode:run
guide: guide.md
papers:
  - smollm2
views:
  - request_timeline
  - token_stream
  - memory
checks:
  - output_equivalence
  - event_consistency
```

Este esquema no contiene requisitos de memoria inventados. Se agregarán perfiles medidos antes de declarar la práctica validada. Los paquetes externos son código instalable: registrar versión y procedencia, y no ejecutar automáticamente paquetes desconocidos al abrir un manifiesto.

## 13. Superficie de comandos propuesta

La base v0.0.1 implementa `nimori`, `--help`, `--version`, `doctor`, `models list/info`, `labs list/info`, `papers list/show` y `lab init ID --path DIR`. Las consultas y la preparación admiten `--json`; ayuda y versión son texto. La inicialización rechaza un directorio existente para conservar su contenido; no carga pesos.

Ejemplos **disponibles** después de instalar el starter:

```bash
nimori
nimori doctor --json
nimori models list --capability prefill_decode
nimori models info smollm2-135m
nimori papers show smollm2
nimori labs list --model smollm2-135m
nimori lab init serving/prefill-decode --path my-first-lab
```

La tabla define el resto de la superficie por versión objetivo:

| Versión | Comandos o comportamiento a construir |
|---|---|
| 0.1.0 | `nimori` abre TUI en terminal interactiva; `papers show ID --file PATH` abre el lector de un PDF local |
| 0.2.0 | `models fetch`, `lab open`, `lab run`, `lab check`, `runs list`, `runs replay` |
| 0.3.0 | `serve start`, `load run`, `runs compare` |
| 0.4.0 | `architecture check`, `architecture analyze` |
| 0.5.0 | `trace inspect` |
| 0.6.0 | `plugins validate` |

Los siguientes ejemplos muestran la **API objetivo** del producto. Los comandos nuevos de cada versión no están implementados en v0.0.1:

```bash
nimori doctor
nimori models list
nimori models info smollm2-135m
nimori models fetch smollm2-135m
nimori labs list --model smollm2-135m
nimori lab open serving/prefill-decode --model smollm2-135m
nimori lab init serving/prefill-decode --model smollm2-135m --path my-first-lab
nimori lab run --config lab.yaml
nimori lab check
nimori runs list
nimori runs compare RUN_A RUN_B
nimori runs replay RUN_A
nimori papers show smollm2
nimori architecture check my-block
nimori architecture analyze my-block
```

En las versiones correspondientes, `lab open` abrirá la TUI y `lab run` permitirá ejecución automatizada. La salida JSON se ofrece donde haya datos estructurados. Descargar y ejecutar son acciones separadas y visibles. En v0.0.1 un comando futuro produce un error de argumento; no devuelve una ejecución ficticia.

Los errores de datos u operaciones devuelven código 1; los errores de sintaxis, código 2. Las consultas completadas devuelven 0. El diagnóstico puede completar correctamente y reportar capacidades pendientes: su código de salida no certifica disponibilidad de GPU o imágenes.

## 14. Estructura de repositorio

La base incluye CLI, catálogo, diagnóstico y preparación de directorios. Las rutas de TUI, motor, renderizado y agentes describen la estructura a crear al implementar sus versiones.

| Ruta | Contenido |
|---|---|
| `pyproject.toml` | Proyecto, dependencias y extras |
| `src/nimori/cli.py` | Comandos implementados en la base; pueden dividirse después |
| `src/nimori/catalog.py`, `doctor.py`, `workspace.py` | Servicios iniciales disponibles |
| `src/nimori/tui/` | Layout, paneles y controles |
| `src/nimori/core/` | Contratos, eventos, recursos y ejecución |
| `src/nimori/models/` | Adaptadores e intervenciones |
| `src/nimori/serving/` | Motor, scheduler, carga y métricas |
| `src/nimori/rendering/` | Figuras, matemáticas y PDF |
| `src/nimori/agents/` | Harness, herramientas y escenarios |
| `src/nimori/storage/` | Runs, progreso e índice |
| `src/nimori/data/catalog.json` | Catálogo de planificación incluido en la distribución |
| `labs/` | Prácticas versionadas |
| `tests/` | Contratos y verificaciones de corrección |
| `docs/` | Instalación, arquitectura y contribución |

Separar código del proyecto, recursos descargados y ejecuciones del usuario. No versionar pesos ni resultados grandes dentro del repositorio. Guardar la ubicación elegida y permitir exportar una ejecución completa.

## 15. Roadmap por versiones

Se avanza al cumplir el criterio de salida. Solo v0.0.1 tiene código incluido en esta entrega.

| Versión | Nombre | Entrega | Criterio para cerrar |
|---|---|---|---|
| 0.0.1 | Semilla | CLI, diagnóstico, catálogo y preparación de prácticas | Instalación local y comandos comprobados; sin soporte de modelos declarado |
| 0.1.0 | Destello | TUI con paneles, gráfica, fórmula y PDF local | Navegar, redimensionar y cancelar una tarea de demostración sin bloquear las vistas |
| 0.2.0 | Pulso | Una inferencia real con SmolLM2-135M y fases explícitas | Equivalencia con referencia, eventos persistidos, gráfica y replay etiquetado |
| 0.3.0 | Flujo | Carga, cola y prefill fragmentado | Comparación reproducible entre políticas; máscaras, posiciones y caché correctas |
| 0.4.0 | Lupa | Pythia e intervenciones; análisis de un bloque nuevo | Modificación observable y estimaciones con supuestos; pesos nuevos identificados |
| 0.5.0 | Brújula | Harnesses y agente local | Recuperación ante fallo programado y evaluación en escenario nuevo; luego prueba con modelo real |
| 0.6.0 | Constelación | Extensiones, Mamba y adaptador vLLM opcional | Práctica añadida por contrato y capacidades comprobadas por backend |

Los hitos técnicos originales se conservan: M0 = v0.1.0; M1 = v0.2.0; M2 = v0.3.0; M3 = v0.4.0; M4 = v0.5.0; M5 = v0.6.0. La primera sesión usable sobre un modelo corresponde a v0.2.0. El MVP de comparación de serving se cierra en v0.3.0.

PDF básico, una fórmula, una gráfica y paneles llegan en v0.1.0. Tectonic completo, búsqueda PDF, marcadores, zoom fino, selección precisa de texto y editor avanzado se agregan como incrementos posteriores. La demostración visual inicial no depende de cargar un modelo ni de tener GPU.

## 16. Backlog inicial y aceptación

El siguiente listado conserva los requisitos técnicos del diseño original. El backlog ejecutable por versión está en `docs/ROADMAP.md`: NIM-101 a NIM-107 para paneles y renderizado; NIM-201 a NIM-206 para la primera inferencia. A01 tiene una implementación preliminar en v0.0.1; certificación gráfica y prueba CUDA se completan en sus versiones correspondientes.

| Ticket | Entregable | Aceptación |
|---|---|---|
| A01 | Diagnóstico local | Reporta entorno real y no descarga modelos al inspeccionar |
| A02 | TUI base | Paneles navegables; worker lento no congela la UI |
| A03 | Renderizadores | Una figura, una ecuación y una página PDF se ven correctamente y se redimensionan |
| A04 | Registro de modelos | Ficha SmolLM2 con revisión resuelta y capacidades explícitas |
| A05 | Prefill/decode | Logits/tokens concuerdan con una referencia bajo condiciones controladas |
| A06 | Eventos y almacenamiento | Run puede reabrirse; orden, errores y cancelación son coherentes |
| A07 | Métricas | TTFT cliente y GPU se distinguen; casos de cero/uno tokens se manejan |
| A08 | Primera guía | Explicación, código, paper y observación están vinculados |
| A09 | Carga y cola | Calendario reproducible; solicitudes canceladas liberan estado |
| A10 | Prefill fragmentado | Cache, posiciones y logits finales coinciden con prefill completo dentro de tolerancia |
| A11 | Comparación | Expone cambios de configuración, población de métricas y procedencia |

La prueba de equivalencia usa evaluación, mismo tokenizer, pesos, precisión y entrada. Primero compara logits con tolerancia numérica; luego generación greedy. No exigir igualdad bit a bit entre kernels o hardware diferentes. Para chunking, comprobar máscaras, posiciones y estado, no solo que el texto parezca razonable.

Validación visual manual en Kitty: abrir, desplazar, ampliar, alternar pestañas y cerrar paneles con imágenes. Validación GPU en el equipo objetivo: calentamiento, memoria, cancelación y variación entre repeticiones. No fijar cifras universales de velocidad antes de medir.

## 17. Primera sesión al llegar a casa

**Objetivo inmediato:** instalar la base, confirmar el diagnóstico y comenzar v0.1.0. El proyecto ya contiene el ejecutable y el catálogo; el siguiente trabajo es construir los paneles.

1. Entra en la raíz del repositorio Nimori, donde está `pyproject.toml`; el starter ya está integrado.
2. Crea el entorno con `uv sync --locked`. `.python-version` selecciona Python 3.12; el paquete declara Python 3.11+.
3. Ejecuta el diagnóstico, consulta el catálogo y prepara una práctica.
4. Abre `docs/FIRST_VERSION_TASK.md` y construye los tickets NIM-101 a NIM-107.
5. Comprueba una sesión visual con un PDF local, una fórmula y una figura; luego avanza a v0.2.0 para añadir el modelo.

Linux, macOS, WSL o Windows PowerShell, desde la raíz del repositorio:

```bash
uv sync --locked
uv run nimori
uv run nimori doctor
uv run nimori models list
uv run nimori papers show smollm2
uv run nimori lab init serving/prefill-decode --path my-first-lab
uv run python -m unittest discover -s tests -v
```

Estos comandos corresponden a la base v0.0.1 y no requieren activar el entorno. La instalación puede descargar Python y la herramienta de empaquetado; después puedes usar `uv run --offline nimori`. No instales un paquete por nombre desde PyPI esperando encontrar esta entrega: el proyecto aún no está publicado.

La base está comprobada con Python 3.12.13/Linux. Las instrucciones para otros sistemas son rutas de inicio, no certificación de compatibilidad. En una laptop NVIDIA, valida primero qué entorno y terminal utilizarás. Windows/WSL y el renderizado gráfico necesitan una comprobación específica. El diagnóstico reporta pistas, no una aprobación automática del entorno.

### Encargo de implementación para la siguiente versión

```text
Continúa Nimori desde la base v0.0.1 incluida. Lee README.md,
docs/SPEC.md, docs/BRAND.md y docs/ROADMAP.md, además de las
instrucciones existentes en el repositorio.

Implementa v0.1.0 (Destello), tickets NIM-101 a NIM-107:
Python + Textual; panel izquierdo de guía, centro de código,
panel derecho con pestañas Paper/Fórmulas/Gráficos y zona de logs.
Añade una figura Matplotlib, una fórmula Mathtext y un lector
básico de un PDF local con pypdfium2 y protocolo gráfico compatible.

Reutiliza el catálogo y los servicios existentes. Conserva el
comando nimori y las consultas JSON. Un worker separado emitirá
eventos de demostración scripted; la navegación seguirá respondiendo
y se podrá cancelar. Los datos de demostración se identifican.

Detecta el entorno real; valida foco, pestañas, redimensionado,
imágenes y navegación PDF en la terminal de referencia disponible.
Resuelve y fija dependencias comprobadas. Documenta cualquier QA
que el entorno no permita completar. No declares inferencia ni
compatibilidad GPU a partir de una simulación o una detección de driver.

Actualiza README, versión y CHANGELOG con lo que funciona.
La inferencia SmolLM2-135M con prefill/decode pertenece a v0.2.0.
```

`docs/FIRST_VERSION_TASK.md` contiene el encargo ampliado. `docs/ROADMAP.md` define dependencias y aceptación. La próxima sesión puede comenzar directamente con esos archivos.

## 18. Fuentes técnicas y precedentes

Las siguientes fuentes respaldan mecanismos o herramientas; las decisiones de producto y los criterios de aceptación anteriores son propuestas propias. Las versiones deben fijarse y comprobarse al construir.

| Fuente | Uso en Nimori |
|---|---|
| [AWS Builder Labs](https://aws.amazon.com/training/digital/immersive-learning/) | Referente de prácticas guiadas |
| [ARENA](https://github.com/callummcdougall/ARENA_3.0) | Referente de profundidad educativa y ejercicios |
| [TransformerLens](https://transformerlensorg.github.io/TransformerLens/) | Intervenciones e inspección de activaciones |
| [PyTorch meta](https://docs.pytorch.org/docs/stable/meta.html) | Análisis estructural sin valores de tensores |
| [PyTorch CUDA Events](https://docs.pytorch.org/docs/stable/generated/torch.cuda.Event.html) | Medición de trabajo en GPU |
| [Empaquetado Python](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) | Distribución instalable y ejecutable definido en pyproject.toml |
| [Textual layouts](https://textual.textualize.io/guide/layout/) y [TabbedContent](https://textual.textualize.io/widgets/tabbed_content/) | Paneles y pestañas |
| [Kitty graphics](https://sw.kovidgoyal.net/kitty/graphics-protocol/) y [textual-image](https://github.com/lnqs/textual-image) | Imágenes en terminal |
| [Mathtext](https://matplotlib.org/stable/users/explain/text/mathtext.html) y [Tectonic](https://tectonic-typesetting.github.io/) | Fórmulas y LaTeX |
| [pypdfium2](https://github.com/pypdfium2-team/pypdfium2) | Lector PDF integrado |
| [vLLM serve](https://docs.vllm.ai/en/stable/cli/serve/) | Controles de batching y prefill fragmentado |
| [vLLM benchmarking](https://docs.vllm.ai/en/stable/benchmarking/cli/) | Definiciones y medición de latencia |
| [vLLM metrics](https://docs.vllm.ai/en/latest/design/metrics/) | Telemetría interna |
| [vLLM disaggregated prefill](https://docs.vllm.ai/en/latest/features/disagg_prefill/) | Alcance de desagregación física |
| [Inspect AI agents](https://inspect.aisi.org.uk/agents.html) y [sandboxing](https://inspect.aisi.org.uk/sandboxing.html) | Evaluación de agentes y ejecución aislada |

## 19. Decisiones abiertas que no bloquean el inicio

Nimori, su comando y la licencia MIT del código original quedan elegidos para iniciar. Permanecen abiertas la publicación/disponibilidad del paquete, compatibilidad adicional de terminales, editor avanzado, tutor opcional, formato definitivo de extensiones y rendimiento mínimo por práctica una vez medido. Las revisiones y condiciones de modelos, datos y papers se registrarán al incorporarlos.

El historial del documento pasa de una especificación conceptual a una identidad concreta, una base de código y entregables por versión. La revisión 0.2 del documento no significa que exista el producto v0.2.0.

**Definición de primera demostración exitosa:** desde una laptop con GPU y terminal compatible, abrir una práctica, leer su paper en un lateral, ver su fórmula, ejecutar un modelo pequeño, observar prefill y decode, comparar un resultado y reabrir la sesión conservando su procedencia.
