# WORKFLOW DE GRABACIÓN: "MODO DIRECTOR" (BUILD IN PUBLIC)
**Ubicación:** Central de Operaciones `@GustavoOsorioDev`
**Objetivo:** Establecer el protocolo exacto para grabar sesiones de código refactorizando con IA, destruyendo el mito del "programador mecanógrafo" y posicionándote como el Arquitecto/Tech Lead.

---

## CONTEXTO Y FILOSOFÍA DE CÁMARA
El objetivo visual no es el código apareciendo mágicamente de la nada. El objetivo visual es **el control sobre el sistema**. 
La audiencia debe ver la fricción real, los fallos de la IA y cómo un Senior los mitiga mediante contratos estrictos y revisión humana.

---

## ESTRUCTURA DE LA SESIÓN DE GRABACIÓN (5 FASES)

### FASE 1: El Tablero de Mando (El "Qué" y el "Por qué")
*Nunca empieces grabando el IDE vacío.*
1. **Pantalla:** Abre tu esquema de arquitectura (`plan.md`) o tu archivo de especificaciones (`spec.md` / `contracts.md`).
2. **Narrativa:** "Esta es la arquitectura. Necesito refactorizar este componente. No voy a escribir esto de cero porque no estamos en 2018. Voy a delegar la carpintería pesada al agente Cline, pero bajo **mis reglas**."
3. **Acción:** Muestra brevemente las restricciones que has definido (ej. "Tercera regla: Cero llamadas a APIs externas sin un manejador de errores Pydantic").

### FASE 2: El Despacho (De Tech Lead a Junior)
*Muestra la interfaz del LLM (Claude, Cursor, Antigravity) como tu terminal de comandos.*
1. **Pantalla:** El chat de la IA incrustado en el IDE o a un lado (preferiblemente Cline con el medidor de costo visible).
2. **Narrativa:** "Aquí es donde la mayoría falla. Piden 'hazme un bot'. Yo le paso el contrato de datos."
3. **Acción:** Escribes o pegas el prompt en vivo. Utilizas el comando adecuado (`@` o slash) para inyectar los archivos de contexto (`contracts.md`, `spec.md`) y haces hincapié: *"Le estoy inyectando el contrato Pydantic para que no alucine los tipos de datos."*
4. **Disparo:** Envías el prompt. Dejas que la máquina genere el código a máxima velocidad.

### FASE 3: El Choque con la Realidad (Donde la magia falla)
*El momento más crítico para generar autoridad. La IA siempre se equivoca en sistemas complejos.*
1. **Pantalla:** El código generado por la IA en la pantalla.
2. **Narrativa:** "Vale, la máquina nos escupió 150 líneas en cinco segundos. Se ve bonito, ¿verdad? **Pero está mal.**"
3. **Acción:** Haces zoom a una línea específica. 
   - *"Mirad esto. Ignoró el rate limit temporal que le pedí para Reddit."*
   - *"Se inventó una importación que no existe en esta librería."*
   - *"Si mando esto a producción tal cual, crasheo el servidor por pérdida de memoria."*

### FASE 4: La Auditoría Quirúrgica (El Senior entra en escena)
*Aquí es donde demuestras por qué ganas lo que ganas.*
1. **Pantalla:** Tú editando manualmente el código generado, borrando líneas innecesarias o agregando control de estado.
2. **Narrativa:** "La IA hizo el 80% del trabajo aburrido (boilerplate, sintaxis bruta). Ahora el humano hace el 20% crítico: auditar, asegurar la persistencia y forzar el tipado fuerte."
3. **Acción:** 
   - Borras código sobrante. ("Minimalismo funcional").
   - Ajustas un try/catch o fuerzas el tipado de retorno.
   - Ejecutas en la terminal el script reparado para que la audiencia vea el "Success".

### FASE 5: El Sello de Autoridad (Post-Generación)
*Donde dejas claro que tú mandas sobre la IA. Destruye el auto-commit.*
1. **Pantalla:** Terminal a tamaño grande o la vista de *Source Control* en VS Code.
2. **Narrativa:** "La IA terminó hace 10 minutos, pero el código no sube hasta que el contrato esté cumplido. Ahora que pasó la auditoría (tests, tipado), yo lo firmo."
3. **Acción:**
   - Escribes el comando en vivo: `git commit -m "feat(module): refactor según rule 3 de spec.md"`
   - Demuestras que tu historial de Git está vinculado directamente a las specs aprobadas, rechazando formalmente automatizar este paso en el agente.

---

## REGLAS DE ORO EN GRABACIÓN

- **Sin cortes perfectos:** Si tienes un error de sintaxis al corregir a la IA, déjalo en el video. El proceso de leer el error en consola y arreglarlo es "Ingeniería Real".
- **Enfoque Dinámico de Pantalla (Adiós al 3 Columnas Estático):** Mantén el tamaño de fuente legible (14px+). Usa un plano inicial de 3 columnas (Specs | Código | Agente), pero haz **zoom dinámico**: expande las Specs al leerlas, usa 2 columnas al generar código y expande la terminal al depurar errores.
- **Transparencia Financiera y Metal Local:** Nunca ocultes el medidor de costo de Cline o el terminal de Ollama. El contraste entre los $2.00 de un loop de Sonnet mal guiado y los **$0.00** de una corrida local con Qwen-7B en tu RTX 4060 es tu mejor prueba de autoridad técnica y eficiencia económica.
- **Protege el Stack Oficial CSDD:** Nunca utilices nomenclaturas genéricas (`PROMPT.md`, `TASKS.md`) en cámara. Defiende la nomenclatura exclusiva que la comunidad debe clonar en tu repo `csdd-templates` (`CONSTITUTION.md`, `contracts.md`, `spec.md`, `plan.md`, `tasks.md`). El "plan" es tu foso competitivo.
- **Narrativa de "Baja Energía / Alta Confianza":** No eres un Youtuber hiperactivo. Habla pausado, con el tono de un ingeniero cansado pero sumamente competente que está explicando un sistema a un Junior (que en este caso, es tu GPU local).
