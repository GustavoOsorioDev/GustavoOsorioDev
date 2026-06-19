# Glosario Metodológico: La Biblia del Seniority — @GustavoOsorioDev

Este documento define los pilares técnicos que separan este canal del "Vibe Coding" y el contenido genérico de IA.

## 1. SDD (Spec-Driven Development)
**Definición:** Metodología donde la especificación (el "qué") precede obligatoriamente a la implementación (el "cómo").
- **El Artefacto:** Archivos `.md` en la carpeta `.specs/`.
- **Uso con IA:** La especificación actúa como el "prompt maestro" de contexto. Sin especificación, no hay generación de código.
- **Narrativa de Canal:** Se vende como **Arquitectura primero, Teclado después**.

## 2. CSDD (Contract-First Spec-Driven Development)
**Definición:** Una especialización del SDD enfocada en la inmutabilidad y consistencia de los datos.
- **El Artefacto:** Modelos de datos (clases de Pydantic, Schemas SQL) definidos como el primer paso del desarrollo.
- **Uso con IA:** Forzar a la IA a respetar tipos de datos innegociables. El contrato es el "acuerdo legal" entre funciones.
- **Narrativa de Canal:** Se vende como **Robustez y Calidad de Producción**. 

## 3. Vibe Coding (Antipatrón a evitar)
**Definición:** Programar pegando prompts aleatorios a una IA hasta que "parezca" que funciona, sin entender la arquitectura subyacente.
- **Riesgo:** Código espagueti, deuda técnica instantánea y alucinaciones de la IA.
- **Posicionamiento:** Nuestro canal es el antídoto contra el Vibe Coding.

### 4. Firewall de Modelos 2.0
Sistema de clasificación de potencia de IA (Nivel 0 al 4) para optimizar costos y precisión.
- **Nivel 0 (Metal):** Tu GPU local (Gratis).
- **Nivel 3 (Arquitecto):** Claude Sonnet para contratos y lógica crítica.

### 5. Yield Protocol (Protocolo de Freno)
Procedimiento de seguridad donde el agente detiene una tarea de arquitectura si detecta el uso de un modelo insuficiente (Nivel 1/2), obligando al Director a autorizar el riesgo o cambiar de modelo.
- **Propósito:** Evitar "matar moscas a cañonazos" y demostrar eficiencia técnica real. En cámara, sirve para legitimar el uso de modelos pequeños para tareas simples y delegar el seniority a modelos grandes.

---
*Este glosario se actualizará con ejemplos de código una vez definido el Avatar y Público Objetivo.*

## 6. Cognitive Debt (Deuda Cognitiva)
**Definición:** Pérdida del modelo mental del software cuando el desarrollador acepta y aprueba código generado por IA sin comprender su lógica interna.
- **Peligro:** El software funciona temporalmente, pero se vuelve imposible de depurar o escalar en el futuro.
- **Prevención:** Jamás desplegar código que no podrías explicar línea por línea en una revisión de código.

## 7. Context Blindness (Ceguera de Contexto)
**Definición:** Falla arquitectónica donde la IA altera un componente de forma aislada, rompiendo dependencias, contratos o patrones globales debido a la falta de visión sistémica (Context Window limit).
- **Contramedida:** Obligar al modelo a revisar los artefactos del SDD (`.specs/`) o consultar el modelo de datos maestro antes de modificar funciones core.

## 8. Plausible Fake Code (Slop Plausible)
**Definición:** Código generado que es sintácticamente válido pero lógicamente roto, obsoleto o inseguro.
- **Peligro:** Desvía el esfuerzo del desarrollador de escribir código hacia depurar "alucinaciones lógicas". A menudo inyecta vulnerabilidades silenciosas.

## 9. Phantom Edit (Edición Fantasma)
**Definición:** Antipatrón donde un agente de IA declara haber realizado un cambio en un archivo —frecuentemente mostrando un diff simulado en el chat— sin que dicho cambio haya llegado al disco.
- **Peligro:** Es invisible. El historial de conversación muestra "trabajo hecho" pero la realidad del sistema es diferente. Es el equivalente documental del **Vibe Coding**: el código *parece* correcto pero la base real está podrida.
- **Contramedida:** El **Protocolo VERIFACT**. Todo cambio declarado debe adjuntar evidencia forense de disco (`[VERIFACT: OK]`) antes de ser reportado como completado.
- **Clasificación:** AI Slop Documental (Ítem 4 de la sección Cero Tolerancia en `GEMINI.md`).

