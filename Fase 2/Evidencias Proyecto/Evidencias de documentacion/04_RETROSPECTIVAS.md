# Evidencias de Retrospectivas

## Retrospectiva Sprint 1 — Base técnica

### ¿Qué salió bien?

- Se definió la arquitectura.
- React y FastAPI quedaron separados.
- Docker Compose permitió probar servicios juntos.
- El contrato API evitó dudas de integración.
- Se creó la base inicial de Oracle.

### ¿Qué puede mejorar?

- Oracle consume mucha memoria.
- Las variables de entorno no estaban totalmente normalizadas al inicio.
- Se perdió tiempo ajustando dominios de despliegue.

### Acciones

- Crear `.env.example`.
- Configurar CORS desde variables.
- Documentar requisitos mínimos.
- Separar servicios para despliegue.
- Validar Oracle antes de desarrollar la UI completa.

### Resultado

- Arquitectura estable.
- Entorno local reproducible.
- Integración frontend/backend preparada.

## Retrospectiva Sprint 2 — POS y FEFO

### ¿Qué salió bien?

- Se implementó el flujo completo de escaneo.
- FEFO quedó centralizado en un servicio.
- El carrito fue desacoplado del backend.
- Las ventas pudieron probarse sin Oracle.

### ¿Qué puede mejorar?

- Las fechas mock no siempre coinciden con la fecha actual.
- La cantidad de escenarios FEFO debía aumentar.
- El escaneo debía distinguir mejor los códigos no encontrados.

### Acciones

- Incorporar pruebas de límites FEFO.
- Mejorar mensajes de error.
- Agregar alertas de vencimiento.
- Reducir lógica dentro de los componentes React.

### Resultado

- POS operativo.
- Validación de 50%, 30%, 15% y 0%.
- Ventas de efectivo, tarjeta y fiado.

## Retrospectiva Sprint 3 — Fiados y Telegram

### ¿Qué salió bien?

- Se creó el cuaderno digital.
- Los abonos respetan saldos.
- Se incorporó control de límite.
- Telegram sustituyó WhatsApp.
- Las reglas se trasladaron al backend.

### ¿Qué puede mejorar?

- Telegram requiere registrar Chat ID.
- El flujo de vinculación no se encuentra automatizado.
- Algunos mensajes podían ser más claros.

### Acciones

- Traducir validaciones al español.
- Validar RUT con dígito verificador.
- Explicar el requisito del Chat ID.
- Verificar mensajes antes de enviarlos.

### Resultado

- Fiados integrado.
- Historial individual operativo.
- Telegram probado en modo sandbox y API real.

## Retrospectiva Sprint 4 — Inventario y cierre

### ¿Qué salió bien?

- Se añadió recepción de lotes.
- CSV y `.xlsx` quedaron soportados.
- Se eliminó la funcionalidad de caja.
- El header quedó adaptable.
- Se añadieron pruebas frontend.

### ¿Qué puede mejorar?

- Probar Oracle con recursos reales.
- Mejorar el reporte de pruebas.
- Agregar capturas automatizadas.
- Validar PWA en dispositivos reales.

### Acciones

- Ejecutar build y lint.
- Ejecutar 77 pruebas backend.
- Ejecutar 41 pruebas frontend.
- Documentar despliegue.
- Mantener evidencia de prueba.

### Resultado

- 118 pruebas aprobadas.
- Frontend compilado.
- ESLint aprobado.
- MVP documentado.

## Mejoras generales del equipo

1. Comunicación asincrónica mediante Git.
2. Contrato API definido antes de integrar.
3. Separación de responsabilidades.
4. Validaciones compartidas.
5. Uso de mocks para pruebas.
6. Redacción de mensajes en español.
7. Eliminación de funcionalidades no requeridas.
8. Automatización de pruebas.
9. Documentación de ejecución.
10. Diseño mobile-first.