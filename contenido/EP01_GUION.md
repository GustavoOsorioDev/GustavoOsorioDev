# EP01: ¿Programador Obsoleto? (Así volví con Inteligencia Artificial)

**Estado:** Borrador V4 (Avatar corregido: Miguel/El Constructor Solo)
**Duración Objetivo:** 8-10 minutos
**Tono:** Honesto, analítico, baja energía / alta confianza. "Ingeniería real compensando el óxido."
**Avatar Primario:** Miguel/Andrea — El Constructor Solo (2-6 años exp., proyectos propios, usa IA masivamente, teme la fragilidad de lo que construye)
**Gancho Psicológico:** La culpa compartida de mandar código de IA a producción sin entenderlo del todo. CSDD como el método que salva al dev solo cuando no tiene Tech Lead que lo corrija.

---

## Thumbnail & Título Ideas
*   **Título Principal:** ¿Quedé obsoleto como programador? Lo comprobé en cámara.
*   **Alternativa A:** Volví a programar después de años fuera del código activo (con IA).
*   **Miniatura (CTR Optimizado - Máx 4 palabras):** 
    *   Fondo: Código con un error grande marcado en rojo o un diagrama roto.
    *   Rostro: Expresión seria, analizando la pantalla.
    *   Texto (Impacto): "¿Programador OBSOLETO?" o "VOLVÍ. CON IA."

---

## ESTRUCTURA DEL GUION

### 1. EL GANCHO: LA CULPA COMPARTIDA (0:00 - 1:00)
**(PANTALLA: Terminal mostrando un error 429 en rojo — sin contexto, sin intro)**
**Gustavo:** "¿Cuántas veces le pediste código a la IA esta semana y lo mandaste a producción sin revisarlo del todo?"
**(PAUSA de 1 segundo)**
**Gustavo:** "Yo lo hice. Y ese código estaba haciendo 50 requests por segundo a Reddit. Bloqueo inmediato. Error 429."
**Gustavo:** "No lo detecté yo. Tengo años de experiencia en backend. Tampoco lo detectó la IA. Lo atrapó el contrato de datos — una estructura Pydantic que gritó: *'Este dato no viene como me lo prometieron'* antes de que el sistema fallara en silencio."
**(CORTE a la terminal ejecutando `cazador-cli` con output limpio y ordenado)**
**Gustavo:** "Esto es Cazador CLI. Lo construí volviendo a programar después de años de no hacerlo activamente. Y este video es el post-mortem honesto de ese proceso."
**Gustavo:** "Soy Gustavo Osorio. Bienvenido a ingeniería real."

### 2. FASE 1: EL TABLERO DE MANDO (1:00 - 3:00) - *El contrato como árbitro*
**(ZOOM IN a la carpeta `.specs/` en el IDE — que se vea el archivo `01_data_contract.md`)**
**Gustavo:** "Déjame mostrarte lo que cambió cómo trabajo. Esta carpeta no la creé porque sea ordenado."
**Gustavo:** "La creé porque me di cuenta de que cuando no tienes un Tech Lead revisando tu código, tu única salvaguarda eres tú mismo. Y si llevas un tiempo sin tocar ese lenguaje, o si simplemente eres el único dev del proyecto, tu instinto puede estar equivocado."
**Gustavo:** "Entonces puse el árbitro por escrito. El contrato de datos. 'Esta es la forma exacta que tiene cada dato en este sistema. Nadie — ni yo, ni la IA — puede ignorarla sin que el sistema grite'."
**(HOVER sobre el archivo, mostrando el modelo Pydantic)**
**Gustavo:** "Aquí no guardas prompts. Aquí guardas decisiones irrevocables. La diferencia entre un proyecto que escala y uno que te explota en producción no está en qué tan avanzada es la IA que usas. Está en si tienes un contrato antes de tocar el teclado."

### 3. FASE 2: EL DESPACHO (3:00 - 5:00) - *Briefear a la máquina*
**(PANTALLA: El chat de Claude o el IDE con el prompt en construcción)**
**Gustavo:** "Ahora le paso este contrato a la IA. No le digo 'hazme un scraper de Reddit'. Le digo: 'Implementa esta función. Los datos de salida deben cumplir este esquema Pydantic. Si un campo falla la validación, levanta una excepción, no silencie el error'."
**Gustavo:** "En mi época de Java había un compilador que te cortaba en seco si rompías un contrato de tipos. Hoy el lenguaje es dinámico y la IA es optimista. Si no la obligas a respetar la estructura, va a inventarse lo que le falte."
**(DISPARO del prompt — la IA genera el código a velocidad máxima)**
**Gustavo:** "Ochenta líneas en cuatro segundos. Se ve limpio. Se ve profesional. Y está mal."  *(sin resolver todavía — dejar la tensión abierta)* 

### 4. FASE 3: EL CHOQUE CON LA REALIDAD (5:00 - 7:30) - *El único adulto en la sala*
**(PANTALLA: El código generado — mostrar las 80 líneas completas)**
**Gustavo:** "Mira esto. Limpio. Legible. Y si lo ejecutas, te bloquea Reddit en 30 segundos."
**(ZOOM a la sección del loop de requests — sin rate limiting, sin delay)**
**Gustavo:** "¿Lo vi a primera vista? No. Y tengo años de experiencia en backend. Porque el código *parece* correcto. Eso es exactamente el problema: el vibe coding no produce código que falla ruidosamente. Produce código que falla en silencio, tres semanas después, en producción."
**(EJECUTAR el script — mostrar el error 429 apareciendo en terminal)**
**Gustavo:** "El rate limit de Reddit cortó la respuesta a la mitad. Datos incompletos. Y aquí es donde ocurrió algo interesante."
**(ZOOM al stack trace — señalar la excepción de Pydantic)**
**Gustavo:** "El modelo Pydantic rechazó el dato incompleto. No silenció el error. Gritó: *'Este campo es obligatorio. Este dato está roto. Para todo.'*"
**Gustavo:** "La IA fue perezosa. Mi instinto estaba oxidado. El contrato fue el único adulto en la sala."
**(PAUSA — dejar que eso aterrice)**

### 5. FASE 4: LA AUDITORÍA QUIRÚRGICA & CIERRE (7:30 - 10:00)
**(PANTALLA: Gustavo editando la corrección — añadir exponential backoff al loop)**
**Gustavo:** "La corrección son cuatro líneas. Un sleep con backoff exponencial. La IA pudo haberlas puesto sola. No lo hizo porque nadie se lo exigió en el contrato."
**Gustavo:** "Ahí está la lección. La IA hace el ochenta por ciento del trabajo aburrido en segundos. El humano hace el veinte por ciento crítico: auditar, entender el fallo, y aplicar la corrección con criterio."
**(EJECUTAR el script corregido — output limpio, datos llegando en tabla Rich)**
**Gustavo:** "No salió perfecto a la primera. Pero salió robusto a la salida, porque el contrato no nos dejó pasar por alto lo que ninguno de los dos habríamos visto solos."

---

**(CTA — tono directo, sin efusividad)**
**Gustavo:** "El código completo está en GitHub. Link en la descripción. No lo copies sin abrirlo. Lee el contrato Pydantic primero, después mira el código. Eso es exactamente cómo deberías revisar el código que te genera la IA."
**Gustavo:** "En el próximo video le pongo un cerebro a esto. Un LLM corriendo en mi propia GPU, sin API keys, para que el bot no solo detecte palabras clave sino que entienda contexto. Si eso te interesa, ya sabes qué hacer."
**(PAUSA)**
**Gustavo:** "Y una pregunta para los comentarios — quiero una respuesta sincera: ¿hay algún proyecto tuyo corriendo en producción ahora mismo cuyo código no entiendes del todo porque lo generó la IA? Porque si la respuesta es sí, este canal es para ti."
**Gustavo:** "Ingeniería real. Sin vibes."
