-- DATOS DE PRUEBA INICIALES - BARRIOSTOCK

-- USUARIOS
INSERT INTO usuarios (rut, nombre, rol, password_hash) 
VALUES ('18.698.365-3', 'Karen Fernández', 'ADMIN', 'hash_karen_2026');
INSERT INTO usuarios (rut, nombre, rol, password_hash) 
VALUES ('19.579.696-3', 'Maite Miranda', 'ADMIN', 'hash_maite_2026');

-- CLIENTES (FIADOS)
INSERT INTO clientes (rut, nombre, telefono, limite_credito, saldo_deuda) 
VALUES ('12.345.678-5', 'Juan Pérez', '+56912345678', 50000, 12500);
INSERT INTO clientes (rut, nombre, telefono, limite_credito, saldo_deuda) 
VALUES ('15.234.567-6', 'María González', '+56987654321', 40000, 8000);
INSERT INTO clientes (rut, nombre, telefono, limite_credito, saldo_deuda) API_CONTRACT.mdAPI_CONTRACT.md
VALUES ('10.987.654-5', 'Pedro Soto', '+56965432109', 50000, 24500);

-- PRODUCTOS
INSERT INTO productos (codigo_barras, nombre, categoria, precio_base, unidad_medida) 
VALUES ('7801234567890', 'Pan Hallulla 1Kg', 'Panadería', 1800, 'KG');
INSERT INTO productos (codigo_barras, nombre, categoria, precio_base, unidad_medida) 
VALUES ('7809876543210', 'Coca-Cola 2L', 'Bebidas', 2000, 'UNIDAD');
INSERT INTO productos (codigo_barras, nombre, categoria, precio_base, unidad_medida) 
VALUES ('7804567890123', 'Yogurt Batido Frutilla', 'Lácteos', 450, 'UNIDAD');
INSERT INTO productos (codigo_barras, nombre, categoria, precio_base, unidad_medida) 
VALUES ('7806543210987', 'Leche Entera 1L', 'Lácteos', 1190, 'UNIDAD');

-- LOTES CON DESCUENTO FEFO (PRÓXIMOS A VENCER EN OCTUBRE 2026)
INSERT INTO lotes (producto_id, codigo_lote, fecha_vencimiento, cantidad_inicial, cantidad_actual, porcentaje_descuento_fefo) 
VALUES (3, 'L-OCT-01', SYSDATE + 2, 20, 15, 30); -- Yogurt vence en 2 días (30% OFF)

INSERT INTO lotes (producto_id, codigo_lote, fecha_vencimiento, cantidad_inicial, cantidad_actual, porcentaje_descuento_fefo) 
VALUES (4, 'L-OCT-02', SYSDATE + 3, 10, 8, 30); -- Leche vence en 3 días (30% OFF)

INSERT INTO lotes (producto_id, codigo_lote, fecha_vencimiento, cantidad_inicial, cantidad_actual, porcentaje_descuento_fefo) 
VALUES (2, 'L-OCT-99', SYSDATE + 90, 50, 45, 0); -- Coca-Cola vence en 3 meses (Sin descuento)

COMMIT;