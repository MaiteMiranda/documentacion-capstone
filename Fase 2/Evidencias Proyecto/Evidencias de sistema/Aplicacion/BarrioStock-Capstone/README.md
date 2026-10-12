# 🏪 BarrioStock - Plataforma Inteligente para Almacenes de Barrio

[![Stack - Oracle 23c](https://img.shields.io/badge/Database-Oracle_23c_Free-red.svg)](https://www.oracle.com/database/free/)
[![Backend - FastAPI](https://img.shields.io/badge/Backend-FastAPI_Python_3.11-009688.svg)](https://fastapi.tiangolo.com/)
[![Frontend - React](https://img.shields.io/badge/Frontend-React_18_+_Vite-61DAFB.svg)](https://react.dev/)
[![UI - TailwindCSS](https://img.shields.io/badge/UI-TailwindCSS-38B2AC.svg)](https://tailwindcss.com/)
[![DevOps - Docker](https://img.shields.io/badge/DevOps-Docker_Compose-2496ED.svg)](https://www.docker.com/)

---

## 📝 Descripción del Proyecto

**BarrioStock** es una solución web integral diseñada para la modernización de los almacenes y minimarkets de barrio en Chile. Combina un Punto de Venta (POS) optimizado para pantallas táctiles, un motor automático de descuentos por vencimiento de productos (**Algoritmo FEFO - *First Expired, First Out***) y un módulo de **Cuaderno Digital de Fiados** integrado con la API oficial de WhatsApp (Meta Cloud API). Además, incluye una **PWA (Progressive Web App)** pública para que los vecinos consulten las "Ofertas Express" del local en tiempo real.

---

## 💡 Propuesta de Innovación y Valor Agregado

- **¿Qué problema resuelve?** Elimina las pérdidas económicas por alimentos vencidos en repisa y reemplaza la libreta física de fiados en papel, evitando cobros desfasados o descontrol de crédito.
- **¿Qué lo hace diferente?** Integra el algoritmo logístico **FEFO** directamente en el escaneo del código de barras en caja, aplicando descuentos automáticos sin requerir intervención manual del cajero.
- **Impacto Social y Sustentable:** Fomenta la economía circular y la reducción de desperdicios de comida ("Salva Alimentos") democratizando el uso de la API oficial de WhatsApp para pequeños comercios a costo $0.

---

## 🚀 Características Principales

- **🛒 Punto de Venta (POS) Táctil:** Interfaz ultra rápida diseñada para operarse con lector de código de barras o teclado táctil, minimizando clics por venta.
- **⚡ Motor FEFO Dinámico:** Detección automática de lotes próximos a vencer durante la lectura del código, aplicando descuentos preconfigurados directo en la boleta.
- **📓 Cuaderno Digital de Fiados:** Control inmutable de cuentas corrientes por cliente, comprobación de límites de crédito y registro de abonos.
- **📲 Notificaciones de Cobranza (WhatsApp):** Envío masivo e individual de recordatorios de deuda a través del Sandbox de Meta Cloud API ($0 costo).
- **📱 Catálogo PWA Móvil:** Vitrina pública para vecinos orientada a la reducción de mermas y consumo sustentable.

---

## 🏛️ Arquitectura del Sistema

BarrioStock utiliza una arquitectura de **Monorepo Desacoplado** basada en capas (Clean Architecture / SOLID) para garantizar alta disponibilidad, mantenibilidad y rapidez de respuesta:

```text
[ Cliente Vecino (PWA Móvil) ]       [ Cajero / Almacenero (React POS) ]
              │                                         │
              └───────────────┬─────────────────────────┘
                              │ (HTTP / JSON REST)
                              ▼
            ┌───────────────────────────────────┐
            │    API REST Backend (FastAPI)     │
            │ ┌───────────┐ ┌─────────────────┐ │
            │ │  Routers  │ │ Services (FEFO) │ │
            │ └───────────┘ └─────────────────┘ │
            └─────────┬───────────────────┬─────┘
                      │                   │
                      ▼                   ▼
        ┌──────────────────────────┐ ┌──────────────────────────┐
        │   Oracle Database 23c    │ │     Meta Cloud API       │
        │   (Docker - 3FN Schema)  │ │   (WhatsApp Sandbox)     │
        └──────────────────────────┘ └──────────────────────────┘

```

* **Frontend (React 18 + Vite + TailwindCSS):** Interfaz Single Page Application (SPA) para el POS y Progressive Web App (PWA) para clientes vecinos.
* **Backend (Python 3.11 + FastAPI):** API REST ligera y asíncrona encargada de la lógica de negocio, reglas del motor FEFO y validaciones Pydantic.
* **Base de Datos (Oracle Database 23c Free):** Motor relacional contenedorizado en Docker que gestiona el modelo en 3FN con transacciones ACID e índices optimizados para FEFO.
* **Integración Externa (Meta Cloud API):** Servicio HTTPS para la automatización de notificaciones y cobranzas de fiados por WhatsApp.

---

## 🏗️ Estructura del Proyecto

```text
BarrioStock-Capstone/
├── docker-compose.yml                  # Contenedorización de Oracle DB 23c Free
├── API_CONTRACT.md                     # Contrato de interfaces JSON Backend-Frontend
├── README.md                           # Documentación principal del repositorio
│
├── Evidencias_de_documentacion/        # DOCUMENTACIÓN FORMAL FASE 2
│   ├── 01_Documento_Inicio_y_Metodologia.md
│   ├── 02_Artefactos_Scrum_Product_Backlog.md
│   ├── 03_Arquitectura_UML_ModeloDatos.md
│   └── 04_Manual_Tecnico_Docker_Pruebas.md
│
└── Evidencias_de_sistema/             # CÓDIGO EJECUTABLE Y BASE DE DATOS
    ├── Base_de_datos/                  # SCRIPTS DE BASE DE DATOS
    │   ├── 01_init.sql                 # Modelo Relacional DDL (3FN - 8 Tablas)
    │   └── 02_seed.sql                 # Datos de prueba (lotes, productos, fiados)
    │
    └── Aplicacion/                     # CÓDIGO FUENTE
        ├── backend/                    # API REST FASTAPI (PYTHON 3.11)
        │   ├── Dockerfile
        │   ├── requirements.txt
        │   └── app/
        │       ├── main.py             # Entrypoint FastAPI
        │       ├── core/               # Configuración y conexión a Oracle DB
        │       ├── api/v1/             # Endpoints (POS, Fiados, Notificaciones)
        │       ├── schemas/            # Validación de datos Pydantic
        │       ├── services/           # Lógica de Negocio (Motor FEFO, Meta API)
        │       └── repositories/       # Consultas SQL (Acceso a Datos)
        │
        └── frontend/                   # APLICACIÓN REACT + VITE (SPA / PWA)
            ├── package.json
            ├── vite.config.js
            └── src/
                ├── pages/              # Vistas principales (POS, Fiados, Home, PWA)
                ├── components/         # Componentes UI reutilizables
                ├── services/           # Clientes HTTP (Axios)
                └── hooks/              # Custom Hooks de estado

```

---

## 🛠️ Requisitos e Instalación Local

### Prerrequisitos

* [Docker Desktop](https://www.docker.com/products/docker-desktop/) en ejecución.
* [Node.js](https://nodejs.org/) v18+ y npm.
* [Python](https://www.python.org/) v3.11+.

### Pasos para Ejecutar el Proyecto

1. **Clonar el Repositorio:**
```bash
git clone [https://github.com/tu-usuario/barriostock-capstone.git](https://github.com/tu-usuario/barriostock-capstone.git)
cd barriostock-capstone

```


2. **Levantar la Base de Datos (Oracle 23c Free en Docker):**
```bash
docker-compose up -d

```


*La base de datos se inicialización automáticamente ejecutando `01_init.sql` y se poblará con datos iniciales mediante `02_seed.sql`.*
3. **Iniciar el Backend (FastAPI):**
```bash
cd Evidencias_de_sistema/Aplicacion/backend
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

```


*Documentación interactiva Swagger disponible en:* `http://localhost:8000/docs`
4. **Iniciar el Frontend (React + Vite):**
```bash
cd ../frontend
npm install
npm run dev

```


*Aplicación web disponible en:* `http://localhost:5173`

---

## 🔄 Metodología y Gestión del Proyecto

El desarrollo se gestiona activamente mediante el marco de trabajo **Scrum**. Se realiza el seguimiento de historias de usuario, tareas y avances en el tablero de Trello:

* 📌 **Tablero Trello del Proyecto:** [BarrioStock - Scrum Board 2026](https://www.google.com/search?q=https://trello.com/b/barriostock-capstone-2026)

---

## 📜 Licencia y Uso Académico

Este proyecto se desarrolla en el marco del Taller de Integración / Capstone para la obtención del título de Ingeniería Informática en Duoc UC. Quedan reservados todos los derechos intelectuales del equipo desarrollador.

```

```