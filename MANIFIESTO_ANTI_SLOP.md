# MANIFIESTO ANTI-SLOP: LA DOCTRINA DE GOBIERNO AI

**"La IA es un Junior Developer. Tú eres el Tech Lead. El código no puede ir a producción sin supervisión arquitectónica."**

Este manifiesto define la taxonomía del código basura autogenerado ("AI Slop") y las contramedidas obligatorias que todo agente o pipeline de IA debe superar antes de integrar código al *Workspace* de @GustavoOsorioDev.

---

## LA TAXONOMÍA DEL "AI SLOP"

La deuda técnica impulsada por IA (AI Technical Debt) destruirá cualquier proyecto a escala si permitimos las siguientes anomalías:

### 1. Plausible Fake Code (Código Falso Plausible)
- **El Vector:** La IA genera código sintácticamente impecable que pasa los linters de Python o Node.js, pero contiene fallas sutiles de lógica, alucina librerías, inventa firmas de métodos (API misuses) o introduce vulnerabilidades de seguridad (*CWEs*) pasivas.
- **La Doctrina:** *Zero-Trust Validation*. El código no se confía por cómo se ve. Ninguna implementación se fusiona sin que un test o una ejecución por consola demuestre que produce el output esperado para un input crudo.

### 2. Context Window Blindness (Ceguera de Contexto)
- **El Vector:** Cuando se solicita modificar un archivo o resolver un bug local, la IA asume que el contexto visible es el sistema completo, y rompe acoplamientos remotos, ignora configuraciones de inyección de dependencias y destruye patrones de arquitectura heredados.
- **La Doctrina:** *Spec-Driven Context*. Obligación absoluta de consultar los contratos base (Pydantic / interfaces) y la documentación de arquitectura antes de proponer cambios que afecten más de un archivo.

### 3. Bloated Abstractions (Abstracciones Infladas)
- **El Vector:** La IA imita mal los patrones de diseño institucionales, escribiendo clases inútiles (Dumb Data Objects), envoltorios masivos sin funcionalidad (wrappers innecesarios) y abusando de importaciones para solucionar flujos que requieren simpleza funcional.
- **La Doctrina:** *Keep it Simple, Pure*. Preferencia inamovible por funciones puras. Mutaciones y side-effects deben estar herméticamente aislados. Cada abstracción debe justificarse financieramente (en términos de carga cognitiva y tokens).

### 4. UI Truncation (Truncamiento UI y Silencio de Código)
- **El Vector:** Para acelerar respuestas, la IA imprime fragmentos con comentarios del estilo `<!-- ... existing code ... -->`, `//...` omitiendo lógica crítica, lo que provoca la eliminación accidental de componentes vivos si el humano hace "copy-paste".
- **La Doctrina:** *Balance 1 a 1*. Prohibición estricta de truncar código en herramientas de escritura en disco (`multi_replace` o reemplazos de bloque). La IA debe modificar el código respetando la exactitud del entorno preexistente.

### 5. Ediciones Fantasma (Phantom Edits)
- **El Vector:** La IA declara sistemáticamente en su output que el código "se ha implementado" y muestra diffs elaborados con resultados que jamás son escritos en el disco. AI Slop del nivel documental.
- **La Doctrina:** *VERIFACT Protocol*. Verificación forense tras cada edición. "Lo que no se puede verificar en disco, no ocurrió".

---

## EL PROTOCOLO DE DEUDA COGNITIVA

La "Deuda Cognitiva" es el costo de mantener un software temporalmente funcional creado por una entidad que comprendió algo que el operador humano (el Arquitecto) ignoró. 
**Regla Máxima:** Nunca aceptes bloques masivos de una generación de caja negra. El desarrollador ("Sebastián") jamás debe perder su modelo mental del proyecto. Si "funciona, no lo toques" NO APLICA si el creador no sabe *por qué* funciona.

---
*Este manifiesto es la base filosófica del contenido de "Ingeniería Real" en YouTube. Toda herramienta generada respetará estas directrices.*
