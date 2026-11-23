## Documento de Diseño: Arquitectura, modelo de datos y diagramas UML


# 1. Resumen ejecutivo

BarrioStock es una plataforma web diseñada para almacenes de barrio. Integra:

- Punto de venta.
- Administración de inventario.
- Recepción de lotes.
- Motor FEFO.
- Ventas en efectivo, tarjeta y fiado.
- Registro de abonos.
- Historial de operaciones.
- Catálogo público PWA.
- Notificaciones mediante Telegram.
- Base de datos Oracle Database 23c.
- Contenedores Docker.

La arquitectura está separada en frontend, API REST, servicios de negocio y persistencia.

---

# 2. Arquitectura general

```mermaid
flowchart LR
    C1[Almacenero / Cajero]
    C2[Administrador]
    C3[Vecino]

    subgraph FRONTEND["Frontend React"]
        R[React 19]
        V[Vite]
        T[Tailwind CSS]
        A[Axios]
        PWA[PWA]
    end

    subgraph SERVIDOR["Servidor FastAPI"]
        API[API REST]
        AUTH[Autenticación Bearer]
        POS[POS]
        FEFO[Motor FEFO]
        FIADO[Fiados]
        INV[Inventario]
        DASH[Dashboard e historial]
        TEL[Telegram]
    end

    subgraph DATOS["Persistencia"]
        ORA[(Oracle Database 23c)]
        MOCK[(Datos mock)]
    end

    subgraph EXTERNO["Servicio externo"]
        BOT[Telegram Bot API]
    end

    C1 --> R
    C2 --> R
    C3 --> PWA

    R --> V
    R --> T
    R --> A
    A --> API

    API --> AUTH
    API --> POS
    POS --> FEFO
    API --> FIADO
    API --> INV
    API --> DASH
    API --> TEL

    AUTH --> ORA
    POS --> ORA
    FIADO --> ORA
    INV --> ORA
    DASH --> ORA
    TEL --> BOT
    API --> MOCK
```


# 3. Componentes del frontend

## Tecnologías

- React 19.
- Vite.
- TailwindCSS.
- Axios.
- PWA.
- Lucide React.
- QRCode React.

## Principales componentes

| Componente | Responsabilidad |
|---|---|
| `App.jsx` | Sesión, navegación y estado global |
| `Header.jsx` | Navegación, usuario y menú responsive |
| `LoginPage.jsx` | Inicio de sesión |
| `PosPage.jsx` | Escaneo, carrito y pagos |
| `FiadosPage.jsx` | Clientes, abonos y Telegram |
| `AlertasPage.jsx` | Productos próximos a vencer |
| `HistorialPage.jsx` | Ventas e productos destacados |
| `AdminInventoryPage.jsx` | Productos, proveedores e inventario |
| `PublicPwaPage.jsx` | Catálogo público |
| `NuevoClienteModal.jsx` | Creación de clientes |
| `AbonoModal.jsx` | Registro de abonos |
| `EditarClienteModal.jsx` | Edición de clientes |
| `QrPwaModal.jsx` | Presentación del enlace QR |
| `api.js` | Cliente HTTP y autenticación |

## Interacción frontend/API

1. React inicia sesión mediante Axios.
2. El backend entrega el token Bearer.
3. React guarda el token en `localStorage`.
4. Las solicitudes protegidas incluyen el token.
5. FastAPI valida permisos y devuelve JSON.
6. React actualiza el estado local o la vista.
7. El catálogo público no requiere autenticación.

---

# 4. Componentes del backend

## Tecnologías

- Python 3.11 o superior.
- FastAPI.
- Pydantic.
- Uvicorn.
- python-multipart.
- oracledb.
- httpx.

## Estructura funcional

```text
backend/app
├── api/v1
│   ├── auth.py
│   ├── pos.py
│   ├── fiados.py
│   ├── inventory.py
│   ├── dashboard.py
│   ├── notificaciones.py
│   └── pwa.py
├── core
│   ├── config.py
│   ├── database.py
│   └── security.py
├── repositories
│   └── oracle_repository.py
├── services
│   ├── fefo_service.py
│   └── telegram_service.py
└── schemas
```

## Responsabilidades

| Componente | Responsabilidad |
|---|---|
| Routers | Exponen endpoints REST |
| Pydantic | Valida entradas y respuestas |
| Seguridad | Genera y valida tokens |
| FEFO | Calcula descuentos por vencimiento |
| Telegram | Envía recordatorios |
| Repositorio | Consulta Oracle y mock |
| Dependencias | Valida autenticación y rol |

---

# 5. Arquitectura por capas

```mermaid
flowchart TB
    subgraph PRESENTACION["Capa de presentación"]
        P1[Interfaz React]
        P2[PWA]
        P3[Responsive UI]
    end

    subgraph CONTROL["Capa de control"]
        C1[Routers FastAPI]
        C2[Validación Pydantic]
        C3[Autorización]
    end

    subgraph NEGOCIO["Capa de negocio"]
        N1[Motor FEFO]
        N2[Ventas]
        N3[Fiados]
        N4[Inventario]
        N5[Telegram]
    end

    subgraph DATOS["Capa de datos"]
        D1[OracleRepository]
        D2[Oracle 23c]
        D3[Mock contingencia]
    end

    P1 --> C1
    P2 --> C1
    C1 --> C2
    C2 --> C3
    C3 --> N1
    C3 --> N2
    C3 --> N3
    C3 --> N4
    C3 --> N5
    N1 --> D1
    N2 --> D1
    N3 --> D1
    N4 --> D1
    N5 --> D1
    D1 --> D2
    D1 --> D3
```

# 6. Modelo entidad-relación

```mermaid
erDiagram
    USUARIOS ||--o{ VENTAS : registra
    USUARIOS ||--o{ MOVIMIENTOS_INVENTARIO : autoriza
    CLIENTES ||--o{ VENTAS : realiza
    CLIENTES ||--o{ ABONOS_FIADO : registra
    CLIENTES ||--o{ NOTIFICACIONES_TELEGRAM : recibe
    PRODUCTOS ||--o{ LOTES : contiene
    LOTES ||--o{ DETALLE_VENTAS : abastece
    PRODUCTOS ||--o{ DETALLE_VENTAS : contiene
    VENTAS ||--|{ DETALLE_VENTAS : incluye
    PRODUCTOS ||--o{ MOVIMIENTOS_INVENTARIO : modifica
    LOTES ||--o{ MOVIMIENTOS_INVENTARIO : identifica
    PROVEEDORES ||--o{ MOVIMIENTOS_INVENTARIO : suministra
```


# 7. Modelo relacional

## USUARIOS

| Campo | Tipo | Restricción |
|---|---|---|
| id | NUMBER | Clave primaria |
| rut | VARCHAR2(12) | Único, obligatorio |
| nombre | VARCHAR2(100) | Obligatorio |
| rol | VARCHAR2(20) | ADMIN o CAJERO |
| password_hash | VARCHAR2(255) | Obligatorio |
| creado_en | TIMESTAMP | Por defecto |

## CLIENTES

| Campo | Tipo | Restricción |
|---|---|---|
| id | NUMBER | Clave primaria |
| rut | VARCHAR2(12) | Único |
| nombre | VARCHAR2(100) | Obligatorio |
| telefono | VARCHAR2(64) | Chat ID Telegram |
| limite_credito | NUMBER(10,0) | Mayor o igual a cero |
| saldo_deuda | NUMBER(10,0) | Mayor o igual a cero |
| creado_en | TIMESTAMP | Por defecto |

> Conviene renombrar `telefono` a `chat_id_telegram` en una actualización del esquema.

## PRODUCTOS

| Campo | Tipo | Restricción |
|---|---|---|
| id | NUMBER | Clave primaria |
| codigo_barras | VARCHAR2(50) | Único |
| nombre | VARCHAR2(100) | Obligatorio |
| categoria | VARCHAR2(50) | Obligatorio |
| precio_base | NUMBER(10,0) | Mayor que cero |
| unidad_medida | VARCHAR2(20) | Por defecto UNIDAD |
| stock_minimo | NUMBER(8,0) | Mayor o igual a cero |
| controla_vencimiento | NUMBER(1,0) | Booleano |
| activo | NUMBER(1,0) | Booleano |

## LOTES

| Campo | Tipo | Restricción |
|---|---|---|
| id | NUMBER | Clave primaria |
| producto_id | NUMBER | Clave foránea |
| codigo_lote | VARCHAR2(50) | Obligatorio |
| fecha_vencimiento | DATE | Obligatorio |
| cantidad_inicial | NUMBER(8,0) | Mayor que cero |
| cantidad_actual | NUMBER(8,0) | Mayor o igual a cero |
| porcentaje_descuento_fefo | NUMBER(3,0) | Por defecto cero |

## PROVEEDORES

| Campo | Tipo | Restricción |
|---|---|---|
| id | NUMBER | Clave primaria |
| nombre | VARCHAR2(120) | Único |
| activo | NUMBER(1,0) | Booleano |

## MOVIMIENTOS_INVENTARIO

| Campo | Tipo | Restricción |
|---|---|---|
| id | NUMBER | Clave primaria |
| producto_id | NUMBER | Clave foránea |
| lote_id | NUMBER | Clave foránea opcional |
| tipo_movimiento | VARCHAR2(20) | COMPRA, VENTA o AJUSTE |
| cantidad | NUMBER(8,0) | Obligatorio |
| motivo | VARCHAR2(200) | Opcional |
| usuario_id | NUMBER | Clave foránea |
| fecha_movimiento | TIMESTAMP | Por defecto |

## VENTAS

| Campo | Tipo | Restricción |
|---|---|---|
| id | NUMBER | Clave primaria |
| usuario_id | NUMBER | Clave foránea |
| cliente_id | NUMBER | Clave foránea opcional |
| fecha_venta | TIMESTAMP | Por defecto |
| total_bruto | NUMBER(10,0) | Obligatorio |
| total_descuento | NUMBER(10,0) | Por defecto cero |
| total_neto | NUMBER(10,0) | Obligatorio |
| tipo_pago | VARCHAR2(20) | EFECTIVO, TARJETA o FIADO |

## DETALLE_VENTAS

| Campo | Tipo | Restricción |
|---|---|---|
| id | NUMBER | Clave primaria |
| venta_id | NUMBER | Clave foránea |
| producto_id | NUMBER | Clave foránea |
| lote_id | NUMBER | Clave foránea |
| cantidad | NUMBER(8,0) | Mayor que cero |
| precio_unitario | NUMBER(10,0) | Mayor o igual a cero |
| descuento_aplicado | NUMBER(10,0) | Mayor o igual a cero |
| subtotal | NUMBER(10,0) | Obligatorio |

## ABONOS_FIADO

| Campo | Tipo | Restricción |
|---|---|---|
| id | NUMBER | Clave primaria |
| cliente_id | NUMBER | Clave foránea |
| monto_abonado | NUMBER(10,0) | Mayor que cero |
| fecha_abono | TIMESTAMP | Por defecto |
| medio_pago | VARCHAR2(20) | EFECTIVO, TARJETA o TRANSFERENCIA |

## NOTIFICACIONES_TELEGRAM

La implementación actual utiliza el nombre histórico `notificaciones_wa` en SQL. Se recomienda corregirlo a:

| Campo | Tipo | Restricción |
|---|---|---|
| id | NUMBER | Clave primaria |
| cliente_id | NUMBER | Clave foránea |
| chat_id_destino | VARCHAR2(64) | Obligatorio |
| mensaje | VARCHAR2(500) | Obligatorio |
| estado | VARCHAR2(20) | PENDIENTE, ENVIADO o FALLIDO |
| proveedor | VARCHAR2(30) | TELEGRAM_BOT_API o TELEGRAM_BOT_SANDBOX |
| fecha_envio | TIMESTAMP | Por defecto |

---

# 8. Diagrama UML de casos de uso

```mermaid
flowchart LR
    ADMIN((Administrador))
    CAJA((Cajero / Almacenero))
    VECINO((Vecino))

    subgraph SISTEMA["BarrioStock"]
        A1[Iniciar sesión]
        A2[Buscar o escanear]
        A3[Agregar al carrito]
        A4[Aplicar FEFO]
        A5[Registrar venta]
        A6[Registrar fiado]
        A7[Registrar abono]
        A8[Gestionar clientes]
        A9[Gestionar inventario]
        A10[Recibir lotes]
        A11[Importar CSV o XLSX]
        A12[Consultar historial]
        A13[Consultar alertas]
        A14[Enviar Telegram]
        A15[Consultar ofertas PWA]
    end

    ADMIN --> A1
    CAJA --> A1
    CAJA --> A2
    CAJA --> A3
    CAJA --> A4
    CAJA --> A5
    CAJA --> A6
    CAJA --> A7
    CAJA --> A8
    CAJA --> A12
    CAJA --> A13
    CAJA --> A14
    ADMIN --> A9
    ADMIN --> A10
    ADMIN --> A11
    ADMIN --> A12
    VECINO --> A15
```


---

# 9. Diagrama UML de clases

```mermaid
classDiagram
    class Usuario {
        +int id
        +string rut
        +string nombre
        +string rol
        +iniciarSesion()
    }

    class Producto {
        +int id
        +string codigoBarras
        +string nombre
        +number precioBase
        +obtenerLotes()
    }

    class Lote {
        +int id
        +string codigo
        +date fechaVencimiento
        +int cantidadActual
        +calcularDescuentoFEFO()
    }

    class Venta {
        +int id
        +number totalBruto
        +number totalDescuento
        +number totalNeto
        +string tipoPago
        +procesar()
    }

    class DetalleVenta {
        +int cantidad
        +number precioUnitario
        +number descuento
        +number subtotal
    }

    class Cliente {
        +int id
        +string rut
        +string nombre
        +string chatIdTelegram
        +number limiteCredito
        +number saldoDeuda
        +registrarAbono()
    }

    class Abono {
        +int id
        +number monto
        +string medioPago
    }

    class Inventario {
        +recibirLote()
        +importarCSV()
        +importarXLSX()
        +registrarMovimiento()
    }

    class TelegramService {
        +generarMensaje()
        +enviarRecordatorio()
    }

    Usuario "1" --> "*" Venta : registra
    Venta "1" --> "*" DetalleVenta : contiene
    Producto "1" --> "*" Lote : posee
    Producto "1" --> "*" DetalleVenta : aparece
    Lote "1" --> "*" DetalleVenta : abastece
    Cliente "1" --> "*" Venta : realiza
    Cliente "1" --> "*" Abono : registra
    Cliente "1" --> "*" TelegramService : recibe
    Inventario --> Producto
    Inventario --> Lote
```

---

# 10. Diagrama UML de secuencia

## Funcionalidad principal: venta FEFO

```mermaid
sequenceDiagram
    actor Cajero
    participant UI as React POS
    participant API as FastAPI
    participant FEFO as FEFOService
    participant Repo as OracleRepository
    participant DB as Oracle Database

    Cajero->>UI: Escanea o escribe código
    UI->>API: GET /api/v1/pos/productos/escaneo/{codigo}
    API->>Repo: Buscar producto y lote
    Repo->>DB: Consulta parametrizada
    DB-->>Repo: Producto y lote
    Repo-->>API: Datos encontrados
    API->>FEFO: Evaluar vencimiento
    FEFO-->>API: Porcentaje y precio final
    API-->>UI: Producto con datos FEFO
    UI->>UI: Agregar al carrito
    Cajero->>UI: Confirmar venta
    UI->>API: POST /api/v1/pos/ventas
    API->>Repo: Registrar venta
    Repo->>DB: Validar stock
    Repo->>DB: Validar límite si es fiado
    Repo->>DB: Registrar venta y detalle
    Repo->>DB: Actualizar stock y deuda
    DB-->>Repo: Confirmación
    Repo-->>API: Resultado
    API-->>UI: Venta procesada
    UI-->>Cajero: Mostrar recibo digital
```

---

# 11. Diagrama de componentes

```mermaid
flowchart TB
    subgraph FRONTEND_COMPONENTES["Frontend"]
        F1[LoginPage]
        F2[Header]
        F3[PosPage]
        F4[FiadosPage]
        F5[AlertasPage]
        F6[HistorialPage]
        F7[AdminInventoryPage]
        F8[PublicPwaPage]
    end

    subgraph BACKEND_COMPONENTES["Backend"]
        B1[Auth Router]
        B2[POS Router]
        B3[Fiados Router]
        B4[Inventory Router]
        B5[Dashboard Router]
        B6[PWA Router]
        B7[Telegram Router]
    end

    subgraph SERVICIOS["Servicios"]
        S1[FEFOService]
        S2[TelegramService]
        S3[Security]
    end

    subgraph DATOS["Datos"]
        D1[OracleRepository]
        D2[(Oracle)]
    end

    F1 --> B1
    F3 --> B2
    F4 --> B3
    F7 --> B4
    F5 --> B2
    F6 --> B5
    F8 --> B6
    F4 --> B7

    B1 --> S3
    B2 --> S1
    B3 --> D1
    B4 --> D1
    B5 --> D1
    B6 --> D1
    B7 --> S2
    S2 --> D1
    D1 --> D2
```

---

# 12. Flujo FEFO

```mermaid
flowchart TD
    A[Consultar fecha del lote]
    B{Cantidad de días}
    C[50% descuento]
    D[30% descuento]
    E[15% descuento]
    F[0% descuento]
    G[Agregar al carrito]
    H[Calcular precio final]
    I[Registrar venta]
    J[Actualizar stock]

    A --> B
    B -->|0 días o vencido| C
    B -->|1 a 3 días| D
    B -->|4 a 7 días| E
    B -->|Más de 7 días| F
    C --> H
    D --> H
    E --> H
    F --> H
    H --> G
    G --> I
    I --> J
```

---

# 13. Flujo de importación de inventario

```mermaid
sequenceDiagram
    actor Administrador
    participant UI as Inventario React
    participant API as Inventory API
    participant Parser as CSV/XLSX
    participant Repo as OracleRepository
    participant DB as Oracle

    Administrador->>UI: Selecciona archivo
    UI->>API: POST /admin/inventario/productos/importar
    API->>Parser: Detectar extensión
    Parser->>Parser: Validar encabezados
    Parser->>Parser: Validar datos
    Parser-->>API: Filas procesadas y errores
    API->>Repo: Crear productos
    Repo->>DB: Insertar o rechazar
    DB-->>Repo: Resultado
    Repo-->>API: Productos creados y errores
    API-->>UI: Resultado de importación
```

---

# 14. Flujo de Telegram

```mermaid
sequenceDiagram
    actor Almacenero
    participant UI as Fiados React
    participant API as FastAPI
    participant Repo as OracleRepository
    participant DB as Oracle
    participant TG as Telegram Bot API

    Almacenero->>UI: Selecciona enviar recordatorio
    UI->>API: POST /notificaciones/telegram
    API->>Repo: Obtener cliente
    Repo->>DB: Consultar nombre y Chat ID
    DB-->>Repo: Datos del cliente
    Repo-->>API: Datos disponibles
    API->>API: Generar mensaje
    API->>TG: Enviar mensaje
    TG-->>API: OK o error
    API-->>UI: Estado enviado o fallido
```

---

# 15. Requisitos no funcionales

## Seguridad

- Contraseñas mediante PBKDF2.
- Tokens Bearer.
- RUT validado con dígito verificador.
- Consultas Oracle con parámetros.
- Rutas administrativas protegidas por rol.
- CORS limitado al dominio autorizado.
- Variables sensibles fuera del repositorio.
- Mensajes de error sin detalles internos.

## Rendimiento

- Índice optimizado para FEFO.
- Consultas específicas por código de barras.
- Archivos PWA precacheados.
- Build de frontend optimizado.
- API REST ligera.

## Usabilidad

- Diseño responsive.
- Menús adaptados a celular.
- Mensajes en español.
- Formularios con validaciones visibles.
- Modales de confirmación.
- Navegación simple.

## Disponibilidad

- Docker Compose.
- Health checks.
- Contenedor backend independiente.
- Fallback mock en ausencia de Oracle.
- Manejo de errores HTTP.

## Portabilidad

- Docker.
- `.env.example`.
- Scripts SQL independientes.
- Frontend configurable mediante `VITE_API_URL`.
- Backend configurable mediante variables.

## Escalabilidad

- Frontend separado del backend.
- Servicios REST.
- Repositorio único de acceso a datos.
- Servicios independientes en Railway.
- Posibilidad de incorporar caché y balanceador.

## Mantenibilidad

- Separación por módulos.
- Validaciones Pydantic.
- Servicios de negocio independientes.
- Pruebas unitarias.
- Pruebas de integración.
- Contrato API documentado.

## Interoperabilidad

- JSON sobre HTTPS.
- Axios para comunicación.
- Telegram Bot API.
- Oracle mediante oracledb.
- Nginx para archivos estáticos.

---

# 16. Docker

## Docker Compose

```yaml
services:
  oracle-db:
    build: ./database
    ports:
      - "${ORACLE_PORT}:1521"
    volumes:
      - oracle_data:/opt/oracle/oradata
    environment:
      ORACLE_PASSWORD: ${ORACLE_PASSWORD}
      ORACLE_PDB: ${DB_SERVICE}

  backend:
    build: ./backend
    ports:
      - "${BACKEND_PORT}:8000"
    environment:
      DB_HOST: oracle-db
      DB_PORT: 1521
      DB_USER: ${DB_USER}
      DB_PASSWORD: ${DB_PASSWORD}
      DB_SERVICE: ${DB_SERVICE}
      SECRET_KEY: ${SECRET_KEY}
      CORS_ORIGINS: ${CORS_ORIGINS}
      TELEGRAM_BOT_TOKEN: ${TELEGRAM_BOT_TOKEN}
      TELEGRAM_DEFAULT_CHAT_ID: ${TELEGRAM_DEFAULT_CHAT_ID}

  frontend:
    build: ./frontend
    ports:
      - "${FRONTEND_PORT}:80"
    environment:
      VITE_API_URL: ${VITE_API_URL}

volumes:
  oracle_data:
```

## Dockerfiles

### Backend

Responsable de instalar Python, abrir el puerto 8000 y ejecutar Uvicorn.

### Frontend

Responsable de:

1. Instalar dependencias.
2. Ejecutar `npm run build`.
3. Generar PWA.
4. Servir los archivos mediante Nginx.

### Oracle

Responsable de iniciar Oracle 23c Free y ejecutar scripts SQL.

## Variables obligatorias

- PROJECT_NAME.
- SECRET_KEY.
- CORS_ORIGINS.
- API_V1_STR.
- DB_HOST.
- DB_PORT.
- DB_USER.
- DB_PASSWORD.
- DB_SERVICE.
- ORACLE_PASSWORD.
- ORACLE_PORT.
- BACKEND_PORT.
- FRONTEND_PORT.
- VITE_API_URL.
- TELEGRAM_BOT_TOKEN.
- TELEGRAM_DEFAULT_CHAT_ID.

## Levantar el sistema

```powershell
docker compose up -d --build
```

## Detener el sistema

```powershell
docker compose down
```

---

# 17. Pruebas

## Backend

- Pruebas FEFO.
- Pruebas de autenticación.
- Pruebas de permisos.
- Pruebas de inventario.
- Pruebas CSV.
- Pruebas `.xlsx`.
- Pruebas de fiados.
- Pruebas de ventas.
- Pruebas de Telegram.
- Pruebas de seguridad.

Resultado confirmado:

```text
77 pruebas backend aprobadas
```

## Frontend

- Validación RUT.
- Login.
- Header responsive.
- Modales.
- Clientes.
- Abonos.
- Navegación por roles.

Resultado confirmado:

```text
41 pruebas frontend aprobadas
```

## Construcción

```text
Build de producción aprobado
Lint aprobado
PWA generada
```

---

# 18. Innovación

## Problema resuelto

BarrioStock reduce pérdidas por vencimiento y desorganización de ventas fiadas.

## Diferenciación

- FEFO integrado al POS.
- Inventario por lotes.
- Fiado digital.
- PWA pública.
- Telegram.
- Docker.
- Oracle.
- Validaciones en español.

## Valor agregado

### Económico

- Reduce merma.
- Mejora rotación.
- Controla deuda.
- Evita errores manuales.

### Social

- Reduce desperdicio.
- Facilita el acceso a ofertas.
- Moderniza almacenes pequeños.

### Técnico

- Arquitectura modular.
- Persistencia relacional.
- API REST.
- Pruebas automatizadas.
- Contenedores reproducibles.

---