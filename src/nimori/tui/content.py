"""Contenido editorial local para la primera estructura de la TUI."""

GUIDE = """\
# Observar prefill y decode

**Vista preliminar · sin inferencia**

## Pregunta

¿Qué trabajo ocurre antes de producir el primer token y qué estado se reutiliza después?

## Secuencia de la práctica

1. Lee la pregunta y anota una predicción.
2. Inspecciona el código de referencia.
3. Relaciona cada operación con la fórmula y el paper.
4. Ejecuta una referencia cuando el motor esté disponible.
5. Cambia una pieza y explica la diferencia observada.

> Cambia una pieza. Predice qué pasará.

Esta pantalla establece la navegación del laboratorio. El worker, las figuras,
el lector PDF y la inferencia se incorporan en módulos posteriores.
"""

CODE_SAMPLE = '''\
def decode_step(token, cache, model):
    """Esquema didáctico; no ejecuta un modelo."""
    hidden = model.embed(token)
    output, next_cache = model.forward_step(hidden, cache)
    return output, next_cache
'''

PAPER_PLACEHOLDER = """\
SmolLM2: When Smol Goes Big

Estado: referencia bibliográfica local; visor PDF pendiente (NIM-105).

La ficha distingue la familia SmolLM2 del checkpoint candidato de 135M.
Usa `nimori papers show smollm2` para consultar los enlaces registrados.
"""

FORMULA_PLACEHOLDER = """\
Fuente prevista para Mathtext (NIM-104):

    Attention(Q, K, V) = softmax(QKᵀ / √dₖ) V

Q: consultas · K: claves · V: valores · dₖ: dimensión de las claves

Esta vista conserva texto copiable. Todavía no presenta una imagen renderizada.
"""

CHART_PLACEHOLDER = """\
Gráfico de demostración pendiente (NIM-104)

La figura mostrará datos locales identificados como `scripted` y conservará
sus valores de origen. Esta pantalla no contiene mediciones de GPU.
"""
