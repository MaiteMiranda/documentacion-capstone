# 🏗️ Arquitectura de Software, Diagramas UML y Modelo de Datos - BarrioStock

---

## 1. Diagrama de Arquitectura de Software

```text
[ Cliente Vecino (Smartphone PWA) ]     [ Cajero / Almacenero (PC / Tablet POS) ]
              │                                           │
              ▼ (HTTP / PWA)                              ▼ (HTTP / SPA React)
      ┌──────────────────────────────────────────────────────────────┐
      │                   FRONTEND (React + Vite)                    │
      └──────────────────────────────┬───────────────────────────────┘
                                     │ (JSON REST API)
                                     ▼
      ┌──────────────────────────────────────────────────────────────┐
      │                BACKEND FASTAPI (Python 3.11)                 │
      │  ┌──────────────────┐ ┌──────────────────┐ ┌──────────────┐  │
      │  │  Routers (API)   │ │ Services (FEFO)  │ │ Repos (SQL)  │  │
      │  └──────────────────┘ └──────────────────┘ └──────────────┘  │
      └──────────────┬────────────────────────────────┬──────────────┘
                     │                                │
                     ▼                                ▼
┌───────────────────────────────┐   ┌───────────────────────────────┐
│     ORACLE DATABASE 23c       │   │     META CLOUD API (WA)       │
│  (Docker Container - Port 1521)│   │  (External API - HTTPS Sandbox)│
└───────────────────────────────┘   └───────────────────────────────┘

2. Diagramas UML
2.1. Diagrama de Casos de Uso
Actores: Cajero, Vecino, Motor FEFO, Meta Cloud API.

Casos de Uso Principales:

CU01 - Escanear Producto: Permite leer el código de barras e invoca la validación del lote FEFO.

CU02 - Anotar en Fiado: Carga el monto a la cuenta corriente tras verificar límites de crédito.

CU03 - Notificar Deuda: Invoca a Meta Cloud API para enviar la plantilla por WhatsApp.

CU04 - Consultar Ofertas Express: Permite al vecino visualizar alimentos rebajados desde la PWA.

2.2. Diagrama de Secuencia (Proceso de Escaneo FEFO)

Cajero              React POS           FastAPI (API)        FEFO Engine          Oracle DB 23c
  │                     │                     │                   │                    │
  │── Escanea Código ──►│                     │                   │                    │
  │                     │── GET /escaneo/780─►│                   │                    │
  │                     │                     │── Obtener Lote───►│                    │
  │                     │                     │                   │── SELECT Lotes ───►│
  │                     │                     │                   │◄─ Data de Lote ────│
  │                     │                     │◄─ Calc. Descuento─│                    │
  │                     │◄── JSON (200 OK) ───│                   │                    │
  │◄─ Muestra -30% OFF ─│                     │                   │                    │

  2.3. Diagrama de Componentes
Frontend: AuthModule, PosModule, FiadosModule, PwaCatalog, ApiService (Axios).

Backend: PosRouter, FiadoRouter, FefoService, WhatsAppService, OracleRepository.


3. Modelo de Datos Relacional (3FN - Oracle Database 23c)
Normalizado en Tercera Forma Normal (3FN) en Oracle 23c compuesto por 8 tablas:

USUARIOS (Credenciales y roles ADMIN/CAJERO).

CLIENTES (Fiados, limite_credito y saldo_deuda).

PRODUCTOS (Catálogo base y precios).

LOTES (Control de vencimientos fecha_vencimiento y estado FEFO).

VENTAS (Cabecera de transacciones).

DETALLE_VENTAS (Líneas de boleta y descuentos aplicados).

ABONOS_FIADO (Historial de pagos).

NOTIFICACIONES_WA (Log de envíos Meta API).

4. Requisitos No Funcionales (RNF)
RNF01 - Rendimiento: Tiempo de respuesta de la API de escaneo < 200 ms.

RNF02 - Disponibilidad: POS opera 100% local en Docker (offline friendly salvo WhatsApp).

RNF03 - Seguridad: Contraseñas encriptadas con Hashing y aislamiento de llaves en .env.

RNF04 - Usabilidad: Interfaz táctil de alto contraste apta para pantallas de caja.