# Plan de Pruebas — BarrioStock

## 1. Objetivo

Verificar las funcionalidades críticas, reglas de negocio, integraciones, seguridad y diseño responsive de BarrioStock.

## 2. Tipos de prueba

- Pruebas unitarias.
- Pruebas de integración.
- Pruebas de API.
- Pruebas de seguridad.
- Pruebas responsive.
- Pruebas de carga previstas.
- Pruebas manuales de interfaz.

## 3. Resultado actual

- Backend: 77 pruebas aprobadas.
- Frontend: 41 pruebas aprobadas.
- Total: 118 pruebas aprobadas.
- Advertencia menor: deprecación de Starlette en una dependencia.
- No se ejecutaron pruebas JMeter.
- No se realizaron pruebas de carga masiva en producción.

## 4. Casos unitarios backend

| ID | Caso | Resultado |
|---|---|---|
| UT01 | Descuento vencido | 50% esperado |
| UT02 | Vence hoy | 50% |
| UT03 | Uno a tres días | 30% |
| UT04 | Cuatro a siete días | 15% |
| UT05 | Más de siete días | 0% |
| UT06 | Hash PBKDF2 | Hash correcto |
| UT07 | Contraseña incorrecta | Rechazada |
| UT08 | Hash con mismo texto | Salt diferente |
| UT09 | Token válido | Subject retornado |
| UT10 | Token expirado | Rechazado |
| UT11 | Firma incorrecta | Rechazada |
| UT12 | Token mal formado | Rechazado |
| UT13 | Mensaje Telegram | Contiene cliente y monto |

## 5. Casos API

| ID | Caso | Resultado |
|---|---|---|
| API01 | Health check | 200 |
| API02 | Login válido ADMIN | 200 |
| API03 | Login válido almacenero | 200 |
| API04 | RUT inválido | 422 |
| API05 | Contraseña incorrecta | 401 |
| API06 | Sin token | 401 |
| API07 | Token expirado | 401 |
| API08 | Escaneo válido | 200 |
| API09 | Código inexistente | 404 |
| API10 | Productos frecuentes | 200 |
| API11 | Venta efectivo | 201 |
| API12 | Venta fiado válida | 201 |
| API13 | Venta fiado excesiva | 400 |
| API14 | Carrito vacío | 400 |
| API15 | Fiado sin cliente | 400 |
| API16 | Abono válido | 201 |
| API17 | Abono excesivo | 400 |
| API18 | Cliente duplicado | 400 |
| API19 | Cliente inexistente | 404 |
| API20 | Deuda impide eliminación | 400 |
| API21 | Historial general | 200 |
| API22 | Historial individual | 200 |
| API23 | Catálogo PWA | 200 |
| API24 | Telegram sandbox | 200 |

## 6. Casos administrativos

| ID | Caso | Resultado |
|---|---|---|
| ADM01 | Almacenero accede a inventario | 403 |
| ADM02 | Admin lista productos | 200 |
| ADM03 | Crear producto válido | 201 |
| ADM04 | Crear código duplicado | 409 |
| ADM05 | Precio negativo | 422 |
| ADM06 | Actualizar producto inexistente | 404 |
| ADM07 | Crear proveedor | 201 |
| ADM08 | Proveedor duplicado | 409 |
| ADM09 | Recepción válida | 200 |
| ADM10 | Recepción cantidad cero | 422 |
| ADM11 | Importar CSV válido | 200 |
| ADM12 | CSV sin encabezados | 422 |
| ADM13 | `.xlsx` válido | 200 |
| ADM14 | Formato no permitido | 415 |

## 7. Casos frontend

| ID | Caso | Resultado |
|---|---|---|
| FE01 | Renderizar login | 41 pruebas totales aprobadas |
| FE02 | RUT válido | Aprobado |
| FE03 | RUT inválido | Aprobado |
| FE04 | Contraseña vacía | Aprobado |
| FE05 | Credenciales incorrectas | Aprobado |
| FE06 | Header desktop | Aprobado |
| FE07 | Header móvil | Aprobado |
| FE08 | Navegación POS | Aprobado |
| FE09 | Inventario solo para ADMIN | Aprobado |
| FE10 | Cerrar sesión | Aprobado |
| FE11 | Crear cliente válido | Aprobado |
| FE12 | Crear cliente vacío | Aprobado |
| FE13 | RUT cliente inválido | Aprobado |
| FE14 | Abono válido | Aprobado |
| FE15 | Nuevo saldo calculado | Aprobado |
| FE16 | Confirmar modal | Aprobado |
| FE17 | Cancelar modal | Aprobado |

## 8. Pruebas de seguridad

| Prueba | Estado |
|---|---|
| Hash de contraseñas | Implementado y probado |
| Contraseñas diferentes con salt | Probado |
| Token válido | Probado |
| Token expirado | Probado |
| Firma modificada | Probado |
| Ruta sin token | Probado |
| Almacenero en ruta ADMIN | Probado |
| RUT incorrecto | Probado |
| Consultas Oracle parametrizadas | Implementado |
| Secretos fuera del repositorio | Pendiente validar en despliegue real |

## 9. Pruebas de rendimiento previstas

No se ejecutaron pruebas de carga masiva.

Pruebas futuras:

- 100 usuarios concurrentes.
- 500 solicitudes por minuto.
- Tiempo de respuesta del POS.
- Tiempo de respuesta de ventas.
- Tiempo de generación del catálogo.
- Carga CSV con 1.000 filas.
- Carga `.xlsx` con 1.000 filas.
- Monitoreo de memoria Oracle.

Herramientas propuestas:

- JMeter.
- k6.
- Locust.

## 10. Evidencia final

### Comandos backend

```powershell
cd backend
python -m pytest -q