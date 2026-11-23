# Product Backlog — BarrioStock

## 1. Prioridad

- **Must:** imprescindible para el MVP.
- **Should:** importante.
- **Could:** deseable.
- **Won't:** fuera del MVP actual.

## 2. Product Backlog priorizado

| Orden | ID | Historia de usuario | Prioridad | Estado |
|---:|---|---|---|---|
| 1 | HU01 | Como usuario quiero iniciar sesión con RUT y contraseña | Must | Implementada |
| 2 | HU02 | Como cajero quiero escanear o buscar productos | Must | Implementada |
| 3 | HU03 | Como cajero quiero aplicar reglas FEFO | Must | Implementada |
| 4 | HU04 | Como cajero quiero modificar las cantidades del carrito | Must | Implementada |
| 5 | HU05 | Como cajero quiero registrar ventas en efectivo | Must | Implementada |
| 6 | HU06 | Como cajero quiero registrar ventas con tarjeta | Must | Implementada |
| 7 | HU07 | Como cajero quiero registrar ventas fiadas | Must | Implementada |
| 8 | HU08 | Como administrador quiero registrar clientes | Must | Implementada |
| 9 | HU09 | Como administrador quiero definir límites de crédito | Must | Implementada |
| 10 | HU10 | Como almacenero quiero registrar abonos | Must | Implementada |
| 11 | HU11 | Como administrador quiero gestionar productos | Should | Implementada |
| 12 | HU12 | Como administrador quiero recibir lotes | Must | Implementada |
| 13 | HU13 | Como administrador quiero importar desde CSV o `.xlsx` | Should | Implementada |
| 14 | HU14 | Como usuario quiero consultar alertas FEFO | Should | Implementada |
| 15 | HU15 | Como usuario quiero consultar el historial | Should | Implementada |
| 16 | HU16 | Como usuario quiero enviar recordatorios por Telegram | Should | Implementada |
| 17 | HU17 | Como vecino quiero consultar ofertas públicas | Should | Implementada |
| 18 | HU18 | Como administrador quiero visualizar indicadores | Should | Implementada |
| 19 | HU19 | Como usuario quiero usar la aplicación desde celular | Should | Implementada |

## 3. Criterios generales de aceptación

Una historia se acepta si:

- Cumple el flujo principal.
- Tiene validaciones.
- Muestra mensajes en español.
- Utiliza API REST.
- Conserva la consistencia de datos.
- Es responsive cuando corresponde.
- Incluye una prueba o evidencia.
- Se encuentra documentada.

## 4. Sprint 1 — Base técnica

### Sprint Backlog

- Configurar React y Vite.
- Crear estructura FastAPI.
- Diseñar modelo Oracle.
- Crear Dockerfiles.
- Crear Docker Compose.
- Definir variables de entorno.
- Crear contrato API.
- Implementar login.
- Implementar autenticación Bearer.
- Crear datos de prueba.

### Entregables

- Frontend accesible.
- Backend operativo.
- Base Oracle inicializada.
- Login funcional.
- Contrato API.

### Criterios de aceptación

- El login responde correctamente.
- Un RUT inválido recibe un mensaje español.
- La contraseña vacía es rechazada.
- El token permite acceder a rutas protegidas.
- Las rutas administrativas requieren ADMIN.
- Docker Compose levanta los servicios.

## 5. Sprint 2 — POS y FEFO

### Sprint Backlog

- Crear pantalla POS.
- Buscar productos.
- Implementar lector USB como teclado.
- Crear carrito.
- Modificar cantidades.
- Implementar FEFO.
- Crear alertas.
- Registrar ventas.
- Actualizar stock.

### Entregables

- POS funcional.
- Motor FEFO.
- Ventas en efectivo, tarjeta y fiado.
- Alertas.

### Criterios de aceptación

- Un código existente muestra el producto y lote.
- Un código inexistente muestra error.
- Entre 1 y 3 días aplica 30%.
- Entre 4 y 7 días aplica 15%.
- Sobre 7 días no aplica descuento.
- Una venta disminuye el stock.
- Una venta vacía no puede procesarse.
- Una venta FEFO aplica el precio correcto.

## 6. Sprint 3 — Fiados, abonos y Telegram

### Sprint Backlog

- Crear y editar clientes.
- Validar RUT.
- Validar límite de crédito.
- Consultar deuda.
- Registrar abonos.
- Historial individual.
- Generar recordatorios.
- Integrar Telegram.

### Entregables

- Cuaderno digital.
- Control de abonos.
- Historial de clientes.
- Telegram.

### Criterios de aceptación

- Un RUT inválido es rechazado.
- Un cliente duplicado no puede registrarse.
- Un abono no puede superar la deuda.
- Un límite no puede ser menor que la deuda.
- Una venta fiada no puede exceder el límite.
- Telegram recibe el Chat ID configurado.
- Cliente sin Chat ID recibe un mensaje apropiado.

## 7. Sprint 4 — Inventario, PWA y cierre

### Sprint Backlog

- Crear productos.
- Actualizar productos.
- Gestionar proveedores.
- Recibir lotes.
- Importar CSV.
- Importar `.xlsx`.
- Crear catálogo público.
- Implementar PWA.
- Ejecutar pruebas.
- Documentar despliegue.
- Revisar responsive.

### Entregables

- Inventario administrativo.
- Importación masiva.
- PWA pública.
- Pruebas automatizadas.
- Manual técnico.

### Criterios de aceptación

- Un CSV UTF-8 válido importa productos.
- Un `.xlsx` válido importa productos.
- Encabezados faltantes generan error.
- Una recepción actualiza stock.
- El catálogo público muestra ofertas.
- El header funciona en computador y celular.
- El build y lint finalizan correctamente.

## 8. Definición de Done

Una historia finalizada debe:

1. Encontrarse integrada al repositorio.
2. Cumplir criterios de aceptación.
3. Validar datos de entrada.
4. Manejar errores en español.
5. Usar autenticación cuando corresponde.
6. Mantener consistencia de inventario y saldo.
7. Tener al menos una prueba o evidencia.
8. Contar con documentación relevante.
9. Funcionar en el entorno local.