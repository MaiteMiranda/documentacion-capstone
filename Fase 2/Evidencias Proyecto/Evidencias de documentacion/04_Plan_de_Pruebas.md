## 1. Objetivo

Definir las pruebas necesarias para verificar que los componentes principales de BarrioStock funcionen de acuerdo con las reglas de negocio documentadas: consulta y venta de productos, selección de lotes mediante FEFO, aplicación de descuentos por vencimiento, administración de fiados, persistencia en Oracle Database 23c e integración de notificaciones mediante Meta Cloud API.

## 2. Alcance

Se consideran los siguientes módulos y componentes:

- **POS:** consulta/registro de productos y procesamiento de ventas.
- **Motor FEFO:** selección del lote disponible con vencimiento más próximo y aplicación de la regla de descuento configurada.
- **Fiados:** registro de deuda por cliente, validación del límite de crédito y registro de abonos.
- **Notificaciones:** comunicación con WhatsApp mediante Meta Cloud API en ambiente Sandbox.
- **API REST:** validación de solicitudes y respuestas JSON de acuerdo con `API_CONTRACT.md`.
- **Base de datos:** persistencia, integridad referencial y estructura relacional en 3FN.
- **Frontend:** flujo principal del POS y visualización de la PWA/catálogo.
- **Infraestructura:** arranque de Oracle mediante Docker Compose.
- **Rendimiento:** pruebas de estrés con JMeter, planificadas para una etapa posterior.


## 3. Estrategia y tipos de prueba

| Tipo de prueba | Propósito | Herramienta / técnica | Momento |
|---|---|---|---|
| Unitaria | Comprobar de forma aislada las reglas del motor FEFO y validaciones de negocio. | Pruebas de funciones y servicios del backend; framework de testing por confirmar en el proyecto. | Durante el desarrollo del backend. |
| Funcional | Verificar los flujos visibles del POS, ventas, fiados y catálogo PWA. | Ejecución de casos paso a paso en la interfaz. | Cuando estén disponibles las vistas y datos necesarios. |
| API | Comprobar solicitudes, respuestas, validaciones y errores de los servicios REST. | Postman y Postman Collections, contrastando con `API_CONTRACT.md`. | A medida que se habiliten los endpoints. |
| Integración | Verificar el intercambio entre frontend, backend, Oracle y Meta Sandbox. | Postman, logs de aplicación y revisión de datos persistidos. | Una vez disponibles los módulos integrados. |
| Base de datos | Verificar integridad, persistencia y estructura del modelo relacional. | Consultas SQL sobre Oracle Database 23c. | Después de inicializar el esquema y cargar datos de prueba. |
| Infraestructura | Confirmar que los servicios puedan levantarse en el entorno definido. | Docker Compose y revisión de logs/estado de contenedores. | En cada ambiente de desarrollo o integración. |
| No funcional / carga | Evaluar comportamiento bajo concurrencia y carga. | Apache JMeter. | Planificado para semanas 11 a 15 en el informe de Fase 2. |

## 4. Ambiente y datos de prueba

### 4.1 Ambiente

- Oracle Database 23c Free ejecutado mediante Docker Compose.
- Backend Python 3.11 con FastAPI.
- Frontend React 18, Vite y TailwindCSS.
- Contrato de comunicación definido en `API_CONTRACT.md`.
- Postman para las pruebas de API.
- Meta Cloud API en entorno Sandbox para pruebas de notificaciones.

### 4.2 Datos requeridos

Preparar datos identificados como datos de prueba, sin utilizar información real de clientes:

1. Productos con código de barras registrado y precio válido.
2. Un producto con dos o más lotes disponibles y fechas de vencimiento distintas, para comprobar el orden FEFO.
3. Un producto con lote próximo a vencer y regla de descuento previamente configurada.
4. Un producto sin stock disponible.
5. Un cliente de prueba con límite de crédito definido y saldo inicial conocido.
6. Un cliente de prueba autorizado para recibir mensajes en el Sandbox de Meta.

## 5. Casos de prueba

### 5.1 Pruebas unitarias y de lógica FEFO

| ID | Escenario | Procedimiento | Resultado esperado | Estado |
|---|---|---|---|---|
| UT-FEFO-01 | Selección del lote con vencimiento más próximo | Preparar un producto con al menos dos lotes disponibles y fechas de vencimiento diferentes. Ejecutar la lógica FEFO para ese producto. | Se prioriza el lote disponible cuya fecha de vencimiento sea la más próxima. | Pendiente |
| UT-FEFO-02 | Exclusión de lotes sin stock | Preparar dos lotes del mismo producto, dejando uno sin unidades disponibles. Ejecutar la selección FEFO. | El lote sin stock no se selecciona; la lógica considera solo disponibilidad válida. | Pendiente |
| UT-FEFO-03 | Aplicación del descuento configurado | Preparar un lote dentro de la condición de vencimiento definida para activar un descuento. Ejecutar el cálculo del precio. | Se aplica la regla y el porcentaje/valor de descuento configurado para el producto o lote. | Pendiente |
| UT-FEFO-04 | Producto fuera de la condición de descuento | Preparar un lote cuya fecha de vencimiento no active la regla de descuento. Ejecutar el cálculo. | Se mantiene el precio regular y no se aplica un descuento no configurado. | Pendiente |

### 5.2 Pruebas funcionales del POS y ventas

| ID | Escenario | Procedimiento | Resultado esperado | Estado |
|---|---|---|---|---|
| TF-POS-01 | Consulta de producto mediante código de barras | Ingresar o escanear el código de barras de un producto existente. | El POS identifica el producto y presenta la información disponible para incorporarlo a la venta. | Pendiente |
| TF-POS-02 | Registro de venta con stock disponible | Agregar un producto con stock a la venta y confirmar la operación según el flujo implementado. | La venta se procesa y se registra con sus productos, cantidades y valores correspondientes. | Pendiente |
| TF-POS-03 | Venta de producto con lote próximo a vencer | Iniciar una venta para un producto con un lote que cumpla la condición de FEFO/descuento. | Se utiliza el lote priorizado por FEFO y el descuento configurado queda reflejado en el detalle/total de venta. | Pendiente |
| TF-POS-04 | Venta sin stock suficiente | Intentar vender una cantidad superior al stock disponible. | El sistema impide confirmar una venta que exceda la disponibilidad e informa el problema al usuario. | Pendiente |

### 5.3 Pruebas funcionales del Cuaderno Digital de Fiados

| ID | Escenario | Procedimiento | Resultado esperado | Estado |
|---|---|---|---|---|
| TF-FIA-01 | Registro de una compra como fiado | Seleccionar un cliente de prueba y registrar una compra por la modalidad de fiado. | Se asocia la operación al cliente y se actualiza su saldo pendiente. | Pendiente |
| TF-FIA-02 | Validación del límite de crédito | Preparar un cliente cuyo saldo más la nueva compra supere el límite de crédito configurado. Intentar registrar el fiado. | El sistema aplica la validación del límite y evita aceptar una operación que lo exceda. | Pendiente |
| TF-FIA-03 | Registro de abono | Registrar un abono válido para un cliente con deuda pendiente. | El abono queda registrado y el saldo pendiente disminuye por el monto abonado. | Pendiente |

### 5.4 Pruebas de API e integración

| ID | Escenario | Procedimiento | Resultado esperado | Estado |
|---|---|---|---|---|
| API-01 | Cumplimiento del contrato JSON | Ejecutar en Postman las solicitudes de los endpoints disponibles y comparar sus respuestas con `API_CONTRACT.md`. | Los campos, tipos de datos y estructura de respuesta coinciden con el contrato vigente. | Pendiente |
| API-02 | Validación de datos de entrada | Enviar a un endpoint una solicitud con campos obligatorios ausentes o tipos de datos inválidos. | La API rechaza la solicitud de acuerdo con las validaciones definidas y devuelve una respuesta de error controlada. | Pendiente |
| INT-01 | Persistencia de una venta | Ejecutar una venta de prueba mediante la API y consultar posteriormente los registros relacionados en Oracle. | La información de la venta queda persistida y puede recuperarse de forma consistente. | Pendiente |
| INT-02 | Consistencia entre venta e inventario | Ejecutar una venta que utilice FEFO y revisar la venta y las existencias luego de la operación. | La venta y la actualización de inventario quedan consistentes; no se descuenta stock dos veces ni se confirma parcialmente una operación. | Pendiente |
| INT-03 | Integración con WhatsApp Sandbox | Enviar una notificación a un número de prueba habilitado en Meta Sandbox y revisar la respuesta del proveedor. | La solicitud se procesa en el entorno Sandbox y el sistema informa el resultado real de la operación. | Pendiente |

### 5.5 Base de datos e infraestructura

| ID | Escenario | Procedimiento | Resultado esperado | Estado |
|---|---|---|---|---|
| BD-01 | Inicialización del modelo | Ejecutar el mecanismo definido para `01_init.sql` y revisar el esquema creado. | Se crea el modelo relacional correspondiente a las ocho tablas descritas para la Fase 2. | Pendiente |
| BD-02 | Integridad referencial | Intentar insertar un registro de prueba que haga referencia a una entidad inexistente, cuando corresponda a una relación definida. | Oracle rechaza la operación por la restricción de integridad referencial aplicable. | Pendiente |
| BD-03 | Verificación del índice FEFO | Consultar el esquema para comprobar la existencia de `idx_fefo_optimo`. | El índice documentado para apoyar las consultas FEFO se encuentra creado. | Pendiente |
| DOCKER-01 | Levantamiento del ambiente | Ejecutar `docker compose up -d` y revisar el estado y los logs del contenedor de Oracle. | El contenedor inicia sin errores bloqueantes y la base de datos queda disponible para la aplicación. | Pendiente |

### 5.6 Pruebas no funcionales y de carga

| ID | Escenario | Procedimiento | Resultado esperado | Estado |
|---|---|---|---|---|
| NF-01 | Validación básica de estabilidad de API | Ejecutar un conjunto repetible de solicitudes válidas y revisar respuestas y errores en logs. | La API responde de forma consistente y no presenta errores inesperados durante la ejecución controlada. | Pendiente |
| NF-02 | Prueba de estrés planificada | Preparar un escenario de concurrencia y ejecutarlo con JMeter cuando el flujo transaccional esté integrado. | Se obtiene evidencia de comportamiento bajo carga para analizarla frente a los umbrales que defina el equipo. | Planificada; no iniciada en el informe de Fase 2 |

## 6. Criterios de aceptación y cierre

Una ejecución se considera aprobada cuando el resultado observado coincide con el resultado esperado y existe evidencia verificable. Para cerrar el ciclo de QA, el equipo debe:

- Ejecutar los casos críticos del flujo de venta y FEFO.
- Verificar que la venta y la actualización del inventario sean consistentes.
- Ejecutar las pruebas de fiados y validar sus saldos.
- Revisar la correspondencia entre los endpoints disponibles y `API_CONTRACT.md`.
- Registrar y comunicar los defectos encontrados, su prioridad y su estado.
- Dejar explícitos los casos pendientes y las limitaciones del ambiente.
