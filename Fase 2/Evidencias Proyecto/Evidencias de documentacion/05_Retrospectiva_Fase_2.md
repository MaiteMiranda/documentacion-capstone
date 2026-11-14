## 1. Objetivo

Revisar el proceso de trabajo y los resultados alcanzados durante la Fase 2, identificar prácticas que facilitaron el desarrollo, reconocer dificultades y establecer acciones de mejora para las siguientes iteraciones de BarrioStock.

## 2. Resumen de la iteración

Durante la Fase 2 se consolidó la arquitectura base y se avanzó en el primer Sprint. Se levantó Oracle Database 23c Free mediante Docker, se construyó un modelo relacional normalizado en tercera forma normal (3FN) de ocho tablas y se incorporó el índice `idx_fefo_optimo` para apoyar las consultas del motor FEFO.

También se definió `API_CONTRACT.md`, con las estructuras JSON de ocho endpoints críticos. Este contrato permitió dividir el trabajo: Karen Fernández avanzó en el backend con FastAPI y la lógica FEFO, mientras Maite Miranda comenzó la maquetación de las vistas React/Vite utilizando datos simulados (*mocks*).

Los objetivos generales y específicos definidos en la Fase 1 se mantuvieron. El ajuste principal fue precisar el stack tecnológico y la estrategia de integración.

## 3. ¿Qué funcionó bien?

### 3.1 Planificación e integración API-First

La definición anticipada del contrato de API permitió que frontend y backend trabajaran en paralelo. Mientras el backend desarrollaba sus servicios, el frontend podía construir y revisar las vistas React utilizando respuestas JSON simuladas. Esto disminuyó la dependencia de tener todos los endpoints terminados para comenzar el desarrollo de la interfaz.

### 3.2 Estandarización del entorno con Docker

Docker Compose permitió levantar Oracle Database 23c Free en los equipos de desarrollo con una configuración común. Esto facilitó que ambas integrantes trabajaran con el mismo motor de base de datos y redujo problemas asociados a diferencias de ambiente.

### 3.3 Organización temprana del trabajo

La creación anticipada del repositorio GitHub y del tablero Kanban facilitó el seguimiento de tareas y el versionamiento del proyecto. Figma también permitió revisar la propuesta visual del POS antes de completar su implementación.

### 3.4 Consolidación del modelo de datos

La definición del modelo relacional en 3FN, junto con el índice `idx_fefo_optimo`, permitió establecer una base de datos alineada con las necesidades de inventario y selección FEFO.

## 4. Dificultades y aspectos por mejorar

### 4.1 Disponibilidad para reuniones sincrónicas

Ambas integrantes trabajan a tiempo completo, lo que limita la disponibilidad para coordinar reuniones y realizar sesiones extensas de integración simultánea.

**Aprendizaje:** mantener el trabajo asíncrono requiere documentación compartida, acuerdos claros de interfaces y registro frecuente de avances y bloqueos.

### 4.2 Dependencia de los endpoints para las pruebas de integración

El plan de pruebas QA requería que los primeros endpoints estuvieran disponibles para ejecutar pruebas de integración. Por este motivo, durante la Fase 2 se avanzó en el diseño de los casos y en la preparación de Postman Collections, pero la ejecución integrada quedó condicionada a la evolución del backend.

**Aprendizaje:** diseñar las pruebas junto con el contrato API permite anticipar escenarios y preparar datos antes de que todos los servicios estén terminados.

### 4.3 Costos de mensajería en producción

Durante la investigación de la integración con Meta Cloud API se identificó que los mensajes de utilidad para cobranza pueden tener costos en un entorno productivo.

**Ajuste realizado:** se decidió utilizar exclusivamente el entorno Sandbox de Meta for Developers para la demostración académica, evitando costos de mensajería productiva. El informe de Fase 2 señala que el Sandbox permite registrar hasta cinco números telefónicos reales para las pruebas.

### 4.4 Ajuste de tecnología de base de datos

La planificación inicial consideraba PostgreSQL/MySQL. Durante el desarrollo se ajustó la decisión y se adoptó Oracle Database 23c Free, considerando sus capacidades transaccionales y el manejo de índices requerido por el motor FEFO. El levantamiento local de Oracle requería recursos, y Docker Compose facilitó la estandarización del entorno.

### 4.5 Actividades aún no iniciadas según el cronograma

La integración y el despliegue Cloud, además de las pruebas de estrés con JMeter, todavía no se habían iniciado en el informe de Fase 2. Estas actividades estaban programadas para las semanas 11 a 15, por lo que se registraron como pendientes de acuerdo con la planificación, no como retrasos.

## 5. Decisiones y ajustes realizados

| Tema | Decisión / ajuste | Motivo |
|---|---|---|
| Coordinación de frontend y backend | Definir `API_CONTRACT.md` antes de completar la implementación de todos los servicios. | Permitir trabajo paralelo y reducir bloqueos entre áreas. |
| Base de datos | Ajustar el diseño desde PostgreSQL/MySQL hacia Oracle Database 23c Free. | Alinear la solución con los requerimientos transaccionales y de indexación del motor FEFO. |
| Infraestructura | Utilizar Docker Compose para levantar Oracle. | Mantener entornos locales estandarizados. |
| WhatsApp | Utilizar Meta Cloud API en Sandbox durante la demostración académica. | Evitar costos asociados a mensajería en producción. |
| Priorización de frontend | Priorizar el módulo de Ventas del POS por sobre el Catálogo Público. | Concentrar el esfuerzo en el flujo principal de negocio. |
| Pruebas | Preparar Postman Collections para ejecutar pruebas directamente sobre los endpoints. | Facilitar pruebas de integración una vez disponibles los servicios. |

## 6. Acciones de mejora para la siguiente etapa

Las siguientes acciones se proponen a partir de los puntos anteriores. Deben incorporarse y asignarse en el tablero del equipo.

| Acción | Responsable propuesto | Resultado esperado | Prioridad / momento |
|---|---|---|---|
| Mantener actualizado `API_CONTRACT.md` cuando se modifiquen solicitudes o respuestas. | Maite Miranda y Karen Fernández | Contrato alineado con los servicios y las vistas que lo consumen. | Alta; durante el desarrollo. |
| Completar los endpoints críticos del flujo de venta y FEFO. | Karen Fernández (Backend) | Servicios disponibles para pruebas de integración. | Alta; siguiente iteración. |
| Continuar el módulo de Ventas del POS integrándolo gradualmente con la API. | Maite Miranda (Frontend), con coordinación de Karen | Flujo de venta conectado a los servicios y no solo a datos simulados. | Alta; siguiente iteración. |
| Ejecutar los casos FEFO, POS y fiados mediante Postman y revisar la persistencia en Oracle. | Maite Miranda y Karen Fernández | Evidencia de pruebas con resultado real y defectos registrados. | Alta; al habilitar los endpoints. |
| Verificar la consistencia transaccional del flujo Venta + Descuento FEFO. | Maite Miranda y Karen Fernández | Venta e inventario actualizados de forma consistente. | Alta; antes de avanzar al despliegue. |
| Mantener el uso de Meta Sandbox y documentar sus restricciones para la demostración. | Responsable técnico por confirmar | Evidencia reproducible sin utilizar mensajería productiva. | Media; durante la integración. |
| Preparar el despliegue Cloud contemplado en el cronograma. | Por asignar en Trello | Aplicación disponible en el entorno de demostración definido. | Según semanas 11 a 15 del plan. |
| Preparar y ejecutar pruebas de estrés con JMeter, definiendo previamente los umbrales de aceptación. | Por asignar en Trello | Resultados de carga documentados y evaluados. | Según semanas 11 a 15 del plan. |
| Mantener registro de acuerdos, bloqueos y avances para facilitar la coordinación asíncrona. | Maite Miranda y Karen Fernández | Menor dependencia de reuniones sincrónicas y mejor trazabilidad. | Continua. |

## 7. Continuar, ajustar y comenzar

| Mantener | Ajustar | Incorporar / comenzar |
|---|---|---|
| Trabajo asíncrono respaldado por documentación. | Coordinar revisiones breves de integración cuando existan cambios relevantes en API o datos. | Registrar sistemáticamente resultados y evidencias de QA. |
| Contrato API como referencia compartida. | Actualizar el contrato junto con cada modificación del backend o frontend. | Ejecutar pruebas de integración cuando los endpoints estén disponibles. |
| Docker Compose para estandarizar el ambiente Oracle. | Revisar periódicamente la configuración de base de datos y los datos semilla. | Preparar el ambiente de despliegue y las pruebas de carga planificadas. |
| Priorización del flujo crítico de venta y FEFO. | Evitar ampliar el alcance de módulos secundarios antes de cerrar el flujo transaccional. | Validar el flujo Venta + Descuento FEFO de extremo a extremo. |

## 8. Conclusión

La Fase 2 permitió establecer una base técnica y metodológica para BarrioStock: modelo de datos en Oracle 23c, ambiente estandarizado mediante Docker Compose, contrato API y desarrollo paralelo de backend y frontend. El enfoque API-First y el trabajo asíncrono fueron facilitadores importantes frente a la disponibilidad limitada de ambas integrantes.

Los principales focos de mejora para la siguiente etapa son completar la integración de los endpoints, validar de extremo a extremo la venta con FEFO, ejecutar formalmente el plan de QA y abordar el despliegue Cloud y las pruebas de estrés en las semanas previstas por el cronograma.
