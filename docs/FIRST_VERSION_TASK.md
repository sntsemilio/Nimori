# Encargo listo: Nimori v0.1.0, Destello

Continúa este repositorio de Nimori. Lee README.md, docs/SPEC.md, docs/BRAND.md y docs/ROADMAP.md, además de las instrucciones locales existentes. El paquete incluye una CLI v0.0.1 funcional: consérvala y reutiliza sus servicios y catálogo.

Construye una interfaz visual dentro de la terminal con Python y Textual. El objetivo es abrir Nimori y ver simultáneamente una guía, un archivo de código, una referencia y los eventos de ejecución. Agrega pestañas laterales para paper, fórmulas y gráficos. Permite ampliar el panel actual para pantallas pequeñas.

Implementa los tickets NIM-101 a NIM-107. Usa Matplotlib/Mathtext para una figura y una fórmula; utiliza pypdfium2 y un adaptador de imágenes para un PDF local. La página debe poder cambiarse y ajustarse al ancho. No abras un navegador como requisito del flujo.

Un worker separado emitirá eventos de demostración `scripted`; muéstralos sin congelar la TUI y permite cancelar. Las imágenes y datos de demostración deben estar etiquetados. No presentes una espera artificial como tiempo de GPU. Mantén las operaciones largas fuera del hilo de interfaz y cierra sus recursos al salir.

Inspecciona el sistema real. La primera referencia visual es Linux con Kitty, pero detecta capacidades: no presupongas que Windows, WSL, SSH o un multiplexor renderizan imágenes. Si no puedes comprobar una terminal gráfica, termina las partes verificables y documenta qué QA visual queda pendiente. No declares que una captura o un test sin terminal certifica el protocolo gráfico real.

Al introducir dependencias, resuélvelas con `uv add` y actualiza el `uv.lock` existente. La CLI, las consultas JSON y el catálogo deben seguir disponibles. El entry point seguirá llamándose `nimori`, y el paquete Python `nimori`. Usa la voz de BRAND.md en guías y bienvenida; conserva los datos técnicos sin adornos.

Valida foco, pestañas, redimensionado, dibujo de imagen, navegación PDF, cancelación y comportamiento sin imágenes. Prueba únicamente los contratos y riesgos de esta entrega. Actualiza versión, README y CHANGELOG con comandos reales y límites observados.

La entrega siguiente, v0.2.0, añadirá SmolLM2-135M y prefill/decode. Para cerrar v0.1.0 basta con contenido local y un worker de demostración claramente identificado. El catálogo completo, GPU, vLLM, agentes y entrenamiento no son requisitos de esta entrega.
