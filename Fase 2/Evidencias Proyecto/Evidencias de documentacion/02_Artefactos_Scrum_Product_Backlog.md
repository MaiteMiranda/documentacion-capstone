# 🔄 Artefactos Scrum, Product Backlog y Planificación - BarrioStock

---

## 1. Product Vision Statement

> *"Para los almaceneros de barrio que sufren pérdidas por alimentos vencidos y descontrol en sus anotaciones en papel, **BarrioStock** es un sistema web de punto de venta (POS) e inventario inteligente que automatiza los descuentos FEFO y digitaliza el cuaderno de fiados con avisos por WhatsApp; a diferencia de los sistemas POS tradicionales costosos y rígidos, nuestra solución opera a **$0 costo**, es intuitiva y conecta la oferta del almacén con los vecinos en tiempo real."*

---

## 2. Definition of Ready (DoR) y Definition of Done (DoD)

### Definition of Ready (DoR)
Una Historia de Usuario está lista para ser ingresada al Sprint cuando:
1. Está redactada en formato ágil (`Como... Quiero... Para...`).
2. Cuenta con Criterios de Aceptación claros e inmutables.
3. El prototipo de pantalla en Figma (si aplica) está diseñado y aprobado.
4. El contrato de API JSON equivalente se encuentra documentado en `API_CONTRACT.md`.
5. Se encuentra estimada en Puntos de Historia (Fibonacci: 1, 2, 3, 5, 8).

### Definition of Done (DoD)
Una Historia de Usuario se considera **COMPLETAMENTE TERMINADA** cuando:
1. El código fuente se encuentra integrado en la rama `main` del Monorepo en Git.
2. Se cumple con la arquitectura limpia y validación de tipos Pydantic en FastAPI.
3. El componente React cumple con los estándares del Design System en Tailwind.
4. La base de datos Oracle 23c ejecuta la consulta sin errores de integridad.
5. Se probó el funcionamiento local en el contenedor de Docker Compose.

---

## 3. Product Backlog Completo

### 🟢 ÉPICA 1: Punto de Venta (POS) y Motor FEFO
* **HU01 - Escaneo de Código de Barras y Motor FEFO (8 SP) [Backend - Karen]:** Escaneo de productos detectando lotes a vencer (`dias <= 3`) y aplicando -30% OFF en boleta.
* **HU02 - Grilla de Productos Frecuentes y Carrito Táctil (5 SP) [Frontend - Maite]:** Interfaz visual por categorías, selección táctil de productos y badges de descuento.
* **HU03 - Procesamiento y Cierre de Venta (8 SP) [Fullstack - Karen/Maite]:** Pago en Efectivo/Tarjeta, descuento de stock inmutable en Oracle DB y emisión de comprobante.

### 🔵 ÉPICA 2: Cuaderno Digital de Fiados y Créditos
* **HU04 - Modal "Anotar en Fiado" y Control de Límite (5 SP) [Frontend - Maite]:** Asignación de venta a cliente comprobando que `saldo_deuda + compra <= limite_credito`.
* **HU05 - Registro de Abonos a Deuda (5 SP) [Fullstack - Karen/Maite]:** Registro de pagos en efectivo/transferencia restando saldo deudor en la tabla `CLIENTES`.

### 🟣 ÉPICA 3: Notificaciones de Cobranza (Meta Cloud API)
* **HU06 - Recordatorio de Cobro por WhatsApp Sandbox (8 SP) [Backend - Karen]:** Envío de mensajes automáticos formateados a través de Meta Cloud API.

### 🟢 ÉPICA 4: Catálogo Público PWA (Ofertas Express)
* **HU07 - Vista Pública Móvil para Vecinos (5 SP) [Frontend - Maite]:** Portal responsive para consulta de productos FEFO rebajados en tiempo real.

---

## 4. Sprint Backlog y Planificación de Sprints

| Sprint | Enfoque Principal | Historias Incluidas | Entregables Clave |
|---|---|---|---|
| **Sprint 1** | Arquitectura & Setup | Setup Base | Docker Oracle 23c, FastAPI base, React Setup, `API_CONTRACT.md`. |
| **Sprint 2** | Motor FEFO & POS | HU01, HU02, HU03 | Endpoint escaneo, algoritmo vencimiento, carrito táctil POS. |
| **Sprint 3** | Fiados & Meta API | HU04, HU05, HU06 | Modal créditos, registro abonos, integración WhatsApp Sandbox. |
| **Sprint 4** | PWA & QA Final | HU07, Pruebas E2E | Vista pública vecinos, optimización móvil, informe final. |

---

## 5. Acta de Retrospectiva (Sprint 1)

| Cuestionamiento | Observación del Equipo | Acción de Mejora Aceptada |
|---|---|---|
| **¿Qué funcionó bien?** | Rápida definición de arquitectura Monorepo, Docker Compose y maquetación en Figma. | Mantener la convención de Git y contratos JSON. |
| **¿Qué salió mal?** | Error de espacio en disco (`ENOSPC`) al instalar dependencias de Node.js en Windows. | Redirigir la caché global de `npm` al disco secundario `D:`. |
| **¿Qué descubrimos?** | La selección manual de caja en el Login agregaba pasos innecesarios. | Fijar `Caja 1` por defecto para optimizar la velocidad del POS. |

---

## 6. Cronograma de Trabajo y Carta Gantt

| Fase | Sprint / Módulo | Tarea / Entregable | Responsable | Semanas | Estado |
|---|---|---|---|---|---|
| **Fase 1** | **Sprint 0** | Levantamiento de Requisitos y Ficha de Inicio | Equipo (Karen/Maite) | Sem 1-2 | ✅ Finalizado |
| **Fase 1** | **Sprint 0** | Prototipado UX/UI en Figma y Design System | Maite Miranda | Sem 3-4 | ✅ Finalizado |
| **Fase 1** | **Sprint 0** | Modelo Relacional Oracle 23c (3FN) y Scripts SQL | Karen Fernández | Sem 4-5 | ✅ Finalizado |
| **Fase 2** | **Sprint 1** | Setup Monorepo, Docker Compose Oracle y API Contract | Karen Fernández | Sem 6-7 | ✅ Finalizado |
| **Fase 2** | **Sprint 1** | Setup React + Vite, TailwindCSS y Rutas Base | Maite Miranda | Sem 6-7 | 🔄 En curso |
| **Fase 2** | **Sprint 2** | API REST Escaneo, Lotes y Motor FEFO (FastAPI) | Karen Fernández | Sem 8-9 | 📅 Programado |
| **Fase 2** | **Sprint 2** | Frontend POS Táctil, Carrito y Alerta FEFO | Maite Miranda | Sem 8-9 | 📅 Programado |
| **Fase 2** | **Sprint 3** | Backend Fiados, Créditos y Meta Cloud API | Karen Fernández | Sem 10-11 | 📅 Programado |
| **Fase 2** | **Sprint 3** | Pantalla Fiados, Modales Abono/WhatsApp y PWA | Maite Miranda | Sem 10-11 | 📅 Programado |
| **Fase 2** | **Cierre F2** | Pruebas de Integración y Documentación Fase 2 | Equipo (Karen/Maite) | Sem 12 | 📅 Programado |
| **Fase 3** | **Sprint 4** | Pruebas de Carga, QA y Seguridad | Karen Fernández | Sem 13-14 | 📅 Programado |
| **Fase 3** | **Sprint 4** | Pulido UI/UX, Despliegue y Manual de Usuario | Maite Miranda | Sem 13-14 | 📅 Programado |
| **Fase 3** | **Defensa** | Informe Final, Presentación Ejecutiva y Exposición | Equipo (Karen/Maite) | Sem 15-16 | 📅 Programado |

> **Tablero de Control Trello:** `https://trello.com/b/barriostock-capstone-2026`