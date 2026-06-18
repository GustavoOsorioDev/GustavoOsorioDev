# MI ESTRATEGIA: YOUTUBE Y CREAR EN PÚBLICO (2026)

Aquí está el plan para convertir mi trabajo diario en contenido para el canal, asegurando que ganemos dinero y autoridad técnica sin dar vueltas.

---

## 1. EL CAMBIO DE RUMBO
- **Lo que no funcionó:** El canal de IA automatizada era demasiado arriesgado (YouTube nos podía borrar) y tomaba demasiado tiempo para lo que pagaba.
- **La Solución (Build in Public):** Grabo lo que programo de Lunes a Viernes y lo convierto en videos el fin de semana.
- **Nuestro Sello:** No enseñamos a programar desde cero. Enseñamos **Ingeniería Real, sin humo**. Nada de copiar y pegar prompts; aquí mostramos cómo mandar nosotros sobre la IA usando reglas y arquitectura sólida.
- **El Negocio real (Micro-SaaS):** No solo hacemos scripts. Creamos herramientas que yo mismo necesito para trabajar (Dogfooding). Si me sirven a mí, le sirven a mi audiencia, y ahí es donde está el dinero: ingresos por YouTube y suscripciones mensuales de gente que tiene mis mismos problemas.

---

## 2. LA AUDIENCIA Y EL AVATAR (PUNTOS DE DOLOR)
Nuestra estrategia se basa en datos reales de frustración técnica identificados en 2026. (Ver detalle en [AUDIENCIA.md](./inteligencia/AUDIENCIA.md)).

- **Target Principal (Sebastián/Valeria):** El desarrollador que usa IA pero siente que la base de código se está pudriendo. Busca **control**.
- **Target Secundario (Carlos/Andrea):** El Tech Lead que lucha contra el código basura generado por sus juniors. Busca **arquitectura**.
- **El Gap de Mercado:** El 46% de los desarrolladores ya no confía en la IA sin supervisión. Nosotros les damos la metodología para supervisar con rigor (CSDD).

---

## 3. ARQUITECTURA DE WORKSPACES Y REPOSITORIOS (CRÍTICO)

Para mantener la integridad operativa y la ilusión visual militar en cámara, los repositorios deben **dividirse estrictamente**. No mezclar logística del canal con código puro.

### A. Proyecto Principal (Logística y Cerebro)
**Directorio Actual:** `c:\Users\Administrador\Documents\Antigravity\@GustavoOsorioDev`
**Uso Oficial:** 
- Almacenaje de guiones.
- Planes de contenido y roadmaps.
- Miniaturas, recursos gráficos.
- Configuración global de prompts (GEMINI.md).
- *Aquí NO debe vivir el código base de las aplicaciones.*

### B. Proyectos Open Source (El Lead Magnet)
**Ejemplo:** `workspace/cazador-cli` (Actualmente tu MVP)
**Uso Oficial:**
- Herramientas pequeñas, crudas e hiper-útiles resolviendo un único problema.
- **Públicas en GitHub** para captar comunidad y leads.
- Deben incluir la carpeta `.specs/` visible en el editor.
- **Tecnología a lucir:** Python puro, SQLite (en lugar de CSV), Pydantic (para Contratos de Datos), y la librería `Rich` para un UI en terminal impactante.

### C. Proyectos Propietarios (El Foso Comercial)
**Ejemplo:** `c:\Users\Administrador\Documents\Antigravity\cazador-engine`
**Uso Oficial:**
- Tu orquestador empresarial Multi-Nichos.
- Motores pesados, web servers, arquitecturas complejas con múltiples fuentes.
- **Privado al 100%.** Nunca se sube a GitHub público.
- Usado para facturación real o encontrar nichos para tus verdaderas micro-apps rentables.

---

## 4. ECOSISTEMA GITHUB (@GustavoOsorioDev)

### A. [csdd-templates](https://github.com/GustavoOsorioDev/csdd-templates) (Público)
- **Función:** El estándar de la industria bajo tu marca.
- **Contenido:** Plantillas de CONSTITUTION, contracts, spec, plan y tasks.
- **Mantenimiento:** Debe actualizarse con ejemplos de Python/Pydantic para alinearse con el contenido del canal.

### B. [csdd-core](https://github.com/GustavoOsorioDev/csdd-core) (Privado)
- **Función:** Aplicación real de la metodología en tus proyectos de negocio.
- **Contenido:** Especificaciones de arquitectura interna y lógica propietaria.

---

## 5. EL EMBUDO DE CONTENIDO (FUNNEL)

### VIDEO 1: El Gancho (El Cazador CLI / MVP)
- **Concepto:** "Estaba perdiendo horas buscando qué app construir, así que construí en Python un bot local que analiza quejas en internet para encontrar nichos rentables automáticamente".
- **Formato:** Autopsia de código. NO desde cero. Abres el código ya hecho del MVP y lo recorres enseñando el contrato de Pydantic, la interfaz de terminal en `Rich`, y lo ejecutas en vivo.
- **CTA (Call to Action):** "Bájate esta herramienta gratuita en mi GitHub". = **Adquisición masiva de usuarios y autoridad.**

### VIDEO 2: La Autoridad (El Refactor Modular)
- **Concepto:** "Las palabras clave no son suficientes. Hoy refactorizo el Cazador CLI para inyectarle un 'cerebro' de IA local (LLM) que corre en mis propias tarjetas gráficas".
- **Formato:** Demostración de arquitectura modular. Cómo el código detecta el hardware y decide si usar Regex (Básico) o LLM (Pro). Uso de `Ollama` / `LiteLLM`.
- **Diferenciador:** Muestras el "detrás de cámaras" de tu granja de GPUs (RTX 3060/4060) trabajando en la inferencia mientras explicas el código.
- **CTA:** "Si no tienes GPU, úsalo en modo Regex o mira mi guía de Kaggle para correrlo gratis".

---

## 5.B EL MODELO DE MONETIZACIÓN (EL ECOSISTEMA CENTRAL)
No venderemos "suscripciones por herramienta individual" ni pagos únicos. Operaremos bajo el **Modelo de Créditos y API Key Central**.

1. **El Producto no es la app, es el Motor (Cómputo/API):** Se venden créditos de ejecución mensual ("Plan Builder: $20/mes = 10,000 créditos").
2. **El Embudo Anti-Fricción (Doble Nivel Gratis):**
   - *Gratis Permanente (Modo Local):* Las herramientas bajadas de GitHub operan en un modo "Zero-Quota" (Ej: Regex/RSS). Son útiles, previenen haters, pero no traen el poder mágico.
   - *Bolsa de Prueba (El "Aha! Moment"):* Al registrarse en `gustavo-hq.com` mediante **GitHub OAuth** (filtro anti-bots/freeloaders), reciben 500 créditos gratis. Obtienen una API Key secreta.
3. **Bloqueo y Migración (Lock-in):** Introducen la API Key en el CLI local. La herramienta pasa a "Modo AI", contacta al `cazador-engine` privado, y quema créditos revelando el verdadero valor. Al acabarse los 500 créditos, la conversión a pago es puramente orgánica.

---

## 6. PIPELINE DE PRODUCCIÓN AUTOMATIZADO
Para mantener el ritmo de 28h/semana, la producción de video no debe ser manual:
1. **Captura:** Grabación de pantalla en la RTX 2000 Ada (HQ).
2. **Carpintería (Asíncrona):** El audio se envía a la RTX 3060 Ti para transcripción automática (Whisper).
3. **Assets (Asíncrona):** La RTX 4060 genera visuales de apoyo vía ComfyUI basándose en el guion.
4. **Ensamblaje:** Edición minimalista en DaVinci Resolve enfocada en el flujo de nodos.

---

## 7. LA REGLA DE ORO: SPEC-DRIVEN DEVELOPMENT (SDD) EN PANTALLA

Consulta las definiciones detalladas en [GLOSARIO_METODOLOGICO.md](./GLOSARIO_METODOLOGICO.md).

Lo que destrozará a la competencia de otros canales de IA es tu enfoque de ingeniería limpia.
En CADA video, tu "set de grabación" debe incluir:
1. Una carpeta `.specs/` donde almacenas los prompts, el `AGENT.md` o el layout del sistema (Markdown).
2. Un discurso donde expliques que **"La IA es un Junior Developer. Tú eres el Tech Lead. Tú le das las especificaciones y ella te devuelve el código. El código no puede ir a producción sin una revisión arquitectónica".**
3. Para el paso a paso exacto en pantalla, seguir el [WORKFLOW_GRABACION_IA.md](./WORKFLOW_GRABACION_IA.md) (El "Modo Director").

*Este documento permanece en el workspace principal de @GustavoOsorioDev como el pilar fundamental que guía la producción del canal y el desarrollo de software.*

---

## 8. ESTADO ACTUAL DE LA INFRAESTRUCTURA (Junio 17, 2026)

- **Workspace HQ (@GustavoOsorioDev):** Preparado. Contiene estrategia y logística.
- **Proyecto Video 1 (cazador-cli):** [COMPLETADO] El núcleo `cazador_v3.py` fue refactorizado exitosamente para el Hito 1.
  - *Técnica:* Implementación de **"Sigilo RSS"** para eludir el error `403` de Reddit sin tokens.
  - *Filtrado:* Escáner de **patrones de frustración sintáctica** (ej. "nightmare", "struggling").
  - *Ingeniería:* Uso de `Pydantic` (Contrato de Datos) y `Rich` (Visualización Premium).
- **Ecosistema GitHub:** [LIMPIO] 5 repositorios antiguos eliminados. Solo quedan `csdd-templates` (público) y `csdd-core` (privado).
- **Foso Comercial (cazador-engine):** Estructura modular confirmada. Listo para el Video 2.
