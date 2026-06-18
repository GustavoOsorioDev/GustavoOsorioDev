# CONTEXTO_PROYECTO.md
# Gustavo Osorio — @GustavoOsorioDev
# Documento de contexto para Claude — pegar al inicio de cada sesión
# Última actualización: 2026-06-19 (Mañana)

---

## INSTRUCCIÓN PARA CLAUDE

Eres mi asistente técnico y estratégico en el proyecto @GustavoOsorioDev.
Conoces todo el contexto de este documento. Retoma desde donde lo dejamos
sin preguntas innecesarias. Si necesitas más detalle sobre algo específico,
consulta el repo: github.com/GustavoOsorioDev/csdd-templates

---

## 1. QUIÉN SOY

- **Nombre:** Gustavo Osorio
- **Perfil:** Desarrollador backend con años de experiencia
- **Ubicación:** Caicedonia, Valle del Cauca, Colombia
- **Email:** gustsorio@gmail.com
- **Herramientas IA:** Claude principalmente, explorando otras
- **Propuesta de valor:** Traductor de ingeniería real al mundo hispanohablante

---

## 2. EL CANAL

- **Nombre:** Gustavo Osorio
- **Handle YouTube:** @GustavoOsorioDev
- **Handle GitHub:** GustavoOsorioDev
- **Tagline:** "Ingeniería real. Sin vibes."
- **Formato:** Build in Public — casos reales, specs, código en vivo
- **Frecuencia:** 1 video de alta calidad por semana
- **Audiencia:** Devs hispanohablantes 3-10 años de experiencia que usan IA pero no confían en ella ciegamente
- **Estado:** Canal creado, personalizado y publicado. Sin videos aún.

### 2.B Setup de Kaggle (Inferencia Gratuita)
Video temático: "Ingeniero de Software por $0.00".
- Notebook: GPU dual T4 recomendado.
- Script de automatización: Ver `estrategia/SCRIPTS_KAGGLE.py`.
- Modelo: Qwen2.5-Coder-32b (Quantized).
- Túnel: ngrok.

---

## 3. LA METODOLOGÍA — CSDD

**Contract-first Spec-Driven Development**

El código es una consecuencia del contrato, nunca al revés.

### Las 5 fases:
1. `CONSTITUTION.md` — reglas no negociables del proyecto
2. `contracts.md` — tipos, interfaces, eventos (Fase 1)
3. `spec.md` — historias de usuario, criterios de aceptación (Fase 2)
4. `plan.md` — arquitectura aprobada por el humano (Fase 3)
5. `tasks.md` — tareas atómicas rastreables (Fase 4)

### Diferenciador vs SDD genérico:
Los contratos entre componentes son el artefacto primario.
El código es desechable. Los contratos son permanentes.

---

## 4. REPOSITORIO GITHUB

**URL:** github.com/GustavoOsorioDev/csdd-templates
**Local:** C:\Users\Administrador\Documents\Antigravity\csdd-templates

### Estado actual del repo (2026-06-17):
```
csdd-templates/
├── CONSTITUTION.md       ✅ publicado
├── contracts.md          ✅ plantilla con ejemplo inline
├── spec.md               ✅ plantilla con ejemplo inline
├── plan.md               ✅ plantilla con ejemplo inline
├── tasks.md              ✅ plantilla con ejemplo inline
├── README.md             ✅ actualizado con estructura completa
├── logo_gustavo_osorio.svg
└── examples/
    └── taskflow-api/     ✅ ejemplo real completo (6 archivos)
        ├── CONSTITUTION.md
        ├── contracts.md
        ├── spec.md
        ├── plan.md
        ├── tasks.md
        └── README.md
```

**Pendiente:** hacer push al repo remoto con el commit:
`feat: complete CSDD ecosystem with templates and taskflow-api example`

### Convención de commits:
```
feat(contracts): descripción
fix(spec): descripción
docs(constitution): descripción
```

---

## 5. ESTRUCTURA LOCAL DEL CANAL

**Directorio:** C:\Users\Administrador\Documents\Antigravity\@GustavoOsorioDev

```
@GustavoOsorioDev/               ← HQ estratégico (NO vive código aquí)
├── CONTEXTO_PROYECTO.md         ← este archivo
├── BITACORA_DECISIONES.md       ← registro de decisiones (D1→D48)
├── auditoria_proyecto.md        ← auditoría técnica pre/post Refactor Seniority
├── checklist_produccion_video_1.md ← Fase 1 ✅ / Fase 2 ✅ / Fase 3 ⏳
├── assets/                      ← identidad visual (Nomenclatura Pro)
│   ├── logo_gustavo_osorio.svg
│   ├── logo_gustavo_osorio.png
│   ├── banner.png
│   ├── BigBanner.png
│   ├── perfil_pro_1.png
│   ├── perfil_pro_2.png
│   ├── thumbnail_draft_ep01.webp
│   └── foto_perfil_alternativa.webp
├── contenido/                   ← guiones, specs de episodios, miniaturas
│   ├── EP01_GUION.md            ← V4, avatar Miguel / El Constructor Solo
│   ├── EP02_SPEC.md             ← Spec del video RTX 4060 + LLM Local
│   ├── GUIA_ESTILO_NARRATIVO.md ← ADN de la marca @GustavoOsorioDev
│   └── PLANTILLA_EPISODIO.md
├── inteligencia/                ← análisis de audiencia y outputs del radar
│   ├── AUDIENCIA.md
│   ├── radar/                   ← histórico de hallazgos
│   └── analisis_audiencia_gustavo_osorio.html
└── estrategia/                  ← plan maestro, decisiones de negocio
    ├── PLAN MAESTRO-GustavoOsorioDev.pdf
    ├── RAZONAMIENTO_ESTRATEGICO.md
    ├── SETUP_IDE_CSDD.md        ← Stack VS Code+Cline+Qwen para el canal
    └── SCRIPTS_KAGGLE.py        ← Automatización de inferencia gratuita
```

> ⚠️ **Regla de arquitectura:** Este workspace es el Centro de Mando. No cohabitan proyectos de código aquí, independientemente de si son derivados o relacionados. Cada proyecto tiene su propio directorio independiente en `Antigravity/`.

**Proyectos de código independientes (fuera de este HQ):**
```
Antigravity/
├── @GustavoOsorioDev/     ← este HQ (estrategia, guiones, assets)
├── cazador-cli/           ← MVP público (ex cazador_v3.py) — Lead Magnet OSS
├── cazador-engine/        ← Motor privado comercial — Moat
└── csdd-templates/        ← Estándar metodológico público
```

---

## 6. EL CAZADOR — SISTEMA DE INTELIGENCIA

> El código de Cazador **NO vive en este workspace**. Proyecto independiente en `Antigravity/cazador-cli/`.

### Hardware:
- Mini PC local corriendo DietPi (x86_64, Intel Celeron N2930, 8GB RAM)
- Conectado 24/7 en IP residencial
- Entorno virtual: /root/cazador_env

### Proyecto:
- **Repo local:** `C:\Users\Administrador\Documents\Antigravity\cazador-cli`
- **Repo GitHub:** github.com/GustavoOsorioDev/cazador-cli (público — Lead Magnet)
- Instancia viva en DietPi: `/root/cazador-cli/`
- Fuentes: Reddit (9 subreddits), HackerNews, Dev.to, StackOverflow, YouTube Data API
- Cron: cada lunes 6AM UTC
- Output: `/root/radar_semanal_YYYY-MM-DD.csv`

### Credenciales:
- YouTube API Key: guardada en /root/.env_cazador (chmod 600)
- GitHub token: guardado en git credential store

### Subreddits monitoreados:
programming, learnprogramming, ChatGPTCoding, node, Python,
softwaredevelopment, ExperiencedDevs, webdev, devops

---

## 7. CONTENIDO — ESTADO ACTUAL

### Episodio 1 — PENDIENTE DE GRABAR
- Caso: "Autopsia de Cazador CLI"
- Dolor validado: Búsqueda manual de nichos toma horas; la IA alucina datos y rompe rate limits.
- Gancho: Construcción de un bot extractor de Reddit (Stealth RSS) bajo Spec-Driven Development.
- Guión: Terminado y validado en `contenido/EP01_GUION.md`

### Top casos capturados (radar_semanal_2026-06-17.csv):
1. Score 161.97 — "the juniors who only learned to code with AI..." (399 comments)
2. Score 122.16 — "Things I used to be proud of doing well..." (304 comments)
3. Score 106.18 — "I've been working with a Vibe Coder..." (264 comments)
4. Score 100.28 — "How to deal with juniors shipping AI slop code?" (250 comments)

### Gaps YouTube detectados:
1. Score 50.84 — "vibe coding solución arquitectura" (398 videos)
2. Score 50.59 — "csdd contract first development" (3 videos — VIRGEN)
3. Score 49.36 — "ai agents contracts microservices" (641 videos)
4. Score 25.01 — "microservicios contratos api español" (5,746 videos)

### Plan de contenido (Próximas 4 semanas - ESTRATEGIA CTR/RETENCIÓN):
- EP01: "Cómo automaticé mi 'Estudio de Mercado' (Autopsia Cazador CLI)" — Narrativa: Spec-Driven Development, Stealth RSS y el rate limit de Reddit.
- EP02: "Conecté una RTX 4060 a mi Bot de Reddit" — Narrativa: El refactor a la v4. Integrando un LLM local para clasificación semántica real de nichos (Pydantic + vLLM).
- EP03: "Odio editar, así que programé mi propia IA (Auto-Editor)" — Narrativa: Creación de la herramienta interna de recorte de audio y silencios en la RTX 3060 Ti.
- EP04: "Mi Junior casi destruye Producción con IA" — Narrativa: APIs rotas por alucinaciones de LLMs. Solución: Contratos de datos estrictos en Fase 1 (CSDD).

---

## 8. IDENTIDAD VISUAL

- Logo: GO circular, fondo negro (#0f0f0f), G teal (#1D9E75), OSORIO blanco
- Banner: foto real retocada por IA + tipografía limpia + teal
- Paleta: fondo #0f0f0f, principal #1D9E75, texto #ffffff, secundario #aaaaaa
- Tipografía: system-ui / sans-serif
- Assets en: `assets/`

---

## 9. ANÁLISIS DE AUDIENCIA (resumen)

- Avatar principal: "Miguel / El Constructor Solo" — 2-6 años exp., usa IA masivamente.
- Avatar secundario: "Sebastián / Valeria — El Dev Frustrado" — 4-8 años exp., busca control.
- Avatar terciario: "Carlos / Andrea — El Tech Lead Agotado" — revisa AI slop de juniors.

---

## 10. PRÓXIMOS PASOS TÁCTICOS Y PENDIENTES

### ✅ Completados (2026-06-19)
- [x] Auditoría integral "Byte a Byte" de YouTube realizada.
- [x] Limpieza estructural del HQ (Eliminados db/, projects/, movido radar.csv).
- [x] Profesionalización de nomenclatura de assets visuales.
- [x] Bitácora de Decisiones actualizada hasta D48.
- [x] Estrategia de Hardware (NVIDIA Broadcast + Smartphone Cam) definida.
- [x] Solución de deuda documental (Glosario, Guía de Estilo, Auditoría).

### ⏳ Próximo bloque — EP01 (Grabación)
- [ ] **[ÚNICO BLOQUEANTE]** Configurar OBS: captura editor modo oscuro + terminal.
- [ ] Limpiar secretos: asegurar que el `.env` no aparezca en pantalla.
- [ ] Prueba de vuelo: `python src/main.py` y confirmar resultados interesantes en < 30 segundos.
- [ ] Grabar Episodio 1 (Workflow "Modo Director").
- [ ] Diseñar miniatura EP01 y publicar.

### 🔜 Futuro — EP02 (Código nuevo)
- [ ] Diseñar diagramas de arquitectura (Regex vs LLM semántico) para EP01 en Excalidraw.
- [ ] Desarrollar `cazador_v4.py` (LiteLLM + RTX 4060) → EP02.
- [ ] Desarrollar `auto_editor.py` (Whisper + RTX 3060 Ti) → EP03.

---

## 11. COMANDOS ÚTILES

### DietPi (cazador-cli en producción):
```bash
source /root/cazador_env/bin/activate
python /root/cazador-cli/src/main.py
ls -lt /root/radar_semanal_*.csv | head -1
crontab -l
```

### GitHub (csdd-templates):
```bash
cd C:\Users\Administrador\Documents\Antigravity\csdd-templates
git add .
git commit -m "mensaje"
git push
```

---

### 12. Decisiones Estratégicas (Resumen)
- **ID D30-D41:** Firewall 2.0, Yield Protocol, Kaggle Scripts e IDE Setup.
- **ID D42-D44:** Soberanía de Hardware (RTX 4060), Qwen-7B y Qwen-1.5B Tab-Autocomplete.
- **ID D45-D48:** NVIDIA Broadcast, Limpieza HQ, Assets Pro y Estrategia de Cámara Zero-Barrier.

---

## 13. REPORTE DE SALUD (19-Jun-2026) ✅

| Componente | Estado | Acción Realizada |
|---|---|---|
| **Estrategia** | 🟢 ÓPTIMA | Auditoría YouTube finalizada. Bloqueos estratégicos levantados. |
| **Cazador-CLI** | 🟢 LISTO | Auditado, refactorizado y limpio del HQ. |
| **Documentación** | 🟢 SINCRO | HQ sin archivos fantasma. Bitácora D48. Guía Estilo v2. |
| **Soberanía IA** | 🟢 METAL | RTX 4060 configurada como motor primario local. |
| **Producción** | 🟡 PREDICCIÓN | Listo para setup de OBS y primera toma. |

---

Gustavo Osorio — @GustavoOsorioDev  
"Ingeniería real. Sin vibes."  
github.com/GustavoOsorioDev/csdd-templates  
*Última actualización: 19 de Junio de 2026 (Mañana) — Decisiones D42-D48 registradas*
