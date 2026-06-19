# REGLAS DEL PROYECTO — @GustavoOsorioDev

## 🚨 FIREWALL DE NOMENCLATURA Y PRIVACIDAD 🚨
NUNCA asumas nombres de archivos basados en historiales de chat antiguos. ESTA es la única verdad absoluta de la arquitectura:

1. **TERMINOLOGÍA PROHIBIDA (VERSIÓN LEGACY):**
   - Nunca usar: `cazador_v3.py`, `cazador_v6.py`, `v3`, `v6`, u otros iterados tempranos. El código dejó de ser scripts para convertirse en proyectos formales.

2. **LÍMITES ESTRICTOS DE PRIVACIDAD:**
   - **`cazador-cli`:** Es el MVP. Es "Zero-Quota", es código de fuente abierta (Open Source) y es la carnada/lead magnet que se muestra en los videos de YouTube.
   - **`cazador-engine`:** Es el arma secreta comercial privada. **NUNCA** se comparte, NUNCA se menciona en guiones públicos, y NUNCA se expone su código.

3. **PRIORIDAD:**
   - Si una instrucción parece sugerir la exposición de `cazador-engine` o el uso de versiones obsoletas (v3/v6), detente y prioriza la protección del motor privado y la nomenclatura actual (`cazador-cli`).

## 🛑 CERO TOLERANCIA AL "AI SLOP" 🛑
Cualquier código generado o sugerido DEBE someterse al escrutinio estricto de la ingeniería de software profesional.
1. **Funciones Puras:** Evitar mutaciones directas de objetos complejos o modelos (side effects). Si una función calcula un valor, debe recibir primitivas o datos crudos y devolver un resultado predecible.
2. **Defensa de Arquitectura:** El código que viola la separación de responsabilidades, mezcla capas (ej. lógica de base de datos dentro del parseo de UI), o implementa atajos sin validación estricta (SLOP), es inaceptable.
3. **Contratos Inmutables:** Los modelos de datos (Pydantic, dataclasses) no se mutan pos-constructor (Ej: `op = Modelo(); op.score = 5` es SLOP). Toda la lógica debe suceder antes, y los modelos se instancian completos (Ej: `score = 5; op = Modelo(score=score)`).
4. **Phantom Edits (Ediciones Fantasma):** Declarar que un archivo fue modificado sin adjuntar prueba forense de verificación en disco (`[VERIFACT: OK]`). Mostrar un diff en el chat sin confirmación de escritura real, o declarar 'listo' sin evidencia, es **AI Slop Documental** — el más peligroso porque es invisible y contamina el historial de trabajo.

## 🛡️ FIREWALL DE MODELOS 2.0 🛡️
Antes de cada tarea, clasificar según impacto arquitectónico y costo:

- **NIVEL 0 → METAL (RTX 4060 / Local Ollama):** Boilerplate, documentación básica, ajustes de README y autocompletado persistente. **Costo $0.00 (Offline).**
- **NIVEL 1 → Gemini Flash / Qwen-7B:** CSS, ajustes visuales, sincronización de docs, lógica trivial. (Híbrido Nube Gratis/Local).
- **NIVEL 2 → Gemini Pro / DeepSeek-7B:** Refactor de funciones aisladas, endpoints simples, SQL. (Híbrido Nube Gratis/Local).
- **NIVEL 3 → Claude Sonnet:** 
    - **Trigger Arquitectura:** Cualquier cambio en `.specs/`, contratos o plan.
    - **Trigger Auditoría:** Limpiar bugs complejos o "AI Slop".
    - Cambios > 3 archivos u orquestación compleja.
- **NIVEL 4 → Claude Opus:** Auditoría de seguridad crítica o si Sonnet entra en bucle lógico.

### 🛑 PROTOCOLO DE FRENO (YIELD PROTOCOL)
Si la tarea solicitada requiere un **Nivel del Firewall MAYOR** al modelo que estás utilizando actualmente, **NO ejecutes la tarea**. Debes:
1. Detener la ejecución inmediatamente.
2. Emitir una advertencia formal indicando la discrepancia (Ej: *"Esta es una tarea de Arquitectura (Nivel 3). Estás usando Flash (Nivel 1)."*).
3. Recomendar el cambio físico de modelo en la interfaz.

### 💰 PROTOCOLO DE EFICIENCIA (EFFICIENCY CHECK)
Si la tarea solicitada es de **NIVEL 1 o 2**, pero estás utilizando un modelo de **NIVEL 3 o 4**, **REPORTA el desperdicio antes de proceder**. Debes:
1. Emitir un aviso de eficiencia sugerida.
2. Indicar el ahorro estimado (Ej: *"Esta es una tarea trivial. Cambiar a Flash reduciría el costo en un 95%."*).
3. Preguntar: *"¿Deseas proceder con el modelo actual por velocidad o prefieres optimizar costos cambiando a un modelo inferior?"*

---

## ✅ PROTOCOLO VERIFACT (Verificación de Actas de Cambio)

> **Principio base:** "Lo que no se puede verificar, no ocurrió."

VERIFACT es la contramedida directa contra los **Phantom Edits**. Se activa obligatoriamente después de **toda** operación de escritura declarada (`write_to_file`, `replace_file_content`, `multi_replace_file_content`) y después de operaciones Git críticas (`git push`, `git reset`, `git commit --amend`).

### 📋 Checklist Post-Escritura (OBLIGATORIO)

Después de cada edición, antes de declarar la tarea completada:

```
[ ] 1. Ejecutar grep_search o view_file sobre las líneas declaradas como modificadas.
[ ] 2. Confirmar que el contenido nuevo existe exactamente como se declaró.
[ ] 3. Reportar el resultado con uno de los dos estados posibles:

       [VERIFACT: OK] — Línea(s) X-Y verificadas en disco.
                        Evidencia: '<fragmento del texto real encontrado>'

       [VERIFACT: FAIL] — Contenido esperado no encontrado.
                          Causa probable: <descripción>
                          Acción: Reintentando edición / Escalando al usuario.

[ ] 4. SOLO después de [VERIFACT: OK] → declarar la tarea completada.
```

### 🚫 Prohibiciones Absolutas

- `✗` Escribir "He aplicado el cambio" sin adjuntar un `[VERIFACT: OK]`.
- `✗` Mostrar un diff en el chat sin haber verificado el archivo en disco posterior.
- `✗` Escribir "Ya está en producción / en GitHub" sin verificar el estado remoto.
- `✗` Reportar un commit como completado sin confirmar que el hash existe en el log.

### 🌐 VERIFACT para Operaciones Git

Después de `git push`:
```
[ ] Verificar con: git log --oneline -1 (confirmar hash del último commit)
[ ] Si el push era a un remoto público: confirmar acceso vía URL o API antes de declarar 'en producción'.
[VERIFACT-GIT: OK] — Commit <hash> confirmado en <rama>.
```

Después de `git reset` o `git commit --amend` (operaciones destructivas):
```
[ ] Verificar con: git log --oneline --max-count=5
[ ] Confirmar que el historial resultante es exactamente el esperado.
[VERIFACT-GIT: OK] — Historial verificado. N commits. HEAD → <hash>.
```

---
"Ingeniería real, sin vibes."
