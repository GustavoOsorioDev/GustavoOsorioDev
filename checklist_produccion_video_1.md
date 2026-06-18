# Checklist Táctico: Producción Video 1 (Cazador CLI)

Este documento contiene las tareas técnicas necesarias para que el proyecto `cazador-cli` esté "listo para cámara".

## 🛠️ Fase 1: Refactor "Seniority" (En `cazador-cli/src`)
- [x] **Validación con Pydantic:** Reemplazar los diccionarios de `base_datos.append({})` por un esquema de Pydantic robusto.
- [x] **Refactor SQLite:** Cambiar el guardado de CSV a una base de datos SQLite local (`db/cazador.db`).
- [x] **UI de Terminal (Rich):** Implementar tablas y barras de progreso elegantes de la librería `Rich`.
- [x] **Manejo de Errores Profesional:** Añadir Try/Except específicos para Rate Limits (429) y que se vean con estilo en la terminal.

## 📄 Fase 2: Documentación de Soporte (Spec-Driven)
- [x] **Finalizar `01_data_contract.md`:** Asegurar que coincida exactamente con el esquema de Pydantic.
- [x] **Crear `ROADMAP.md` del Lite:** Poner 3 o 4 features futuras para que el espectador quiera seguir el canal.

## 🎥 Fase 3: Preparación del Set (Grabación)
- [ ] **Configurar OBS:** Captura de pantalla del editor (Modo Oscuro) + Terminal.
- [ ] **Limpiar Secretos:** Asegurar que el `.env` no se vea o que solo se vea el `.env.example`.
- [ ] **Prueba de Vuelo:** Correr el bot completo y confirmar que arroja resultados interesantes en los primeros 30 segundos.

---
*Nota: No grabar hasta que todos los puntos de la Fase 1 y 2 estén marcados.*
