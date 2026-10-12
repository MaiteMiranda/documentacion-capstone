## 1. Documento de Inicio de Proyecto (PID)

### 1.1. Problema Identificado
Los almacenes y minimarkets de barrio en Chile enfrentan dos pérdidas operativas y financieras críticas:
1. **Mermas por Vencimiento (Pérdida FEFO):** Falta de control sobre las fechas de caducidad en mercadería perecible, provocando que productos vencen en repisa sin venderse.
2. **Morosidad e Ineficiencia en Fiados:** El registro manual de deudas en cuadernos de papel genera pérdidas de dinero, cobros desfasados y falta de límites de crédito claros para los vecinos.

### 1.2. Objetivos del Proyecto
* **Objetivo General:** Desarrollar e implementar un sistema web integral (POS + Fiado Digital + PWA) que reduzca la merma por vencimiento mediante un motor FEFO y automatice la cobranza por WhatsApp.
* **Objetivos Específicos:**
  * Implementar un algoritmo FEFO que aplique descuentos dinámicos en caja antes del vencimiento.
  * Crear un módulo de cuaderno digital con verificación estricta de límites de crédito.
  * Integrar Meta Cloud API (WhatsApp Sandbox) para notificaciones de cobro automáticas a $0 costo.
  * Desplegar una PWA pública para la consulta de "Ofertas Express" por parte de los vecinos.

### 1.3. Matriz de Stakeholders (Actores de Interés)
* **Cajero / Almacenero:** Usuario primario del sistema POS y panel de fiados.
* **Vecinos / Clientes del Barrio:** Beneficiarios de las Ofertas Express vía PWA y receptores de avisos de cobro vía WhatsApp.
* **Karen Fernández:** *Backend, Data & QA Lead* (API REST FastAPI, Oracle 23c y motor FEFO).
* **Maite Miranda:** *Frontend, UI/UX & Project Lead* (Diseño Figma, React + Vite y gestión Scrum).
* **Comisión Académica Evaluadora:** Entidad revisora de la asignatura Capstone.

### 1.4. Alcance del MVP (Producto Mínimo Viable)
* **Incluido:** Autenticación de usuarios, lectura de código de barras, motor de descuento FEFO dinámico, gestión de cuentas corrientes con límite de crédito, envío de WhatsApps vía Sandbox, catálogo público PWA y contenedorización en Docker.
* **Excluido del MVP:** Transbank POS físico integrado, boleta electrónica oficial SII (simulada localmente) y facturación electrónica a proveedores.

### 1.5. Restricciones del Proyecto
* **Presupuesto Financiero:** Presupuesto estrictamente de **$0 USD** en infraestructura y licencias.
* **Tiempo:** 16 semanas de desarrollo en el semestre académico 2026.
* **Base de Datos:** Uso obligatorio de Oracle Database 23c Free.

### 1.6. Justificación
BarrioStock democratiza la tecnología de inventarios para pequeños comerciantes que no pueden costear licencias costosas, entregando una herramienta moderna y alineada con la economía circular de "Salva Alimentos".

---

## 2. Metodología Declarada y Justificada (Scrum)

### 2.1. Declaración del Marco Metodológico
Se declara el uso de la metodología ágil **Scrum**, adaptada a un equipo de 2 integrantes (*Scrum de Pareja*), organizando el desarrollo en **Sprints de 2 semanas de duración**.

### 2.2. Justificación de la Elección
1. **Flexibilidad e Incrementalidad:** Permite ajustar prototipos en Figma y contratos de API (`API_CONTRACT.md`) en cada entrega académica sin congelar el alcance de forma rígida.
2. **Entregables Funcionales:** Garantiza que al cierre de cada Sprint se obtenga un incremento de software utilizable (ej. Docker con Oracle 23c en Sprint 1, Motor FEFO en Sprint 2).
3. **División Eficiente de Trabajo:** Separa el desarrollo Frontend (Maite) y Backend/BD (Karen) mediante interfaces JSON estandarizadas.

### 2.3. Roles y Ceremonias Adaptadas
* **Scrum Master / PO (Maite Miranda):** Gestión de Trello, prototipado UI/UX y Frontend.
* **Lead Developer / QA (Karen Fernández):** Arquitectura de software, Oracle 23c, FastAPI y Meta API.
* **Ceremonias:** Planning quincenal, Daily asíncrona (WhatsApp/Discord), Review y Retrospectiva por Sprint.

---

## 3. Declaración de Innovación y Valor Agregado

* **¿Qué problema resuelve?** Elimina la pérdida económica por alimentos vencidos en minimarkets y moderniza la libreta de fiados sin costos operativos.
* **¿Qué lo hace diferente?** Integra el algoritmo logístico industrial FEFO directo en la lectura del scanner del POS, aplicando descuentos de forma automática e imperceptible para el cajero.
* **Propuesta de Valor:** Democratiza la API oficial de WhatsApp en el comercio de barrio y conecta la oferta con la comunidad bajo el concepto de economía circular ("Salva Alimentos").