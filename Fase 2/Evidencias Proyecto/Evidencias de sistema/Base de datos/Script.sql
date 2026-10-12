-- 1. TABLA USUARIOS
CREATE TABLE usuarios (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    rut VARCHAR2(12) NOT NULL UNIQUE,
    nombre VARCHAR2(100) NOT NULL,
    rol VARCHAR2(20) DEFAULT 'CAJERO' CHECK (rol IN ('ADMIN', 'CAJERO')),
    password_hash VARCHAR2(255) NOT NULL,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. TABLA CLIENTES
CREATE TABLE clientes (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    rut VARCHAR2(12) NOT NULL UNIQUE,
    nombre VARCHAR2(100) NOT NULL,
    telefono VARCHAR2(15) NOT NULL,
    limite_credito NUMBER(10, 0) DEFAULT 50000 NOT NULL,
    saldo_deuda NUMBER(10, 0) DEFAULT 0 NOT NULL,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_saldo_limite CHECK (saldo_deuda <= limite_credito)
);

-- 3. TABLA PRODUCTOS
CREATE TABLE productos (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    codigo_barras VARCHAR2(50) NOT NULL UNIQUE,
    nombre VARCHAR2(100) NOT NULL,
    categoria VARCHAR2(50) NOT NULL,
    precio_base NUMBER(10, 0) NOT NULL,
    unidad_medida VARCHAR2(20) DEFAULT 'UNIDAD',
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. TABLA LOTES
CREATE TABLE lotes (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    producto_id NUMBER NOT NULL,
    codigo_lote VARCHAR2(50) NOT NULL,
    fecha_vencimiento DATE NOT NULL,
    cantidad_inicial NUMBER(8, 0) NOT NULL,
    cantidad_actual NUMBER(8, 0) NOT NULL,
    porcentaje_descuento_fefo NUMBER(3, 0) DEFAULT 0,
    CONSTRAINT fk_lotes_producto FOREIGN KEY (producto_id) REFERENCES productos(id),
    CONSTRAINT chk_cantidad_positiva CHECK (cantidad_actual >= 0)
);

-- ÍNDICE OPTIMIZADO PARA EL ALGORITMO FEFO
CREATE INDEX idx_fefo_optimo ON lotes (producto_id, fecha_vencimiento, cantidad_actual);

-- 5. TABLA VENTAS
CREATE TABLE ventas (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    usuario_id NUMBER NOT NULL,
    cliente_id NUMBER NULL,
    fecha_venta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_bruto NUMBER(10, 0) NOT NULL,
    total_descuento NUMBER(10, 0) DEFAULT 0,
    total_neto NUMBER(10, 0) NOT NULL,
    tipo_pago VARCHAR2(20) NOT NULL CHECK (tipo_pago IN ('EFECTIVO', 'TARJETA', 'FIADO')),
    CONSTRAINT fk_ventas_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    CONSTRAINT fk_ventas_cliente FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

-- 6. TABLA DETALLE_VENTAS
CREATE TABLE detalle_ventas (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    venta_id NUMBER NOT NULL,
    producto_id NUMBER NOT NULL,
    lote_id NUMBER NOT NULL,
    cantidad NUMBER(8, 0) NOT NULL,
    precio_unitario NUMBER(10, 0) NOT NULL,
    descuento_aplicado NUMBER(10, 0) DEFAULT 0,
    subtotal NUMBER(10, 0) NOT NULL,
    CONSTRAINT fk_det_venta FOREIGN KEY (venta_id) REFERENCES ventas(id),
    CONSTRAINT fk_det_producto FOREIGN KEY (producto_id) REFERENCES productos(id),
    CONSTRAINT fk_det_lote FOREIGN KEY (lote_id) REFERENCES lotes(id)
);

-- 7. TABLA ABONOS_FIADO
CREATE TABLE abonos_fiado (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    cliente_id NUMBER NOT NULL,
    monto_abonado NUMBER(10, 0) NOT NULL,
    fecha_abono TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    medio_pago VARCHAR2(20) DEFAULT 'EFECTIVO' CHECK (medio_pago IN ('EFECTIVO', 'TRANSFERENCIA', 'TARJETA')),
    CONSTRAINT fk_abonos_cliente FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

-- 8. TABLA NOTIFICACIONES_WA
CREATE TABLE notificaciones_wa (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    cliente_id NUMBER NOT NULL,
    telefono_destino VARCHAR2(15) NOT NULL,
    mensaje VARCHAR2(500) NOT NULL,
    estado VARCHAR2(20) DEFAULT 'PENDIENTE' CHECK (estado IN ('PENDIENTE', 'ENVIADO', 'FALLIDO')),
    fecha_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_notif_cliente FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);