# 📄 Contrato de API REST - BarrioStock v1.0

Este documento define la interfaz de comunicación estándar entre el **Backend (FastAPI)** y el **Frontend (React / Vite)** para la plataforma BarrioStock. Toda petición y respuesta utiliza formato JSON (`Content-Type: application/json`).

---

## 🔍 Resumen de Endpoints (8 Endpoints Base)

| # | Módulo | Método | Endpoint | Descripción |
|---|---|---|---|---|
| 1 | POS | `GET` | `/api/v1/pos/productos/escaneo/{codigo_barras}` | Escanea código de barras y aplica motor FEFO |
| 2 | POS | `GET` | `/api/v1/pos/productos/frecuentes` | Obtiene productos frecuentes para la grilla del POS |
| 3 | POS | `POST` | `/api/v1/pos/ventas` | Registra una transacción de venta (Efectivo, Tarjeta, Fiado) |
| 4 | Fiados | `GET` | `/api/v1/fiados/clientes` | Lista los clientes con sus saldos y límites de crédito |
| 5 | Fiados | `GET` | `/api/v1/fiados/clientes/{cliente_id}/historial` | Muestra el historial transaccional de un cliente |
| 6 | Fiados | `POST` | `/api/v1/fiados/abonos` | Registra un pago/abono a la deuda de un cliente |
| 7 | Notif. | `POST` | `/api/v1/notificaciones/whatsapp` | Envía un recordatorio de cobro vía Meta Cloud API |
| 8 | Catálogo | `GET` | `/api/v1/catalog/ofertas-express` | Consulta pública de productos FEFO para la PWA móvil |

---

## 📐 Especificación Detallada de Endpoints

### 1. Escanear Producto por Código de Barras
Obtiene la información del producto e identifica automáticamente si el lote activo requiere aplicar un descuento dinámico por proximidad de vencimiento (Algoritmo FEFO).

* **Método:** `GET`
* **URL:** `/api/v1/pos/productos/escaneo/{codigo_barras}`
* **Parámetros de Ruta:** `codigo_barras` (string, ej: `7804567890123`)
* **Respuesta Exitosa (`200 OK`):**
```json
{
  "id": 3,
  "codigo_barras": "7804567890123",
  "nombre": "Yogurt Batido Frutilla 120g",
  "categoria": "Lácteos",
  "precio_base": 450,
  "lote": {
    "id": 1,
    "codigo_lote": "L-OCT-01",
    "fecha_vencimiento": "2026-10-14",
    "dias_para_vencer": 2,
    "cantidad_disponible": 15
  },
  "fefo": {
    "aplica_descuento": true,
    "porcentaje_descuento": 30,
    "precio_final": 315,
    "mensaje_ui": "Aplica Dscto. por Vencimiento -30%"
  }
}

```

* **Respuesta de Error (`404 Not Found`):**

```json
{
  "codigo_error": "PRODUCTO_NO_ENCONTRADO",
  "mensaje": "El código de barras ingresado no existe en el catálogo."
}

```

---

### 2. Listar Productos Frecuentes

Obtiene los productos destacados ordenados por categoría para desplegar en la grilla rápida del POS.

* **Método:** `GET`
* **URL:** `/api/v1/pos/productos/frecuentes`
* **Parámetros de Consulta (Opcional):** `categoria` (string, ej: `Lácteos`)
* **Respuesta Exitosa (`200 OK`):**

```json
{
  "total": 4,
  "productos": [
    {
      "id": 1,
      "codigo_barras": "7801234567890",
      "nombre": "Pan Hallulla 1Kg",
      "categoria": "Panadería",
      "precio_base": 1800,
      "tiene_fefo_activo": false
    },
    {
      "id": 3,
      "codigo_barras": "7804567890123",
      "nombre": "Yogurt Batido Frutilla",
      "categoria": "Lácteos",
      "precio_base": 450,
      "tiene_fefo_activo": true,
      "porcentaje_fefo": 30
    }
  ]
}

```

---

### 3. Registrar Venta (Efectivo / Tarjeta / Fiado)

Procesa la transacción de compra, actualiza el stock del lote consumido y, si el tipo de pago es `FIADO`, incrementa el saldo deudor del cliente.

* **Método:** `POST`
* **URL:** `/api/v1/pos/ventas`
* **Cuerpo de la Petición (`Request Body`):**

```json
{
  "usuario_id": 1,
  "cliente_id": 1,
  "tipo_pago": "FIADO",
  "total_bruto": 3350,
  "total_descuento": 405,
  "total_neto": 2945,
  "detalles": [
    {
      "producto_id": 2,
      "lote_id": 3,
      "cantidad": 1,
      "precio_unitario": 2000,
      "descuento_aplicado": 0,
      "subtotal": 2000
    },
    {
      "producto_id": 3,
      "lote_id": 1,
      "cantidad": 3,
      "precio_unitario": 450,
      "descuento_aplicado": 405,
      "subtotal": 945
    }
  ]
}

```

* **Respuesta Exitosa (`201 Created`):**

```json
{
  "id_venta": 102,
  "fecha_transaccion": "2026-10-12T12:35:00Z",
  "estado": "PROCESADA",
  "tipo_pago": "FIADO",
  "total_neto": 2945,
  "cliente": {
    "id": 1,
    "nombre": "Juan Pérez",
    "nuevo_saldo_deuda": 15445,
    "credito_disponible": 34555
  }
}

```

* **Respuesta de Error (`400 Bad Request` - Exceso de Límite):**

```json
{
  "codigo_error": "CREDITO_EXCEDIDO",
  "mensaje": "La compra supera el límite de crédito permitido para este cliente."
}

```

---

### 4. Listar Clientes y Estado de Fiados

Obtiene el listado completo de clientes registrados en el "Cuaderno Digital" con sus saldos de deuda y créditos disponibles.

* **Método:** `GET`
* **URL:** `/api/v1/fiados/clientes`
* **Respuesta Exitosa (`200 OK`):**

```json
{
  "resumen_general": {
    "total_clientes": 5,
    "saldo_total_pendiente": 50000,
    "credito_disponible_global": 130000
  },
  "clientes": [
    {
      "id": 1,
      "rut": "12.345.678-5",
      "nombre": "Juan Pérez",
      "telefono": "+56912345678",
      "limite_credito": 50000,
      "saldo_deuda": 12500,
      "estado_cuenta": "MOROSO"
    },
    {
      "id": 2,
      "rut": "15.234.567-6",
      "nombre": "María González",
      "telefono": "+56987654321",
      "limite_credito": 40000,
      "saldo_deuda": 8000,
      "estado_cuenta": "AL_DIA"
    }
  ]
}

```

---

### 5. Historial de Cuenta Corriente del Cliente

Consulta el detalle histórico de compras a fiado y abonos realizados por un cliente en específico.

* **Método:** `GET`
* **URL:** `/api/v1/fiados/clientes/{cliente_id}/historial`
* **Parámetros de Ruta:** `cliente_id` (integer, ej: `1`)
* **Respuesta Exitosa (`200 OK`):**

```json
{
  "cliente_id": 1,
  "nombre": "Juan Pérez",
  "saldo_actual": 12500,
  "movimientos": [
    {
      "id": 102,
      "tipo": "CARGO_COMPRA",
      "fecha": "2026-10-12T12:35:00Z",
      "monto": 2945,
      "medio": "FIADO"
    },
    {
      "id": 45,
      "tipo": "ABONO_PAGO",
      "fecha": "2026-10-05T18:10:00Z",
      "monto": -5000,
      "medio": "EFECTIVO"
    }
  ]
}

```

---

### 6. Registrar Abono a Deuda (Pago de Fiado)

Registra un abono en dinero de un vecino, reduciendo su saldo deudor acumulado en el sistema.

* **Método:** `POST`
* **URL:** `/api/v1/fiados/abonos`
* **Cuerpo de la Petición (`Request Body`):**

```json
{
  "cliente_id": 1,
  "monto_abonado": 5000,
  "medio_pago": "EFECTIVO"
}

```

* **Respuesta Exitosa (`201 Created`):**

```json
{
  "id_abono": 46,
  "fecha_abono": "2026-10-12T11:47:00Z",
  "monto_abonado": 5000,
  "saldo_anterior": 12500,
  "nuevo_saldo_deuda": 7500,
  "mensaje": "Abono registrado exitosamente."
}

```

---

### 7. Enviar Recordatorio de Cobro por WhatsApp

Dispara el envío de una plantilla de mensaje a través de Meta Cloud API (Sandbox) al WhatsApp del cliente.

* **Método:** `POST`
* **URL:** `/api/v1/notificaciones/whatsapp`
* **Cuerpo de la Petición (`Request Body`):**

```json
{
  "cliente_id": 1
}

```

* **Respuesta Exitosa (`200 OK`):**

```json
{
  "status": "ENVIADO",
  "proveedor": "META_CLOUD_API_SANDBOX",
  "telefono_destino": "+56912345678",
  "mensaje_enviado": "Hola Juan Pérez, te recordamos que tu saldo pendiente en Almacén Don Tito es de $12.500. ¡Gracias por tu preferencia!",
  "fecha_envio": "2026-10-12T11:47:00Z"
}

```

---

### 8. Catálogo Público de Ofertas Express (PWA Vecinos)

Punto de acceso público para que los vecinos vean desde sus celulares los productos con rebaja por vencimiento FEFO.

* **Método:** `GET`
* **URL:** `/api/v1/catalog/ofertas-express`
* **Respuesta Exitosa (`200 OK`):**

```json
{
  "almacen": "Almacén Don Tito",
  "total_ofertas": 2,
  "ofertas": [
    {
      "producto_id": 3,
      "nombre": "Yogurt Batido Frutilla 120g",
      "categoria": "Lácteos",
      "dias_para_vencer": 2,
      "precio_normal": 450,
      "precio_oferta": 315,
      "descuento_porcentaje": 30,
      "etiqueta": "⏳ Vence en 2 días"
    },
    {
      "producto_id": 4,
      "nombre": "Leche Entera 1L",
      "categoria": "Lácteos",
      "dias_para_vencer": 3,
      "precio_normal": 1190,
      "precio_oferta": 833,
      "descuento_porcentaje": 30,
      "etiqueta": "⏳ Vence en 3 días"
    }
  ]
}

```

---

## 🛠️ Estructura Genérica de Errores (HTTP 4xx / 5xx)

```json
{
  "status": "ERROR",
  "code": 400,
  "error_type": "VALIDATION_ERROR",
  "message": "Descripción legible del error para la interfaz de usuario.",
  "timestamp": "2026-10-12T11:47:00Z"
}

```
---
