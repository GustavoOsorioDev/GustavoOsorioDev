# SETUP IDE — Contract-First Spec-Driven Development (CSDD)
# Gustavo Osorio — @GustavoOsorioDev
# Última actualización: 2026-06-18

---

## DECISIÓN TOMADA (no reabrir)

**Stack elegido:** VS Code + Cline (agente autónomo)

**Razón:** No es la opción más fácil, pero sí la más correcta para el canal.
Cursor y Windsurf son cajas negras. Con Cline, el agente razona en voz alta, muestra el costo por tarea en dólares y expone el flujo de contexto. Eso es contenido educativo de alta calidad, no magia escondida.

### 3. Setup de Kaggle (Inferencia Gratuita)
Video temático: "Ingeniero de Software por $0.00".
- **Notebook:** GPU dual T4 recomendado.
- **Script de automatización:** Ver `estrategia/SCRIPTS_KAGGLE.py`.
- **Modelo:** Qwen2.5-Coder-32b (Quantized).
- **Túnel:** ngrok.

---

## 1. EXTENSIONES DE VS CODE (ordenadas por prioridad)

### Tier 1 — Core del stack CSDD

| Extensión | Rol | Por qué, no otra |
|---|---|---|
| **Cline** | Agente autónomo principal | Muestra razonamiento, costo, tokens en tiempo real. Indispensable para el canal. |
| **Continue.dev** | Chat + autocompletado desacoplado | Conecta a cualquier modelo (local o cloud). Sin lock-in de proveedor. |

### Tier 2 — Soporte para el canal

| Extensión | Rol |
|---|---|
| **GitLens** | Visualización de historial, autoría y blame. Narrativa de "commits por spec completada". |
| **Error Lens** | Muestra errores inline — error visible en cámara sin hacer zoom a la consola. |
| **Mermaid Preview** | Renderizar diagramas de arquitectura (`.specs/diagrama_flujo.md`) en vivo. |

### Tier 3 — Consideradas, descartadas para arranque

| Extensión | Razón del descarte |
|---|---|
| Roo Code | Fork de Cline. Útil para specs >50 páginas. No aplica en EP01-EP03. Revisar en EP04. |
| GitHub Copilot | Costoso, black-box, no muestra tokens. Contradice la narrativa del canal. |

---

## 2. LAYOUT DE VS CODE PARA GRABACIÓN EN 1080p/4K

El layout no es estético. Es narrativo. La audiencia debe ver la jerarquía:
**Las specs mandan. El código obedece.**

```
┌─────────────────┬─────────────────┬─────────────────┐
│  COLUMNA IZQ    │  COLUMNA CENTRO │  COLUMNA DER    │
│                 │                 │                 │
│  .specs/        │  src/main.py    │  Cline          │
│  01_data_       │  (código que    │  (agente        │
│  contract.md    │   la IA genera  │   razonando,    │
│                 │   o modifica)   │   costo visible)│
│  ← El Jefe →    │                 │                 │
└─────────────────┴─────────────────┴─────────────────┘
│                  TERMINAL (abajo)                   │
│  $ python src/main.py → output en Rich              │
└────────────────────────────────────────────────────-┘
```

**Reglas de grabación que surgen del layout:**
- Las specs SIEMPRE visibles a la izquierda. Si las cierras, no se entiende el video.
- El panel de Cline muestra el `$cost` acumulado. Nunca ocultar ese número.
- La terminal debe mostrar output de Rich (tablas, colores). Ajustar tamaño de fuente a 14px mínimo para cámara.

---

## 3. CONFIGURACIÓN DE CLINE (System Prompt Base CSDD)

Este System Prompt va en: `Cline → Settings → Custom Instructions`

```markdown
# IDENTIDAD
Eres un junior engineer que trabaja bajo la supervisión estricta de un
arquitecto senior. Tu única fuente de verdad es el archivo de contratos
ubicado en `.specs/`. No asumas tipos de datos, nombres de funciones
ni comportamientos que no estén explícitamente definidos en ese archivo.

# PROTOCOLO OBLIGATORIO
1. Antes de escribir CUALQUIER línea de código, leer `.specs/01_data_contract.md`.
2. Si el contrato no define algo, DETENTE y pregunta. No inventes.
3. Prohibido usar `any`, tipos sin anotación, o casteos sin validación previa.
4. Toda función que mutate estado debe ser pura: recibe primitivas, devuelve resultado.
5. Si hay un error en ejecución, reportarlo completo. Nunca silenciar un `except`.

# LO QUE NUNCA HARÁS
- Asumir rutas de archivo. Usa siempre rutas absolutas desde el contexto dado.
- Escribir código que no tenga un ítem correspondiente en `tasks.md`.
- Cambiar la arquitectura sin aprobación del humano.
- Usar `innerHTML` para datos de usuarios o APIs.
- Dejar un `except: pass` en código de producción.

# FORMATO DE RESPUESTA
Siempre declara qué archivo estás modificando antes de hacerlo.
Siempre reporta el costo estimado de tokens antes de la ejecución masiva.
```

---

## 4. CONFIGURACIÓN DE CONTINUE.DEV (config.json)

Ruta: `%USERPROFILE%\.continue\config.json`

```json
{
  "models": [
    {
      "title": "Claude Sonnet (Cloud — Principal)",
      "provider": "anthropic",
      "model": "claude-sonnet-4-5",
      "apiKey": "TU_KEY_ANTHROPIC"
    },
    {
      "title": "Qwen2.5-Coder 7B (Local — RTX 4060)",
      "provider": "ollama",
      "model": "qwen2.5-coder:7b",
      "apiBase": "http://localhost:11434"
    },
    {
      "title": "Qwen2.5-Coder 32B (Kaggle — Gratuito)",
      "provider": "ollama",
      "model": "qwen2.5-coder:32b",
      "apiBase": "PEGAR_URL_NGROK_AQUI"
    }
  ],
  "contextProviders": [
    {"name": "file"},
    {"name": "code"},
    {"name": "docs"}
  ],
  "slashCommands": [
    {
      "name": "spec",
      "description": "Inyectar contrato de datos antes de cualquier tarea",
      "prompt": "Lee el archivo .specs/01_data_contract.md completamente antes de proceder."
    }
  ]
}
```

---

## 5. SETUP KAGGLE + QWEN-CODER (Para el video "SDD $0.00")

> **ADVERTENCIA OPERACIONAL:**
> Las sesiones de Kaggle tienen timeout (máx. ~9h). Si grabas en vivo
> y la sesión muere, pierdes el modelo y la toma.
> Este setup es para el VIDEO ESPECÍFICO del modelo gratuito, no para
> el día a día de producción.

### Celdas del Notebook Kaggle (orden exacto):

```bash
# Celda 1: Instalar Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Celda 2: Levantar servidor en background
ollama serve &
sleep 5

# Celda 3: Descargar modelo (elegir según GPU disponible)
# Con T4 (15GB VRAM) -> 7B
# Con P100 (16GB VRAM) -> 14B
ollama pull qwen2.5-coder:7b

# Celda 4: Instalar ngrok y crear túnel
pip install pyngrok -q
from pyngrok import ngrok
ngrok.set_auth_token("TU_TOKEN_NGROK")  # Token gratuito en ngrok.com
tunnel = ngrok.connect(11434, "http")
print(f"URL pública: {tunnel.public_url}")
# Pegar esta URL en Continue.dev config → apiBase
```

### Alternativa recomendada para el día a día: Qwen local

Con las GPUs disponibles en el setup (RTX 3060 Ti + 4060 + 2000 Ada),
correr Qwen localmente es más estable para producción:

```bash
# RTX 4060 (8GB VRAM) → Qwen2.5-Coder 7B en Q4
ollama run qwen2.5-coder:7b
# Latencia ~15-20 tokens/seg. Suficiente para demostraciones en cámara.
```

---

## 6. NARRATIVA DE COSTOS PARA EL CANAL

El medidor de costo de Cline es un personaje del canal, no un detalle técnico.

| Escenario | Costo estimado | Narrativa |
|---|---|---|
| Vibe Coding: "Hazme un bot de Reddit" sin specs | $3-8 por tarea | La IA da vueltas, regenera, alucina imports |
| CSDD: Cline + contrato `.specs/` inyectado | $0.15-0.40 por tarea | Una sola corrida, directa al grano |
| Qwen-Coder 7B local | $0.00 | Contraargumento al "la IA es cara" |

**Línea de guión sugerida para el video:**
> "Ven este número. Cuatro dólares. Eso costó ese loop infinito de prompts.
> Ahora miran esto: le paso el contrato. Una sola llamada. Veinte centavos.
> Esta es la diferencia entre vibe coding e ingeniería real."

---

*Gustavo Osorio — @GustavoOsorioDev*
*"Ingeniería real. Sin vibes."*
