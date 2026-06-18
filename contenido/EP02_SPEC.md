# SPEC — EP02: "Conecté una RTX 4060 a mi Bot de Reddit (V4)"
# Gustavo Osorio — @GustavoOsorioDev
# Última actualización: 2026-06-18
# Estado: EXPLORACIÓN TÉCNICA

---

## INTENCIÓN (PROMPT.md)

**El problema (Gap del EP01):**
El bot del EP01 usa Regex y RSS. Es rápido, pero "tonto". Clasifica como "dolor" posts que son solo quejas de soporte técnico o chistes, contaminando mi base de datos de nichos. El vibe coding intentaría arreglar esto con 500 líneas de `if/else`. Nosotros usaremos inferencia local.

**La solución:**
Integrar un LLM local (Qwen2.5-Coder o Llama 3) corriendo en la RTX 4060 para actuar como un "Filtro de Seniority". El LLM leerá el post y decidirá: "¿Esto es un problema de negocio real o solo ruido?".

---

## CONTRATO (SPEC.md)

### Audiencia objetivo
- El Constructor Solo que busca máxima precisión sin pagar APIs de OpenAI/Anthropic.
- Entusiastas del hardware que quieren ver su GPU trabajando en desarrollo real.

### Definition of Done del video
- [ ] Refactor del script de `cazador-cli` a v4 (Modular: Local LLM enabled).
- [ ] Demostración en vivo de la latencia vs precisión (RTX 4060 vs CPU).
- [ ] El bot filtra con éxito ≥ 90% de los falsos positivos detectados en el EP01.
- [ ] La base de datos guarda el "Razonamiento del LLM" para demostrar transparencia.

---

## ARQUITECTURA DEL VIDEO

### Gancho (0:00 - 0:45)
Muestro la base de datos del EP01 llena de basura. "El bot del video pasado es bueno, pero le falta cerebro. Hoy vamos a darle uno." Zoom a la RTX 4060 en el setup. "Inferencia local al servicio de la arquitectura."

### Sección 1 — El "Slop" de Regex (0:45 - 3:00)
- Mostrar ejemplos reales de posts que el Regex dejó pasar.
- Explicar por qué escalar con Regex es una deuda técnica infinita.

### Sección 2 — Setup del "Cerebro" (vLLM / Ollama) (3:00 - 6:00)
- Instalación rápida del motor de inferencia.
- Selección del modelo: ¿Por qué Qwen2.5-Coder es el junior ideal para este filtro?
- El contrato Pydantic para la respuesta del LLM (Structured Output).

### Sección 3 — El Refactor de Seniority (6:00 - 10:00)
- Inyectar el agente Cline en VS Code para que realice la integración.
- **Narrativa CSDD:** "No le pedimos que 'use el modelo', le pasamos el contrato de cómo queremos que el modelo clasifique".

### Sección 4 — Resultados y Hardware Performance (10:00 - 13:00)
- Ejecución final.
- Comparativa de consumo de VRAM y velocidad.
- "Costo por inferencia: $0.00. El hardware ya está pagado."

---

## CHECKLIST DE PRODUCCIÓN

- [ ] Instalar Ollama/vLLM y verificar que la RTX 4060 sea reconocida.
- [ ] Crear el objeto `OportunidadMejorada` en Pydantic (incluye campo `analisis_semantico`).
- [ ] Grabar B-roll de la tarjeta de video con luces teal si es posible.
- [ ] Preparar 3-4 posts de "ruido" que el bot viejo aceptaba y el nuevo rechaza.

---

*Gustavo Osorio — @GustavoOsorioDev*
*"Ingeniería real. Sin vibes."*
