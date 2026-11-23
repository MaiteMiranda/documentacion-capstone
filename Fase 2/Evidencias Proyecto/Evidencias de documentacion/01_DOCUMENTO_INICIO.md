# Documento de Inicio del Proyecto — BarrioStock

## 1. Identificación del proyecto

**Nombre:** BarrioStock  
**Tema:** Plataforma digital para almacenes y minimarkets de barrio  
**Integrantes:** Maite Miranda y Karen Fernández  
**Metodología:** Scrum adaptado  

BarrioStock integra punto de venta, inventario por lotes, motor FEFO, fiados digitales, historial de operaciones, catálogo público PWA y notificaciones mediante Telegram.

## 2. Problema identificado

Los almacenes de barrio presentan dos problemas principales:

### 2.1 Pérdidas por vencimiento

Los productos perecibles suelen administrarse sin priorizar automáticamente la fecha de vencimiento. Esto genera:

- Productos vencidos en la venta.
- Falta de alertas oportunas.
- Pérdidas económicas.
- Desperdicio de alimentos.
- Dificultad para aplicar descuentos preventivos.

### 2.2 Descontrol de ventas fiadas

Las ventas a crédito suelen registrarse en cuadernos físicos. Esto provoca:

- Falta de historial.
- Errores en cálculos de deuda.
- Ausencia de control de límites.
- Dificultad para identificar morosidad.
- Registro incompleto de abonos.
- Cobranza manual.

## 3. Oportunidad

Existe la oportunidad de ofrecer una solución accesible que utilice:

- Tecnología web.
- Lector USB de códigos de barras.
- Inventario por lotes.
- Descuentos preventivos.
- Cuenta corriente digital.
- Notificaciones por Telegram.
- Ejecución local mediante Docker.
- Aplicación pública PWA.

## 4. Objetivos

### Objetivo general

Desarrollar una plataforma web que permita administrar ventas, inventario por lotes, vencimientos FEFO y fiados digitales en almacenes de barrio.

### Objetivos específicos

1. Implementar autenticación por RUT y contraseña.
2. Crear un POS responsive.
3. Incorporar escaneo mediante lector USB o ingreso manual.
4. Aplicar descuentos FEFO.
5. Registrar ventas en efectivo, tarjeta y fiado.
6. Administrar clientes y límites de crédito.
7. Registrar abonos.
8. Gestionar inventario y proveedores.
9. Importar productos desde CSV o Excel.
10. Mostrar catálogo público PWA.
11. Enviar recordatorios mediante Telegram.
12. Contener frontend, backend y base de datos mediante Docker.
13. Implementar pruebas unitarias y de integración.

## 5. Usuarios y stakeholders

| Actor | Interés |
|---|---|
| Administrador | Control de inventario, ventas, usuarios y reportes |
| Almacenero | Operación general del negocio |
| Cajero | Registro de ventas y cobros |
| Cliente con fiado | Conocer deuda y realizar abonos |
| Vecino | Consultar ofertas públicas |
| Maite Miranda | Desarrollo frontend y documentación |
| Karen Fernández | Backend, datos, seguridad y QA |
| Profesor o evaluador | Validación técnica y académica |

## 6. Alcance del MVP

### Incluido

- Login con token Bearer.
- Rol ADMIN y rol CAJERO.
- POS.
- Motores FEFO.
- Ventas.
- Clientes.
- Fiados.
- Abonos.
- Inventario.
- Recepción de lotes.
- Productos frecuentes.
- Alertas FEFO.
- Historial general e individual.
- Importación CSV o `.xlsx`.
- Catálogo PWA público.
- Telegram.
- Docker Compose.
- Oracle 23c.
- Pruebas automatizadas.

### Implementación técnica

- React 19.
- Vite.
- Tailwind CSS.
- FastAPI.
- Python.
- Pydantic.
- Oracle 23c.
- Axios.
- Docker y Docker Compose.
- Railway para opciones de despliegue independientes.
- Telegram Bot API.

## 7. Fuera del alcance inicial

- Escaneo por cámara.
- Integración bancaria real.
- Integración con Transbank.
- Boleta electrónica SII.
- Nómina.
- Contabilidad.
- Facturación electrónica.
- Múltiples sucursales.
- Aplicación móvil nativa.

## 8. Restricciones

- Capacidad limitada de memoria en entornos locales o gratuitos.
- Oracle Database puede requerir más recursos que un contenedor ligero.
- Telegram requiere Chat ID registrado.
- Los lectores USB actúan como teclado.
- La aplicación depende de conexión al servidor y a la base.
- Railway requiere servicios independientes.
- No se debe exponer información sensible en variables públicas.
- El catálogo público no requiere autenticación.
- Las rutas administrativas requieren Bearer Token.

## 9. Supuestos

- El almacén utiliza un lector USB o ingresará códigos manualmente.
- Los administradores conocerán las credenciales asignadas.
- Los clientes recibirán Telegram solo si registraron Chat ID válido.
- Oracle se ejecutará mediante Docker o en un entorno con recursos suficientes.
- Las fechas de vencimiento se registrarán al recibir inventario.

## 10. Riesgos

| Riesgo | Impacto | Mitigación |
|---|---|---|
| Oracle se queda sin memoria | Indisponibilidad persistente | Aumentar recursos o utilizar un plan adecuado |
| Chat ID incorrecto | Fallo de Telegram | Validar y almacenar el Chat ID |
| RUT inválido | Registro incorrecto | Validación con dígito verificador |
| Importación mal preparada | Datos incorrectos | Validar columnas y tipos |
| Producto sin lote | No puede venderse correctamente | Validar recepción de inventario |
| Duplicación de código | Conflictos de catálogo | Validar código único |
| Fallo de red | API no disponible | Mostrar mensajes y modo fallback |

## 11. Criterios de éxito

El proyecto se considera exitoso cuando:

- El usuario puede iniciar sesión.
- El POS registra ventas.
- FEFO calcula descuentos correctamente.
- Una venta reduce el stock.
- Fiado aumenta la deuda.
- El abono reduce la deuda.
- Se crea y modifica inventario.
- CSV y `.xlsx` pueden cargarse.
- Telegram puede enviar o simular una notificación.
- La interfaz funciona en celular y computador.
- Las pruebas aprobadas respaldan las reglas implementadas.

## 12. Metodología

Se utilizará Scrum adaptado:

- Sprints de dos semanas.
- Product Backlog priorizado.
- Sprint Backlog.
- Revisión al finalizar cada Sprint.
- Retrospectiva.
- Trabajo asincrónico.
- API-First.
- Integración continua durante el desarrollo.
- Evidencias por Sprint.