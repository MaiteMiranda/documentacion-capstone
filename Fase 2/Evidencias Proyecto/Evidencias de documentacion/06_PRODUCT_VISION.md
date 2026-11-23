# Visión de producto - BarrioStock

## 1. Propósito del producto

BarrioStock es una plataforma web diseñada para modernizar la operación diaria de almacenes y minimarkets de barrio. El sistema integra ventas, inventario por lotes, prevención de pérdidas por vencimiento, control de fiados y comunicación con clientes.

## 2. Declaración de visión

**Para** los almaceneros y minimarkets de barrio que necesitan reducir pérdidas, ordenar las ventas y llevar un control confiable de las cuentas de sus clientes,

**BarrioStock es** una plataforma integral de punto de venta e inventario que combina el algoritmo FEFO, fiados digitales, historial de operaciones y notificaciones mediante Telegram.

**Que** centraliza la operación del almacén, automatiza descuentos preventivos por vencimiento y registra los compromisos de pago de los clientes.

**A diferencia de** las libretas físicas, las hojas de cálculo independientes y los sistemas POS generales que no consideran automáticamente los lotes y las fechas de vencimiento,

**Nuestro producto** permite vender primero los lotes próximos a vencer, informar a los vecinos sobre ofertas disponibles y consultar saldos y abonos desde una única plataforma web.

## 3. Problema que queremos resolver

Los almacenes de barrio presentan dificultades para:

- Registrar y priorizar productos próximos a vencer.
- Controlar el stock por lote.
- Llevar de forma confiable las ventas a crédito.
- Conocer los límites de crédito disponibles.
- Registrar abonos y movimientos de cuentas.
- Informar a los clientes sobre productos con descuento.
- Recordar pendientes de cobro sin utilizar métodos manuales.

Como resultado:

- Se generan pérdidas por productos vencidos.
- Las cuentas pueden quedar desordenadas.
- Algunos clientes exceden su límite de crédito.
- Las ventas no tienen trazabilidad suficiente.
- Los vecinos no conocen las ofertas preventivas disponibles.

## 4. Público objetivo

### Almacenero o administrador

Necesita controlar el inventario, revisar las operaciones del negocio y administrar productos, proveedores y ventas.

### Cajero

Necesita buscar productos, agregar cantidades al carrito, procesar ventas y registrar pagos fiados.

### Cliente vecino

Necesita consultar ofertas, conocer los precios disponibles y recibir notificaciones de cobranza cuando corresponda.

## 5. Propuesta de valor

BarrioStock entrega una solución diseñada específicamente para la realidad de los almacenes de barrio.

Sus principales aportes son:

- Digitalización del POS.
- Gestión del inventario por lotes.
- Descuento preventivo según vencimiento.
- Control de crédito y fiados.
- Registro de abonos.
- Historial general e individual.
- Catálogo público PWA.
- Notificaciones mediante Telegram.
- Ejecución local mediante Docker.
- Arquitectura frontend/backend desacoplada.

## 6. Objetivo general del producto

Desarrollar una plataforma web integral que permita controlar la venta de productos, administrar lotes e inventario, aplicar descuentos FEFO y registrar cuentas corrientes de clientes, reduciendo las pérdidas por vencimiento y mejorando la trazabilidad de las operaciones.

## 7. Objetivos específicos

1. Permitir búsquedas manuales y escaneo mediante lector USB.

2. Identificar el lote disponible que vence antes y aplicar FEFO.

3. Registrar ventas en efectivo, tarjeta o fiado.

4. Controlar los límites de crédito de los clientes.

5. Registrar abonos y consultar saldos pendientes.

6. Administrar productos, proveedores y recepción de lotes.

7. Permitir la carga de inventario mediante CSV o Excel `.xlsx`.

8. Mostrar alertas de vencimiento.

9. Presentar ofertas FEFO en una PWA pública.

10. Enviar recordatorios de cobro mediante Telegram.

11. Mantener historial de ventas y movimientos de clientes.

12. Ejecutar el sistema mediante Docker Compose.

## 8. Propuesta funcional

### Punto de venta

El POS permite:

- Buscar por nombre o código.
- Agregar productos al carrito.
- Modificar cantidades.
- Identificar descuentos FEFO.
- Procesar pagos en efectivo.
- Procesar pagos con tarjeta.
- Registrar ventas fiadas.

### Inventario

El módulo administrativo permite:

- Crear y actualizar productos.
- Administrar categorías y precios.
- Registrar proveedores.
- Importar catálogos desde CSV o Excel.
- Recibir lotes.
- Asociar cantidades y fechas de vencimiento.
- Consultar movimientos de inventario.

### Fiados

El módulo de fiados permite:

- Crear clientes.
- Validar RUT.
- Registrar límites de crédito.
- Consultar saldos.
- Registrar abonos.
- Consultar historial individual.
- Revisar productos frecuentes.
- Enviar recordatorios por Telegram.

### PWA pública

Los vecinos pueden consultar:

- Nombre del almacén.
- Productos con oferta.
- Precio normal.
- Precio rebajado.
- Porcentaje de descuento.
- Días restantes para vencer.

## 9. Diferenciadores del producto

### Motor FEFO

El sistema aplica descuentos según la cantidad de días que quedan para el vencimiento:

- Hasta 3 días: 30%.
- De 4 a 7 días: 15%.
- Más de 7 días: precio regular.
- Vencido o vence hoy: 50%.

### Fiado digital

Las cuentas se mantienen centralizadas y no dependen exclusivamente de una libreta física.

### Arquitectura desacoplada

El frontend React, el backend FastAPI y Oracle Database pueden evolucionar y desplegarse de manera independiente.

### PWA móvil

Los clientes pueden consultar el catálogo público desde un navegador móvil y agregar la aplicación a su pantalla de inicio.

### Integración Telegram

El sistema puede enviar recordatorios a Chat IDs registrados previamente.

## 10. Indicadores de éxito

BarrioStock podrá considerarse exitoso cuando:

- El POS registre ventas completas.
- Los lotes próximos a vencer reciban automáticamente descuentos FEFO.
- El stock se actualice después de cada venta.
- Las ventas fiadas respeten el límite de crédito.
- Los abonos reduzcan correctamente el saldo.
- Los productos puedan cargarse desde CSV o Excel.
- Los usuarios puedan navegar desde computadores, tablets y celulares.
- El catálogo público muestre las ofertas reales.
- Telegram pueda enviar notificaciones a los clientes configurados.
- El sistema mantenga trazabilidad de ventas y movimientos.

## 11. Alcance inicial

El alcance inicial corresponde a un MVP local que incluye:

- Usuarios ADMIN y CAJERO.
- POS.
- Inventario.
- Fiados.
- Historial.
- PWA.
- Telegram.
- Docker Compose.
- Oracle Database 23c.
- Pruebas automatizadas.

## 12. Exclusiones iniciales

No forman parte del MVP:

- Cámara web o escaneo por cámara.
- Integración bancaria o de pagos externos.
- Boleta electrónica del SII.
- Gestión contable completa.
- Facturación electrónica.
- Múltiples sucursales.
- Roles avanzados o permisos personalizados.
- Despliegue productivo definitivo no probado.
- Pruebas masivas con usuarios reales.

## 13. Riesgos principales

| Riesgo | Consecuencia | Respuesta |
|---|---|---|
| Oracle necesita mucha memoria | Base caída o lento inicio | Usar Docker local adecuado o plan Railway con recursos suficientes |
| Chat ID no registrado | Telegram no entrega el mensaje | Implementar registro previo del Chat ID |
| Datos inconsistentes | Stock o deuda incorrectos | Validar transacciones y restricciones |
| Código mal ingresado | Producto no encontrado | Validar el código antes de procesar |
| Importación incorrecta | Datos inválidos | Validar encabezados, tipos y columnas |
| Despliegue independiente | Configuración CORS o API incorrecta | Gestionar variables de entorno y dominios |

## 14. Criterios de aceptación del producto

El producto se considera aceptado cuando:

1. Un administrador puede iniciar sesión.
2. Un almacenero puede iniciar sesión.
3. Se puede agregar un producto al carrito.
4. FEFO calcula correctamente el descuento.
5. Una venta actualiza el stock.
6. Una venta fiada actualiza la deuda.
7. Un abono reduce el saldo.
8. Se puede crear un cliente válido.
9. Se rechazan RUT inválidos.
10. Se puede importar CSV o `.xlsx`.
11. El catálogo público muestra ofertas.
12. El sistema envía o simula Telegram.
13. El diseño funciona en celular y computadora.
14. Las pruebas automatizadas finalizadas sean aprobadas.

## 15. Visión a largo plazo

A futuro, BarrioStock puede evolucionar hacia:

- Aplicación móvil nativa.
- Escaneo mediante cámara.
- Integración con impresoras fiscales.
- Boleta electrónica.
- Integración con medios de pago.
- Notificaciones automáticas programadas.
- Gestión de varias sucursales.
- Aplicación para proveedores.
- Inteligencia predictiva de demanda.
- Recomendaciones de compra según historial.

## 16. Resultado esperado

BarrioStock busca convertirse en una herramienta accesible, clara y económica para mejorar la gestión operativa de pequeños comercios, reducir desperdicio de alimentos y brindarles una experiencia profesional sin depender de sistemas comerciales complejos.
