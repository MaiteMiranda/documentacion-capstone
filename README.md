# 🏪 BarrioStock – Plataforma Inteligente para Almacenes de Barrio

[![Database - Oracle 23c Free](https://img.shields.io/badge/Database-Oracle_23c_Free-red.svg)](https://www.oracle.com/database/free/)
[![Backend - FastAPI](https://img.shields.io/badge/Backend-FastAPI_Python_3.11-009688.svg)](https://fastapi.tiangolo.com/)
[![Frontend - React](https://img.shields.io/badge/Frontend-React_18_%2B_Vite-61DAFB.svg)](https://react.dev/)
[![UI - TailwindCSS](https://img.shields.io/badge/UI-TailwindCSS-38B2AC.svg)](https://tailwindcss.com/)
[![DevOps - Docker Compose](https://img.shields.io/badge/DevOps-Docker_Compose-2496ED.svg)](https://www.docker.com/)

> Solución web para apoyar la gestión diaria de almacenes y minimarkets de barrio en Chile, con punto de venta, control de inventario por vencimiento y gestión digital de fiados.

## 📚 Contenido

- [Descripción del proyecto](#-descripción-del-proyecto)
- [Problema, innovación y valor agregado](#-problema-innovación-y-valor-agregado)
- [Características principales](#-características-principales)
- [Tecnologías y herramientas](#-tecnologías-y-herramientas)
- [Equipo e integrantes](#-equipo-e-integrantes)
- [Arquitectura del sistema](#-arquitectura-del-sistema)
- [Estructura del repositorio](#-estructura-del-repositorio)
- [Requisitos e instalación local](#-requisitos-e-instalación-local)
- [Metodología y gestión del proyecto](#-metodología-y-gestión-del-proyecto)
- [Pruebas y aseguramiento de calidad](#-pruebas-y-aseguramiento-de-calidad)
- [Documentación y evidencias](#-documentación-y-evidencias)
- [Licencia y uso académico](#-licencia-y-uso-académico)

---

## 📝 Descripción del proyecto

**BarrioStock** es una solución web integral diseñada para modernizar la administración de almacenes y minimarkets de barrio en Chile. El sistema reúne un **Punto de Venta (POS)** optimizado para pantallas táctiles, un motor de descuentos por vencimiento basado en el algoritmo **FEFO (*First Expired, First Out*)**, un **Cuaderno Digital de Fiados** y una **PWA (*Progressive Web App*)** pública para que los vecinos consulten las Ofertas Express del local.

La solución contempla, además, la integración con la **Meta Cloud API de WhatsApp** para enviar recordatorios de cobranza. Para la demostración académica se considera el entorno Sandbox de Meta; el envío de mensajes en producción puede estar sujeto a tarifas de la plataforma.

## 💡 Problema, innovación y valor agregado

- **Problema que resuelve:** busca disminuir las pérdidas económicas asociadas a productos vencidos o próximos a vencer y reemplazar el control manual de fiados en libretas físicas, reduciendo errores de registro y seguimiento de las deudas.
- **Diferenciador:** incorpora la lógica FEFO en el flujo de venta. Al consultar o escanear un producto, el sistema puede identificar el lote disponible con vencimiento más próximo y aplicar la regla de descuento previamente configurada.
- **Impacto social y sustentable:** promueve la reducción de mermas de alimentos mediante ofertas oportunas y entrega herramientas digitales de gestión a pequeños comercios.
- **Viabilidad de la integración:** el uso de WhatsApp Sandbox permite demostrar el flujo de notificaciones sin asumir los costos de mensajería de un entorno productivo.

## 🚀 Características principales

- **🛒 Punto de Venta (POS) táctil:** interfaz para agilizar el registro de productos mediante lector de código de barras o ingreso desde la interfaz.
- **⚡ Motor FEFO dinámico:** prioriza los lotes según su fecha de vencimiento y contempla descuentos preconfigurados para productos próximos a vencer.
- **📓 Cuaderno Digital de Fiados:** permite gestionar cuentas corrientes por cliente, consultar saldos, controlar límites de crédito y registrar abonos.
- **📲 Notificaciones de cobranza por WhatsApp:** integración prevista con Meta Cloud API para enviar recordatorios individuales o masivos mediante el entorno Sandbox.
- **📱 Catálogo PWA móvil:** vitrina pública para consultar ofertas del almacén y apoyar la reducción de mermas.

## 🛠️ Tecnologías y herramientas

| Área | Tecnología / herramienta | Uso en el proyecto |
|---|---|---|
| Frontend | React 18 | Construcción de las vistas del POS y de la experiencia web para clientes. |
| Herramienta frontend | Vite | Servidor de desarrollo y construcción de la aplicación React. |
| Estilos e interfaz | TailwindCSS | Maquetación y estilos de los componentes de la interfaz. |
| Lenguaje backend | Python 3.11 | Implementación de la lógica del servidor. |
| Backend | FastAPI | Construcción de la API REST. |
| Base de datos | Oracle Database 23c Free | Persistencia relacional; modelo de datos normalizado en tercera forma normal (3FN). |
| Contenedores | Docker y Docker Compose | Estandarización del entorno de desarrollo y ejecución de Oracle. |


## 👥 Equipo e integrantes

| Integrante | Rol / área principal | Responsabilidades |
|---|---|---|
| **Maite Miranda** | UI/UX y Frontend | Planificación visual, diseño de mockups en Figma y desarrollo de las vistas React del POS. |
| **Karen Fernández** | Requerimientos, Base de Datos y Backend | Levantamiento de requerimientos, diseño e implementación del modelo de datos Oracle 23c y desarrollo del Backend REST con Python y FastAPI. |
| **Maite Miranda y Karen Fernández** | Pruebas y calidad | Diseño del plan de pruebas QA y preparación de pruebas de integración sobre los endpoints mediante Postman Collections. |

## 🏛️ Arquitectura del sistema

BarrioStock se organiza como un **monorepo desacoplado** con separación entre frontend, backend y persistencia de datos. El backend expone servicios REST que son consumidos por el POS y la PWA. La lógica de negocio , incluido el procesamiento FEFO, se concentra en los servicios del backend, mientras que los repositorios gestionan el acceso a Oracle.

```text
[ Cliente vecino (PWA móvil) ]       [ Cajero / almacenero (React POS) ]
                │                                  │
                └────────────────┬─────────────────┘
                                 │ HTTP / JSON REST
                                 ▼
                 ┌───────────────────────────────┐
                 │       API REST FastAPI       │
                 │                               │
                 │  Routers | Schemas | Services │
                 │           | Repositories       │
                 └──────────────┬─────────┬──────┘
                                │         │
                     SQL        │         │ HTTPS
                                ▼         ▼
                 ┌──────────────────┐  ┌────────────────────┐
                 │ Oracle Database  │  │ Meta Cloud API     │
                 │ 23c Free         │  │ WhatsApp Sandbox   │
                 │ Modelo relacional│  └────────────────────┘
                 │ 3FN              │
                 └──────────────────┘
```

### Componentes

- **Frontend – React 18, Vite y TailwindCSS:** aplicación SPA para el POS y experiencia PWA para los clientes del almacén.
- **Backend – Python 3.11 y FastAPI:** API REST que contiene la lógica de negocio, las reglas del motor FEFO y validaciones de datos mediante Pydantic.
- **Base de datos – Oracle Database 23c Free:** motor relacional ejecutado en Docker. En la Fase 2 se reporta un modelo normalizado en 3FN de **8 tablas** y el índice `idx_fefo_optimo` para apoyar las consultas del motor FEFO.
- **Integración externa – Meta Cloud API:** comunicación HTTPS con WhatsApp, utilizando Sandbox para las pruebas y demostración académica.
- **Contrato de API:** `API_CONTRACT.md` define las estructuras de solicitudes y respuestas JSON de **8 endpoints críticos**, permitiendo el trabajo paralelo entre frontend y backend mediante el enfoque API-First.


## 🧰 Requisitos e instalación local

### Prerrequisitos

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado y en ejecución.
- [Node.js](https://nodejs.org/) v18 o superior y npm.
- [Python](https://www.python.org/) 3.11 o superior.
- Git para clonar el repositorio.

### 1. Clonar el repositorio

Reemplaza la URL de ejemplo por la dirección real del repositorio de GitHub:

```bash
git clone https://github.com/tu-usuario/barriostock-capstone.git
cd barriostock-capstone
```

### 2. Levantar la base de datos

Desde la raíz del proyecto, ejecuta:

```bash
docker compose up -d
```

También puede utilizarse `docker-compose up -d`, según la versión de Docker Compose instalada.

Los scripts `01_init.sql` y `02_seed.sql` corresponden, respectivamente, a la creación del esquema y a la carga de datos iniciales. Su ejecución automática depende de cómo estén montados y configurados en `docker-compose.yml`.

### 3. Instalar e iniciar el backend

```bash
cd Evidencias_de_sistema/Aplicacion/backend
python -m venv venv
```

Activar el entorno virtual:

```bash
# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Windows CMD
venv\Scripts\activate.bat

# Linux / macOS
source venv/bin/activate
```

Instalar dependencias e iniciar FastAPI:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

La documentación interactiva de la API queda disponible en:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### 4. Instalar e iniciar el frontend

En una segunda terminal:

```bash
cd Evidencias_de_sistema/Aplicacion/frontend
npm install
npm run dev
```

La aplicación de desarrollo queda disponible en `http://localhost:5173`.

## 🔄 Metodología y gestión del proyecto

El proyecto utiliza **metodología ágil Scrum**, con Sprints de dos semanas y trabajo principalmente asíncrono. Para facilitar la colaboración entre integrantes con jornadas laborales completas, se definió anticipadamente el contrato de API mediante el enfoque **API-First Design**. Esto permitió avanzar en paralelo: el frontend comenzó a consumir datos simulados (*mocks*) y el backend desarrolló la lógica de negocio y los servicios REST.

- **Planificación y seguimiento:** historias de usuario, tareas y avance mediante tablero Kanban en Trello.
- **Versionamiento:** repositorio GitHub con un modelo de ramificación Git Flow simplificado.
- **Diseño previo:** mockups de interfaz realizados en Figma.
- **Contrato de integración:** `API_CONTRACT.md`, con estructuras JSON acordadas para el intercambio de datos entre frontend y backend.

📌 **Tablero Trello:** [BarrioStock – Scrum Board 2026](https://trello.com/b/FCKShWlK/barrio-stock)

## 📜 Licencia y uso académico

Este proyecto se desarrolla en el marco de la asignatura **Capstone / Taller de Integración** para la obtención del título de Ingeniería Informática en **Duoc UC**. Los derechos intelectuales del trabajo corresponden al equipo desarrollador, de acuerdo con las condiciones académicas aplicables.
