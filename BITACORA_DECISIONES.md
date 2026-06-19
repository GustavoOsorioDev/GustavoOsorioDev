# Bitácora de Decisiones — @GustavoOsorioDev

Aquí anoto por qué cambiamos de rumbo. Sirve para no dar vueltas en círculos y no perder el tiempo repitiendo errores.

## 16-Jun-2026: El Gran Cambio de Planes

### 1. Adiós al canal de "IA sin rostro"
- **Por qué:** Analicé los números y no daban. Hacer un video tomaba 15 horas para ganar centavos, con el riesgo de que YouTube nos borrara por generar contenido basura. No valía la pena.
- **Qué vamos a hacer:** Usar esas 28 horas semanales para programar en público y enseñar ingeniería de verdad.

### 2. "Ingeniería real" como marca
- **Por qué:** Queremos diferenciarnos de los canales que solo copian y pegan lo que dice ChatGPT.
- **Decisión:** Mostrar siempre el diseño antes del código. No vendemos humo, vendemos arquitectura sólida.

### 3. Separación de Proyectos (Lite vs Core)
- **Causa:** Necesidad de un "Lead Magnet" (Lite en GitHub) vs un "Moat" (Core privado para negocio).
- **Decisión:** El canal de YouTube se alimentará de ambos, pero solo el Lite se comparte como software descargable.

### 4. Uso de Workspaces Independientes
- **Causa:** Evitar contaminación de contexto en la IA y desorden visual en el set de grabación.
- **Decisión:** `@GustavoOsorioDev` es el HQ estratégico. `cazador-cli` es el set de rodaje técnico.

### 5. Consolidación de Ecosistema GitHub
- **Audit:** Revisión de `csdd-templates` y `csdd-core`.
- **Decisión:** Mantener `csdd-templates` como el estándar público y vitaminarlo con soporte para Python/Pydantic para alinearlo con el lanzamiento del canal. `csdd-core` permanece como el repositorio espejo para proyectos de negocio.

### 6. Limpieza Quirúrgica de Repositorios
- **Causa:** Mantener la ilusión visual y autoridad técnica requería un "set de grabación" limpio.
- **Decisión:** Eliminados 5 repositorios basura, dejando únicamente `csdd-templates` y `csdd-core`.

### 7. Ingeniería del Video 1: "Stealth RSS"
- **Causa:** Reddit API bloqueaba (403) el escáner del Cazador V3 en entornos automatizados.
- **Decisión:** Implementada la técnica *Stealth RSS Atom* extraída del motor V6 en el script Lite. Se enfocó la validación (Pydantic/Rich) estrictamente en "sintaxis de frustración" para demostrar resolución técnica real y mantener el alcance de un MVP.

### 8. Arquitectura de Marca y Nomenclatura Constante
- **Causa:** Evitar la fragmentación y deuda técnica en el posicionamiento al tener nombres temporales o con bajo "seniority".
- **Decisión:** Renombra local y remoto para `cazador-cli` (público MVP), `cazador-engine` (privado enterprise), y `csdd-core` (privado core tech).

### 9. El Modelo "Iceberg" (Privacidad de cazador-engine)
- **Causa:** Definir la línea entre la aportación de valor a la comunidad y la protección del activo de negocio (Moat).
- **Decisión:** `cazador-engine` se mantendrá **estrictamente privado**. Solo se mostrará su arquitectura y funcionamiento interno en los videos para generar autoridad técnica (El Modelo "Iceberg"). Por el contrario, `cazador-cli` fungirá como el "Lead Magnet" open-source.

---

## Decisiones 17-Jun-2026: Especialización Técnica y Escalabilidad

### 10. Especialización de Hardware (Pipeline de Producción)
- **Causa:** Necesidad de optimizar las 28h semanales mediante automatización de tareas repetitivas (carpintería técnica).
- **Decisión:** Configurar workflows asíncronos distribuidos:
    - **RTX 2000 Ada (Oficina):** Estación de desarrollo puro, compilación y orquestación de agentes de IA locales.
    - **RTX 3060 Ti (Casa - Planta Multimedia):** Procesamiento automático de audio (Whisper), limpieza de ruido y generación de subtítulos.
    - **RTX 4060 (Casa - Asistente de Inferencia):** Generación de assets visuales (ComfyUI) e inferencia de lógica pesada (Modular LLM).

### 11. Refactor Modular de Cazador CLI (Hardware-Agnostic)
- **Causa:** Conflicto entre la autoridad técnica (uso de hardware Pro) y la accesibilidad de la audiencia (mínimo común denominador).
- **Decisión:** Implementar un diseño modular en `cazador-cli`:
    - **Capa 1 (Regex):** Rápida y sin requisitos de GPU (para la audiencia general).
    - **Capa 2 (Local LLM):** Alta precisión y clasificación semántica real (para demostrar autoridad técnica con hardware NVIDIA).

### 12. Posicionamiento de Kaggle como "Puente de Valor"
- **Causa:** La audiencia sin GPU local necesita una vía para ejecutar las herramientas Pro de Gustavo.
- **Decisión:** No usar Kaggle como entorno de desarrollo principal (para no diluir la marca de "Ingeniero de Metal"), sino como un recurso táctico para el usuario final. Gustavo construye en local; el usuario replica en la nube gratuita (Kaggle/Colab).

### 13. El "Proceso de Ingeniería" como Producto
- **Causa:** Diferenciarse de los tutoriales de "Copia y Pega".
- **Decisión:** El éxito de @GustavoOsorioDev no reside en el script final, sino en documentar cómo el código se rompe y cómo la arquitectura (SDD) lo arregla. El "broken-and-fixing" es el motor de confianza técnica.

### 14. El "Modo Director" y el Mito del "Mecanógrafo"
- **Causa:** El Síndrome del Impostor generado por el estereotipo irreal de Hollywood del hacker escribiendo 200 líneas de código por minuto sin mirar.
- **Decisión:** Abrazar de frente el uso intensivo de la IA. El formato no ocultará a Claude/Antigravity; los convertirá en coprotagonistas (los Juniors). El foco del canal no es tipear rápido, sino **orquestar, auditar y corregir** los desastres de la IA aplicando arquitectura pura.

### 15. Definición Psiconómica de Avatares (Sebastián y Carlos)
- **Causa:** Necesidad de enfocar el mensaje para maximizar el CTR y la retención en un mercado saturado de "Vibe Coding".
- **Decisión:** Definir dos avatares específicos basados en datos de 2026:
    - **Sebastián/Valeria (Mid-Level):** Busca recuperar el control técnico que la IA le ha quitado.
    - **Carlos/Andrea (Tech Lead):** Busca un framework (CSDD) para estandarizar la calidad de sus equipos y frenar el "AI Slop".
- **Acción:** Consolidación de datos del `analisis_audiencia_gustavo_osorio.html` en un nuevo documento maestro `AUDIENCIA.md` dentro de `/inteligencia/` para facilitar la consulta asíncrona de la IA.

### 16. La "Tercera Puerta" y Filosofía Fractal
- **Causa:** Evitar competir en nichos saturados de tutoriales genéricos o lidiar con el bajo CPM del "vibe coding" o curiosidades generales en español.
- **Decisión:** Implementar la "Tercera Puerta": Documentales técnicos aplicando la Filosofía Fractal (Biología vs. Modernidad). Se definió el hook de "hackear el círculo de seguridad" y la creación de la identidad en `FRACTAL_FILOSOFIA.md`.

### 17. Reestructuración del Episodio 1
- **Causa:** El guion original del EP01 estaba anclado al caso "Reddit/Cursor" que no aprovechaba la infraestructura local y no hacía de "Lead Magnet" efectivo para la audiencia objetivo.
- **Decisión:** Se reescribió `contenido/EP01_GUION.md` para hacer la "Autopsia de Cazador CLI". El video ahora enseña CSDD (con Pydantic), el "Stealth RSS" para eludir errores 403, y expone de forma transparente las limitaciones del análisis de texto actual (creando el puente para el EP02 con LLM local).

---
*Fin de registro del día (Estrategia de hardware documentada, Filosofía Fractal consolidada, EP01 alineado como Autopsia de MVP).*

## Decisiones 17-Jun-2026 (Noche): Alineación de Avatar y Ejecución

### 18. Redefinición del Avatar Primario para EP01/EP02
- **Causa:** El guion original del EP01 hablaba desde la vulnerabilidad ("estoy oxidado"), pero intentaba conectar con Tech Leads (Carlos) o Devs de equipos corporativos (Sebastián), creando disonancia de autoridad.
- **Decisión:** Se introdujo a "Miguel / Andrea — El Constructor Solo" como Avatar Primario temporal en `AUDIENCIA.md`. La narrativa de Gustavo resuena al 100% con personas que construyen solas sistemas delicados delegando en IA y que temen a la fragilidad.

### 19. Reescribir el Gancho y Fases del EP01
- **Causa:** El guion resolvía la tensión muy pronto (min 0:15) y el clímax estaba enterrado (min 5:00).
- **Decisión:** El `EP01_GUION.md` se actualizó a V4. El error 429 se adelantó a los primeros 10 segundos, la carpeta `.specs/` se planteó como un salvavidas (no una clase teórica) y el CTA final se volvió directo y emocional para el avatar específico.

### 20. Freno a la Planificación Infinita
- **Causa:** Una auditoría integral descubrió que no se podía grabar porque el código sobre el que habla el video aún no existe o no tiene los estándares.
- **Decisión:** No documentar nada más en el HQ estratégico de @GustavoOsorioDev. La primera tarea indiscutible de la mañana es cambiar el contexto al workspace de `cazador-cli` y refactorizar su código base.

### 21. El Refactor "Seniority" de Cazador-CLI
- **Causa:** El MVP del canal (`cazador_v3.py`) adolecía de defectos que destruirían la narrativa de "autoridad técnica" (sin persistencia estructurada, sin manejo robusto de tasa de límites y sin sincronía algorítmica con sus spec_docs).
- **Decisión:** Se ejecutó agresivamente la primera parte del `checklist_produccion_video_1.md`. Se integró SQLite para robustez, Pydantic para el cumplimiento estricto del *Data Contract*, captura explícita de `HTTP 429` (Rate limits) utilizando librerías elegantes (Rich) y el rename de "script.py" a `main.py`. El código se homologó al grado de "demo de cámara técnica", validando la propia doctrina pregonada en el canal.

---

## Decisiones 18-Jun-2026: Documentación Post-Refactor

### 22. Creación de `auditoria_proyecto.md` como Artefacto Permanente
- **Causa:** El Refactor "Seniority" (Decisión 21) produjo cambios técnicos reales y sustanciales que debían quedar registrados con precisión — no como notas en la bitácora sino como un documento técnico auditable y consultable en futuras sesiones.
- **Decisión:** Se creó `@GustavoOsorioDev/auditoria_proyecto.md` con el diagnóstico pre/post completo: brechas encontradas (tabla de severidad), cambios de código documentados como diffs, esquema SQLite definitivo, cobertura del checklist por fase, deuda técnica conocida y veredicto técnico. El documento establece que el código está **listo para grabar EP01** y que el siguiente bloque de código pertenece a EP02.
- **Convención:** Este patrón (auditoría técnica como artefacto separado) se adopta para cada refactor mayor antes de grabar. No sustituye a la bitácora; la complementa con evidencia técnica específica.

### 24. Optimización de Calidad (Hack Top/Week)
- **Causa:** El análisis post-refactor (Sesión 18-Jun) reveló que el modo `/new.rss` entregaba una relación señal/ruido muy baja (muchos falsos positivos, posts de éxito, o quejas sin tracción real).
- **Decisión:** Se cambió la fuente RSS de `new` a `top.rss?t=week`. 
- **Impacto:** Reddit ahora hace la pre-validación por nosotros. Solo procesamos posts que la comunidad ya votó y validó durante la semana, pero los filtramos con nuestro detector semántico de dolor. Esto asegura que el "insumo de trabajo" del canal sea de alta fidelidad desde el EP01.

### 23. Corrección de Bug Crítico — Scoring RSS ("Bug de Demostración Muerta")
- **Causa:** Durante la revisión de documentación post-refactor se detectó que la función `calcular_score()` producia `0.0` invariablemente en modo RSS, ya que los campos `comentarios=0` y `votos=0` (el feed RSS no los expone sin OAuth) anulaban cualquier multiplicador semántico. El filtro `if op.score_gap > 0` bloqueaba todos los resultados, dejando la base de datos vacía y la demo en cámara inutilizable.
- **Decisión:** Se añadió una rama de fallback en `calcular_score()`: cuando `base_score == 0`, el score se calcula directamente como conteo de coincidencias semánticas con `PATRONES_DOLOR` (`return round(float(coincidencias), 2)`). El contrato `.specs/01_data_contract.md` fue actualizado a v1.1.0 para formalizar este comportamiento como "Regla de fallback RSS". La auditoría `auditoria_proyecto.md` registra el diagnóstico completo con tabla de valores en la sección 5b.
- **Lectura:** Este es el mismo ciclo que el canal predica: el contrato atrás el código, la auditoría atrás el contrato.

### 25. Oficialización del Slogan: "Ingeniería real, sin vibes"
- **Causa:** El posicionamiento del canal necesita una navaja de Ockham para filtrarse entre los creadores genéricos de IA, y atraer ingenieros mid/senior cansados de tutoriales frágiles ("vibe developers").
- **Decisión:** Integrar el slogan como el "grito de guerra" del canal. El lema polariza, lo cual es invaluable comercial y demográficamente, pero fuerza al creador (Gustavo) a operar bajo un microscopio, requiriendo que su código de cámara carezca de malas prácticas (side effects, dependencias circulares, etc).
- **Ejecución:** Empieza a aplicarse como tagline narrativo en descripciones, scripts y cabeceras de repositorios.

### 26. Proscripción Fundamental: 🛑 CERO TOLERANCIA AL "AI SLOP" 🛑
- **Causa:** La coherencia con el slogan (Decisión 25) exige un muro técnico irrompible. Generar código con ChatGPT no puede significar aceptar "soluciones mágicas" sin integridad.
- **Decisión:** Se anexó el protocolo 🛑 CERO TOLERANCIA AL "AI SLOP" 🛑 al `GEMINI.md` principal, forzando algorítmicamente a Antigravity (y otros agentes locales) a mantener una estricta adhesión a Funciones Puras, Arquitectura Limpia y Contratos Inmutables.
- **Impacto a cámara:** Esta regla es el motor del canal. La IA generará basura en cámara, pero **Gustavo** ejercerá de tech lead validando con esta convención el por qué ese código es "slop" y refactorizándolo.

### 27. El Fin de Juego: Dogfooding y Micro-SaaS (Double-Dip ROI)
- **Causa:** Quedarse produciendo scripts o web-scrapers genera views, pero no monetización profunda ni resuelve el dolor fundamental del avatar.
- **Decisión:** El objetivo de programación definitivo pasa a ser la construcción de **Micro-SaaS y DevTools** usando "Dogfooding". Gustavo programará herramientas que él mismo necesita urgentemente. Al documentarlas, demuestra arquitectura real de producción (Auth, DB, Pagos).
- **Impacto al Negocio:** El canal opera bajo el formato de "Double-Dip ROI": Adsense/Sponsors por las visitas, más MRR (Monthly Recurring Revenue) de los espectadores que comprarán el software porque padecen el mismo problema que Gustavo ("El Constructor Solo").

### 28. Arquitectura de Monetización: "Ecosistema Central" y Doble Nivel Gratis
- **Causa:** Evitar la fatiga de suscripción en Devs (comprar herramientas separadas) y mitigar el abuso de bots en los Trials gratuitos.
- **Decisión:** El SaaS adoptará un modelo de **Créditos y API Key Central**. Todas las herramientas de CLI/Web generadas en el canal serán clientes que consuman una sola bolsa de créditos procesada en el backend privado (`cazador-engine`, que es estrictamente privado).
- **El Producto no es la app, es el Motor:** Se factura por capacidad de cómputo/procesamiento ("Plan Builder: $20/mes = 10,000 créditos"), no por herramienta individual. Esto escala sin fricción con cada nueva herramienta que se lance.
- **Embudo Anti-Fricción (Doble Nivel Gratis):**
  1. *Zero-Quota Permanente (Capa Local):* El código open-source descargado de GitHub opera en modo básico (ej. Regex/RSS) **sin requerir API Key**. La herramienta hace algo útil. Esto es obligatorio para no crear haters que sientan que el GitHub gratuito es humo. La credibilidad de la comunidad open-source está intacta.
  2. *Bolsa de Prueba — "Aha! Moment" (Capa Engine):* Al registrarse en `hq.gustavoosorio.dev`, el usuario recibe **500 créditos gratuitos (sin tarjeta de crédito)** y genera una API Key personal. La clave se pega en el CLI local. La herramienta activa el "Modo AI": contacta el `cazador-engine` privado, revela el verdadero poder del análisis semántico pesado, y va quemando créditos hasta el agotamiento.
- **Calibración del Trial:** Los 500 créditos deben ser exactamente suficientes para el "Aha! Moment" (encontrar 1 nicho rentable real), pero NO para cubrir una semana de uso intensivo. El objetivo es que el usuario integre la herramienta en su flujo antes de agotar el trial.
- **Migración Orgánica al Pago:** Cuando los créditos se agotan, la terminal lanza un error estilizado (`[bold red]Créditos agotados. Recarga en hq.gustavoosorio.dev[/]`). El usuario ya conoce el valor; sacar la tarjeta es un paso natural, no una venta forzada.
- **Defensa Anti-Abuso (GitHub OAuth):** El registro exige **GitHub OAuth** en lugar de email/password. Un dev real no creará 10 perfiles falsos de GitHub (que requieren antigüedad, repos y actividad para ser creíbles) para ahorrarse $10/mes. La barrera de ingeniería filtra parásitos de forma inherente sin necesitar CAPTCHAs invasivos.
- **Impacto en la Arquitectura GitHub:** Este modelo consolida la separación arquitectónica ya establecida:
  - `cazador-cli` (Público): Lead magnet, construye comunidad, cero barrera de entrada.
  - `cazador-engine` (Privado): Motor de ingresos, accesible solo vía API Key del SaaS.

### 29. El Conversion Funnel Completo (YouTube → GitHub → SaaS)
- **Causa:** Necesidad de documentar el flujo completo de conversión de un espectador anónimo a cliente de pago, para no improvsar la arquitectura del SaaS en el futuro.
- **Decisión:** El embudo es de 4 capas, cada una con una función específica:
  1. **YouTube (Tráfico + Autoridad):** El espectador llega por SEO técnico ("bot Reddit Python", "Pydantic tutorial"). La narrativa del video demuestra ingeniería real. El CTA es siempre el repositorio de GitHub.
  2. **GitHub (Lead Magnet + Comunidad):** El usuario clona `cazador-cli`. Lo usa en modo Zero-Quota. Empieza a entender el potencial. El README lo dirige a `hq.gustavoosorio.dev` para "activar el modo AI".
  3. **hq.gustavoosorio.dev — Sign Up (Lead Captura):** El usuario hace GitHub OAuth. **El correo electrónico se captura en este punto.** Se convierte de visitante anónimo a Lead en la base de datos. Obtiene 500 créditos. Llega a su "Aha! Moment".
  4. **Checkout (Conversión a MRR):** Los créditos se agotan. El Lead recibe un email recordatorio de recarga. Con el valor ya demostrado, la conversión a plan de pago es orgánica. El MRR crece con cada nueva herramienta que se lance en YouTube porque los suscriptores existentes la prueban gratis con sus créditos, consumen más, y hacen upgrade de plan.
- **Métrica Clave a rastrear:** `Tasa de Activación de Trial` (% de clones de GitHub que llegan a `hq.gustavoosorio.dev`) y `Tasa de Conversión de Trial a Pago`. Son los dos cuellos de botella que determinarán la salud del negocio.

---

## Decisiones 18-Jun-2026 (Tarde): Stack de IDE para CSDD y Modelos Locales

### 30. Elección Definitiva del IDE: VS Code + Cline
- **Contexto:** Sesión de investigación comparativa entre Cursor, Windsurf, VS Code con plugins, y Claude Code.
- **Opciones descartadas:**
  - **Cursor:** Caja negra. Perfecta para la productividad personal, pero el agente no explica su razonamiento. Inutilizable como contenido educativo.
  - **Windsurf (Cascade):** Similar problema. El flujo Cascade es potente pero opaco para la audiencia.
  - **GitHub Copilot:** Costoso, black-box, no muestra tokens ni costos. Contradice la narrativa CSDD del canal.
- **Decisión:** `VS Code + Cline` como stack principal del canal.
- **Razón técnica:** Cline muestra en tiempo real: el razonamiento del agente, el costo por tarea en dólares, los tokens consumidos, y los archivos que lee como contexto. Esto es el contenido, no solo la herramienta.
- **Razón estratégica:** El "Costo de Configuración" (la curva de aprendizaje) no es una desventaja para el canal. Es la mina de oro de contenido. Cada paso del setup es un video.
- **Documentado en:** `estrategia/SETUP_IDE_CSDD.md`

### 31. Estrategia de Modelos: Local Primero, Kaggle para el Video Específico
- **Contexto:** Exploración de Qwen-Coder suite en Kaggle como motor gratuito para CSDD.
- **Decisión técnica:** La arquitectura Kaggle + ngrok + Ollama es viable, pero **frágil para producción**:
  - Sesiones de Kaggle tienen timeout (máx. ~9h). Una sesión muerta en medio de la grabación arruina la toma.
  - `ngrok` free tier muestra una página de advertencia de seguridad en el navegador.
- **Decisión definitiva:**
  1. **Día a día de desarrollo:** Qwen2.5-Coder 7B corriendo en Ollama local (RTX 4060, 8GB VRAM). ~15-20 tokens/seg. Estable, $0.00, sin dependencia de red.
  2. **Video temático "SDD $0.00":** Se monta el setup Kaggle en vivo como demostración. El riesgo del timeout es parte del drama del video.
  3. **Tareas que requieren máxima inteligencia:** Claude Sonnet como modelo principal en Cline (con API key Anthropic).
- **Regla derivada:** Qwen local es el "junior local" del canal. Claude es el "consultor externo" para arquitectura compleja. La audiencia ve el costo de cada uno.
- **Documentado en:** `estrategia/SETUP_IDE_CSDD.md`, `contenido/EP02_SPEC.md`

### 32. EP02 Re-definido: "Conecté una RTX 4060 a mi Bot de Reddit"
- **Contexto:** Se había propuesto el setup del IDE como EP02, pero se analizó que rompía la narrativa de construcción ("Build in Public").
- **Decisión:** El setup de VS Code + Cline se queda como documentación interna (`estrategia/SETUP_IDE_CSDD.md`) y demo contextual dentro de otros videos. El EP02 vuelve a ser la integración de la RTX 4060 con LLM local para clasificación semántica de `cazador-cli`.
- **Razón:** Mantener la "Serie" funcional: EP01 (Bot básico) -> EP02 (Bot con cerebro local) -> EP03 (IA para edición). Esto maximiza la retención y la autoridad de construcción.

### 33. Rechazo de la Automatización de Git en el Agente
- **Contexto:** Se planteó que el agente (Cline) hiciera commits automáticos al cumplir cada especificación para "destruir el vibe coding".
- **Decisión:** **Rechazado.** El agente propone el código; el humano audita (Fase 4 del WORKFLOW) y ejecuta el commit.
- **Razón:** Si el agente aprueba su propio trabajo con un autocommit, el historial de Git prueba que la IA tiene la autoridad final, invalidando tu rol como Arquitecto. El "git commit" deliberado, referenciando una decisión de la spec, es la demostración empírica del CSDD.

### 34. Modelo Dinámico de Grabación (Layout VS Code)
- **Contexto:** Mantener un layout estricto de 3 columnas (Specs | Código | Agente) resultaría ilegible en pantallas de teléfonos móviles (60%+ de la audiencia).
- **Decisión:** El layout 3 columnas es solo el "Establishment Shot" (Plano General) al inicio de una tarea. Durante la ejecución se utiliza el zoom dinámico: 
  - Zoom a las Specs ("Lo que dice el Jefe").
  - Pantalla dividida en 2 (Spec + Código) durante la generación.
  - Full Terminal durante los errores y corrección.
- **Razón:** Priorizar la legibilidad móvil sin sacrificar la jerarquía visual de que "las specs siempre mandan".

### 35. Protección de Marca del "Stack CSDD"
- **Contexto:** Se sugirió usar un stack genérico simplificado (`PROMPT.md`, `SPEC.md`, `TASKS.md`) para hacer el método más "clonable" por la audiencia general.
- **Decisión:** **Totalmente rechazado.** Se utilizará rigurosamente la nomenclatura oficial de `csdd-templates` (`CONSTITUTION.md`, `contracts.md`, `spec.md`, `plan.md`, `tasks.md`).
- **Razón:** El término `plan.md` es el foso competitivo (Moat) del CSDD vs el Vibe Coding; es la prueba de que el arquitecto aprobó la estructura antes de que la IA tirara línea. Ceder ante el formato genérico anula la diferenciación del canal y diluye el SEO natural de la metodología.

### 36. Actualización del Firewall de Modelos 2.0 (Factor Metal y Triggers)
- **Causa:** El sistema original de Niveles 1-4 era puramente logístico. Se necesitaba alinearlo con la narrativa del canal: Hardware local, ahorro de costos y primacía de la arquitectura.
- **Decisión:** Implementar la jerarquía de 5 niveles e introducir "Triggers de Arquitectura":
    - **Nivel 0 (Metal):** Inferencia en GPUs locales (RTX) para boilerplate y docs ($0.00 cost).
    - **Trigger de Contrato:** Cualquier cambio en `.specs/` escala automáticamente a **Nivel 3 (Sonnet)**, sin importar el volumen de código o complejidad aparente.
    - **Trigger de Auditoría:** Corregir "AI Slop" requiere Nivel 3.
- **Impacto:** Refuerza el posicionamiento de Gustavo como un Tech Lead que sabe cuándo delegar a un "Junior local" y cuándo llamar al "Arquitecto Senior" (Sonnet) para validar la base de datos o el contrato.

### 37. Consolidación de Guía de Estilo Narrativo
- **Causa:** El tono de voz y los términos clave estaban dispersos en guiones y plantillas. Se necesitaba un "Source of Truth" para la identidad del canal.
- **Decisión:** Crear `contenido/GUIA_ESTILO_NARRATIVO.md`. 
- **Puntos Críticos:**
    - Se formaliza el tono "Baja Energía / Alta Confianza".
    - Se blindan términos como "Vibe Coding", "AI Slop", "Óxido" y "Carpintería".
    - Se prohíben introducciones de saludo genérico.
- **Objetivo:** Asegurar que cada video de la serie mantenga la misma autoridad técnica y comercial.

### 38. Activación de Protocolo de Freno (Yield Protocol)
- **Causa:** Evitar que el agente ejecute cambios críticos de arquitectura con modelos insuficientes (Nivel 1/2) de forma silenciosa.
- **Decisión:** Implementado el "Yield Protocol" en `GEMINI.md`. El agente debe detenerse y pedir confirmación explícita (o cambio de modelo) si la tarea es de Nivel 3 pero el modelo es inferior.
- **Razón:** Blindar la integridad de los contratos y las especificaciones arquitectónicas, evitando el "AI Slop" por subestimación de complejidad.

### 39. Lanzamiento de Infraestructura de Inferencia Nivel 0 (Kaggle)
- **Causa:** Necesidad de un mecanismo reproducible para que la audiencia use SDD sin costo operativo.
- **Decisión:** Creación de `estrategia/SCRIPTS_KAGGLE.py` que automatiza la instalación de Ollama y la exposición vía ngrok.
- **Razón:** Permitir a la audiencia escalar de modelos pequeños locales a modelos de 14B/32B parámetros de forma gratuita, validando la tesis de "Ingeniería Real por $0.00" para el canal de YouTube.

### 40. Implementación de Efficiency Check (Gestión de Desperdicio)
- **Causa:** El Firewall solo bloqueaba hacia arriba, permitiendo el desperdicio de modelos caros en tareas triviales.
- **Decisión:** Obligar al agente a reportar y recomendar degradación de modelo si detecta tareas de Nivel 1/2 ejecutándose en modelos de Nivel 3/4.
- **Razón:** Reforzar la marca de "Arquitecto Senior" que no solo cuida el código sino la economía del proyecto. Es un elemento pedagógico clave para el canal.
### 41. Universalización del Firewall 2.0 (Constitución Global)
- **Causa:** Necesidad de que la metodología CSDD sea persistente en cualquier proyecto, nuevo o existente.
- **Decisión:** Actualizado el archivo maestro `~/.gemini/GEMINI.md` y creados `GEMINI.md` locales en `cazador-cli`, `cazador-engine` y `csdd-templates`.
- **Impacto:** Cualquier agente de IA operando en el ecosistema bajo Antigravity ahora hereda automáticamente la lógica de Yield y Efficiency Check. Se eliminó el riesgo de "olvido de reglas" por parte del agente.

---

## Decisiones 19-Jun-2026: Soberanía de Hardware y Costo $0.00

### 42. Soberanía de Hardware (La Revolución de la RTX 4060)
- **Causa:** Necesidad de fundamentar la promesa de "Ingeniería Real por $0.00" sin depender de la volatilidad de las cuotas gratuitas de la nube (Google/Groq).
- **Decisión:** Establecer la **RTX 4060 (8GB VRAM)** como el motor primario de inferencia local para tareas de Nivel 0, 1 y 2.
- **Configuración:** Uso de **Ollama** con el modelo **Qwen 2.5 Coder 7B (Q4/Q8)**. Este modelo cabe perfectamente en los 8GB de VRAM, permitiendo una latencia ultra-baja (<20ms) y una velocidad de generación superior a los 60 tokens/seg.
- **Impacto Narrativo:** El canal ahora tiene un "asistente local" que no consume tokens pagados, reforzando la imagen de Gustavo como un ingeniero que domina su propio metal.

### 43. El Stack Local "Zero-Cost" para el Canal
- **Causa:** El espectador debe ser capaz de replicar el workflow de Gustavo sin abrir la cartera.
- **Decisión:** Estandarizar la configuración de **Continue.dev (VS Code)** apuntando a `localhost:11434`.
- **Diferenciación:** Mientras otros canales enseñan a pagar $20/mes por ChatGPT Plus, Gustavo enseña a "hackerar" la productividad usando hardware que el gamer/dev promedio ya tiene (la serie 40 de NVIDIA).
- **Documentado en:** `config.json` (plantilla en HQ) y mención obligatoria en el EP02.

### 45. Optimización de Audio con IA (NVIDIA Broadcast)
- **Causa:** El micrófono actual (Trust GXT 232 Mantis) es de gama entrada y no proyecta la "Autoridad Senior" requerida por el canal.
- **Decisión:** Delegar el procesamiento de audio a la **RTX 4060** usando **NVIDIA Broadcast**.
- **Impacto:** Eliminación de ruido y eco vía hardware, convirtiendo un micro económico en una herramienta de audio profesional sin inversión adicional. Refuerza la narrativa de "Soberanía de Hardware".

### 46. Higiene Estructural Absoluta del HQ
- **Causa:** La auditoría "Byte a Byte" detectó contaminación de archivos de código (`db/`, `projects/`) y archivos temporales (`.csv`) en el HQ estratégico.
- **Decisión:** Eliminación inmediata de directorios de código y archivos de datos crudos del HQ.
- **Ley:** El HQ es el "Set de Grabación Estratégico". Solo residen guiones, specs y planes. El código vive en sus propios workspaces independientes en `Antigravity/`.

### 47. Profesionalización de Activos Visuales
- **Causa:** Presencia de archivos con nombres tipo hash (`7738452f...`) o con espacios, degradando la imagen de "Ingeniería Real".
- **Decisión:** Renombrar todos los assets a nomenclatura semántica (`thumbnail_draft_ep01`, `foto_perfil_alternativa`, etc.).

### 48. Estrategia de Cámara "Zero-Barrier"
- **Causa:** Incerteza sobre la compra de hardware de video inicial.
- **Decisión:** Iniciar el EP01 usando el **Smartphone (vía Camo Studio/Iriun)** como cámara principal.
- **Justificación:** La narrativa de "Ingeniero que optimiza lo que tiene" es más potente para el primer video que presumir equipo caro. La iluminación (LED/Aro) se prioriza sobre la cámara.

---
*Fin de registro de la mañana - 19-Jun-2026. HQ Limpio, Estrategia de Hardware blindada. Listo para Setup de OBS.*
