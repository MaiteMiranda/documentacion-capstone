# Manual Técnico y Despliegue — BarrioStock

## 1. Propósito del documento

Este manual describe cómo instalar, configurar, ejecutar y desplegar BarrioStock. Incluye Docker Compose, variables de entorno, ejecución local, pruebas, Telegram y resolución de problemas.

## 2. Alcance

El manual cubre:

- Frontend React.
- Backend FastAPI.
- Oracle Database 23c.
- Docker Compose.
- Desarrollo local.
- Despliegue independiente en Railway.
- Configuración de Telegram.
- Ejecución de pruebas.
- Uso básico del POS.

## 3. Tecnologías requeridas

### Para desarrollo local

- Git.
- Docker Desktop.
- Node.js 20 o superior.
- npm.
- Python 3.11 o superior.
- Navegador moderno.
- Oracle Database 23c Free, mediante Docker Compose.

### Opcional

- Cuenta de Telegram.
- Bot creado en BotFather.
- Chat ID para recordatorios.
- Cuenta de Railway.

## 4. Repositorios

El proyecto utiliza:

- Repositorio de código: `BarrioStock-Capstone`.
- Repositorio de evidencias: documentos, capturas y modelos.

El manual se ejecuta desde la raíz del repositorio de código:

```powershell
cd D:\CAPSTONE-PORTF\BarrioStock-Capstone
```

---

# 5. Estructura del proyecto

```text
BarrioStock-Capstone/
├── backend/
│   ├── app/
│   ├── tests/
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   ├── public/
│   ├── Dockerfile
│   ├── package.json
│   └── vite.config.js
├── database/
│   ├── 01_init.sql
│   ├── 02_seed.sql
│   └── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```

---

# 6. Variables de entorno

Crear un archivo `.env` desde `.env.example`:

```powershell
Copy-Item .env.example .env
```

No subir el archivo `.env` a Git.

## 6.1 Variables generales

```env
PROJECT_NAME=BarrioStock API
API_V1_STR=/api/v1
SECRET_KEY=cambiar-por-un-secreto-largo-y-aleatorio
CORS_ORIGINS=https://tu-dominio-front.up.railway.app
BACKEND_PORT=8000
FRONTEND_PORT=5173
```

## 6.2 Variables Oracle

```env
DB_HOST=oracle-db
DB_PORT=1521
DB_USER=barriostock_user
DB_PASSWORD=cambiar-por-un-password-seguro
DB_SERVICE=FREEPDB1
ORACLE_PASSWORD=cambiar-por-un-password-seguro
ORACLE_PORT=1522
```

### Uso local

Docker Compose puede resolver el backend y la base mediante:

```text
DB_HOST=oracle-db
DB_PORT=1521
```

### Uso fuera de Docker

Cuando el backend se ejecuta directamente en el equipo, utilizar:

```env
DB_HOST=localhost
DB_PORT=1522
```

## 6.3 Variables Telegram

```env
TELEGRAM_BOT_TOKEN=token-entregado-por-BotFather
TELEGRAM_DEFAULT_CHAT_ID=
```

Si no se configura Telegram:

- El sistema puede operar en modo sandbox.
- La API puede devolver `TELEGRAM_BOT_SANDBOX`.
- No se enviará un mensaje real.

## 6.4 Variable frontend

```env
VITE_API_URL=http://localhost:8000/api/v1
```

En producción:

```env
VITE_API_URL=https://dominio-backend.up.railway.app/api/v1
```

> `VITE_API_URL` debe incluir `/api/v1` en el backend.

---

# 7. Configurar CORS

El dominio público del frontend debe estar en `CORS_ORIGINS` sin barra final:

```env
CORS_ORIGINS=https://barriostock.up.railway.app
```

No usar:

```text
https://barriostock.up.railway.app/
```

si la versión del backend exige un origen exacto sin barra final.

Para varios dominios:

```env
CORS_ORIGINS=http://localhost:5173,https://barriostock.up.railway.app
```

---

# 8. Levantar el proyecto con Docker Compose

## 8.1 Archivo Docker Compose

El proyecto incluye:

- `database/Dockerfile`.
- `backend/Dockerfile`.
- `frontend/Dockerfile`.
- `docker-compose.yml`.

## 8.2 Construir y levantar

Desde la raíz del proyecto:

```powershell
docker compose up -d --build
```

## 8.3 Consultar estado

```powershell
docker compose ps
```

## 8.4 Consultar logs

Todos los servicios:

```powershell
docker compose logs -f
```

Base de datos:

```powershell
docker compose logs -f oracle-db
```

Backend:

```powershell
docker compose logs -f backend
```

Frontend:

```powershell
docker compose logs -f frontend
```

## 8.5 Detener contenedores

```powershell
docker compose down
```

## 8.6 Detener y eliminar volúmenes

Esta operación elimina los datos persistentes de Oracle:

```powershell
docker compose down -v
```

Usarla únicamente si se desea reinicializar completamente la base.

---

# 9. Accesos locales

| Servicio | Dirección |
|---|---|
| Frontend | `http://localhost:5173` |
| Backend | `http://localhost:8000` |
| Swagger | `http://localhost:8000/docs` |
| Health backend | `http://localhost:8000/health` |
| Oracle | `localhost:1522` |

La PWA pública puede estar disponible en:

```text
http://localhost:5173/pwa/dontito
```

---

# 10. Inicialización de Oracle

Oracle utiliza:

- `database/01_init.sql`.
- `database/02_seed.sql`.

El script de inicialización crea:

- Usuarios.
- Clientes.
- Productos.
- Lotes.
- Ventas.
- Detalles de venta.
- Abonos.
- Proveedores.
- Movimientos de inventario.

## Advertencia de recursos

Oracle Database Free puede requerir más memoria que un contenedor ligero.

Si el contenedor queda `CRASHED` o reinicia:

- Verificar memoria disponible.
- Aumentar memoria de Docker Desktop.
- Revisar el plan utilizado.
- Verificar que el volumen no esté incompleto.
- Evitar reinicializaciones repetidas si el volumen ya contiene datos.

> Si Oracle no está disponible, el backend puede operar en modo mock de contingencia. En ese modo los datos no son persistentes.

---

# 11. Ejecución manual sin Docker completo

## 11.1 Backend

Crear entorno virtual:

```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Instalar dependencias:

```powershell
pip install -r requirements.txt
```

Iniciar backend:

```powershell
uvicorn app.main:app --reload --port 8000
```

Puede ejecutarse con:

```text
http://localhost:8000/docs
```

## 11.2 Frontend

Abrir otra terminal:

```powershell
cd frontend
npm install
npm run dev
```

Abrir:

```text
http://localhost:5173
```

## 11.3 Oracle individual

Para iniciar Oracle:

```powershell
docker compose up -d oracle-db
```

Y configurar el backend con:

```env
DB_HOST=localhost
DB_PORT=1522
```

---

# 12. Compilación del frontend

Para generar el build de producción:

```powershell
cd frontend
npm run build
```

Los archivos se generan en:

```text
frontend/dist
```

El Dockerfile de frontend puede generar el build y entregar los archivos mediante Nginx.

## Variables necesarias durante build

Si la variable se utiliza con Vite:

```text
VITE_API_URL
```

Debe configurarse antes de construir:

```powershell
$env:VITE_API_URL="https://backend.example.com/api/v1"
npm run build
```

En Railway, configurar la variable dentro del servicio frontend antes de desplegar.

---

# 13. Verificar el backend

Comprobar estado:

```text
GET /health
```

Ejemplo:

```text
http://localhost:8000/health
```

Respuesta esperada:

```json
{
  "status": "online",
  "database": "connected",
  "version": "1.0.0"
}
```

Si Oracle no está disponible:

```json
{
  "database": "mock_standby"
}
```

No afirmar que el sistema tiene persistencia real si la respuesta usa `mock_standby`.

## Estado de Swagger

Swagger permite probar endpoints:

```text
http://localhost:8000/docs
```

Para rutas protegidas:

1. Ejecutar `/api/v1/auth/login`.
2. Copiar `access_token`.
3. Pulsar `Authorize`.
4. Ingresar:

```text
Bearer COPIA_EL_TOKEN_AQUI
```

---

# 14. Iniciar sesión

## Usuarios de prueba

El archivo seed contiene usuarios de prueba. Se debe cambiar su contraseña o crear nuevos usuarios antes de una instalación productiva.

Ejemplo:

| Usuario | Rol |
|---|---|
| Karen Fernández | ADMIN |
| Maite Miranda | ADMIN |
| Almacenero Don Tito | CAJERO |

El login requiere:

- RUT válido.
- Contraseña.
- Dígito verificador correcto.

Ejemplo de petición:

```json
{
  "rut": "18.698.365-3",
  "password": "BarrioStockPass2026!"
}
```

Endpoint:

```text
POST /api/v1/auth/login
```

---

# 15. Operación del POS

## 15.1 Buscar productos

El POS permite:

- Buscar por nombre.
- Buscar por código.
- Seleccionar productos frecuentes.
- Escanear mediante lector USB.

## 15.2 Uso del lector USB

Un lector USB actúa como un teclado:

1. Conectar el lector.
2. Abrir el módulo POS.
3. Ubicar el cursor en el campo de búsqueda.
4. Escanear el código.
5. El lector escribe los dígitos.
6. El lector envía Enter.
7. React consulta el producto.

Flujo:

```text
GET /api/v1/pos/productos/escaneo/{codigo_barras}
```

La aplicación no implementa lectura mediante cámara.

## 15.3 Agregar al carrito

El usuario puede:

- Seleccionar un producto.
- Modificar cantidad.
- Eliminar productos.
- Vaciar el carrito.

## 15.4 Confirmar venta

Métodos disponibles:

- EFECTIVO.
- TARJETA.
- FIADO.

Endpoint:

```text
POST /api/v1/pos/ventas
```

La venta:

- Valida el carrito.
- Valida el stock.
- Valida el límite si es fiado.
- Actualiza lotes.
- Actualiza deudas.
- Genera el recibo digital.

---

# 16. Motor FEFO

FEFO significa:

**First Expired, First Out**

Primero expira, primero sale.

## Reglas

| Días al vencimiento | Descuento |
|---|---:|
| Vencido o 0 días | 50% |
| 1 a 3 días | 30% |
| 4 a 7 días | 15% |
| Más de 7 días | Sin descuento |

## Verificación

Ejemplo:

- Yogurt con 2 días: 30%.
- Leche con 3 días: 30%.
- Coca-Cola con 90 días: sin descuento.

---

# 17. Módulo de fiados

## Crear cliente

Datos necesarios:

- RUT.
- Nombre.
- Chat ID de Telegram.
- Límite de crédito.

## Validaciones

- RUT válido.
- Nombre válido.
- Chat ID válido cuando se utiliza Telegram.
- Límite mayor o igual a cero.
- RUT único.
- Límite no menor que la deuda existente.

## Registrar abono

Un abono:

- Debe ser mayor que cero.
- No puede superar la deuda.
- Actualiza el saldo.
- Permite cambiar el estado.

## Historial

El sistema permite consultar:

- Movimientos de cuenta.
- Cargos por ventas.
- Abonos.
- Compras anteriores.
- Productos frecuentes.

---

# 18. Configurar Telegram

## 18.1 Crear bot

1. Abrir Telegram.
2. Buscar `@BotFather`.
3. Ejecutar `/newbot`.
4. Ingresar el nombre del bot.
5. Ingresar el nombre de usuario.
6. Copiar el token.

## 18.2 Obtener Chat ID

### Forma manual

Enviar un mensaje al bot y consultar:

```text
https://api.telegram.org/botTOKEN/getUpdates
```

Buscar:

```json
"chat": {
  "id": 123456789
}
```

El identificador puede ser positivo o negativo.

## 18.3 Configurar cliente

Registrar el Chat ID en el campo de Telegram del cliente.

> No se debe confundir el Chat ID con el número de teléfono.

## 18.4 Configurar variables

```env
TELEGRAM_BOT_TOKEN=123456:token-real
TELEGRAM_DEFAULT_CHAT_ID=123456789
```

En un despliegue, guardar el token como secreto.

## 18.5 Enviar prueba

Endpoint:

```text
POST /api/v1/notificaciones/telegram
```

Cuerpo:

```json
{
  "cliente_id": 1
}
```

Respuesta real:

```json
{
  "status": "ENVIADO",
  "proveedor": "TELEGRAM_BOT_API"
}
```

Modo sandbox:

```json
{
  "status": "ENVIADO",
  "proveedor": "TELEGRAM_BOT_SANDBOX"
}
```

---

# 19. Administración de inventario

Accesible para usuarios con rol `ADMIN`.

## Crear producto

Campos:

- Código de barras.
- Nombre.
- Categoría.
- Precio base.
- Unidad de medida.
- Stock mínimo.

Endpoint:

```text
POST /api/v1/admin/inventario/productos
```

## Editar producto

Endpoint:

```text
PATCH /api/v1/admin/inventario/productos/{product_id}
```

## Crear proveedor

Endpoint:

```text
POST /api/v1/admin/inventario/proveedores
```

---

# 20. Recepción de inventario

El administrador registra:

- Proveedor.
- Número de documento.
- Código de barras.
- Código de lote.
- Cantidad.
- Fecha de vencimiento.
- Costo.

Endpoint:

```text
POST /api/v1/admin/inventario/recepciones
```

La recepción:

- Verifica que el producto exista.
- Crea o actualiza lotes.
- Aumenta el stock disponible.
- Registra movimiento `COMPRA`.
- Conserva trazabilidad.

---

# 21. Importación masiva

## Formato CSV

El archivo debe estar codificado en UTF-8.

Ejemplo:

```csv
codigo_barras,nombre,categoria,precio_base,unidad_medida,stock_minimo
7801234567890,Pan Hallulla,Panadería,1800,UNIDAD,5
7809876543210,Coca-Cola,Bebidas,2000,UNIDAD,3
```

## Formato Excel

Extensión aceptada:

```text
.xlsx
```

Los encabezados deben coincidir con:

```text
codigo_barras
nombre
categoria
precio_base
unidad_medida
stock_minimo
```

Endpoint:

```text
POST /api/v1/admin/inventario/productos/importar
```

## Validaciones

- Archivo obligatorio.
- Extensión válida.
- CSV sin encabezados rechazado.
- Excel vacío rechazado.
- Encabezados obligatorios.
- Precio válido.
- Código único.
- Cantidades válidas.

---

# 22. PWA pública

La aplicación pública está disponible en:

```text
/pwa/dontito
```

También puede consultar:

```text
GET /api/v1/catalog/ofertas-express
```

## Características

- No requiere iniciar sesión.
- Consulta productos con FEFO.
- Muestra precio normal.
- Muestra precio rebajado.
- Muestra descuento.
- Muestra días hasta el vencimiento.
- Puede agregarse al inicio del celular.

---

# 23. Despliegue en Railway

## 23.1 Crear servicios separados

Crear tres servicios:

1. Frontend.
2. Backend.
3. Base de datos o Oracle externo.

> Oracle requiere recursos adecuados. No se recomienda asumir que funcionará en un plan gratuito sin prueba.

## 23.2 Configurar backend

En la raíz del servicio backend:

```text
/backend
```

Variables:

```env
API_V1_STR=/api/v1
SECRET_KEY=secreto-real-largo
CORS_ORIGINS=https://dominio-frontend.up.railway.app
DB_HOST=dominio-o-servicio-oracle
DB_PORT=1521
DB_USER=barriostock_user
DB_PASSWORD=password-real
DB_SERVICE=FREEPDB1
TELEGRAM_BOT_TOKEN=token-real
TELEGRAM_DEFAULT_CHAT_ID=
```

No incluir barra final en el dominio frontend.

## 23.3 Configurar frontend

En la raíz:

```text
/frontend
```

Variable:

```env
VITE_API_URL=https://dominio-backend.up.railway.app/api/v1
```

Verificar que el build use esta variable.

## 23.4 Configurar dominio

Ejemplo frontend:

```text
https://barriostock.up.railway.app
```

Ejemplo backend:

```text
https://barriostock-prod.up.railway.app
```

Configurar el dominio exacto en CORS.

---

# 24. Health checks

Backend:

```text
GET /health
GET /api/v1/health
```

Frontend:

```text
https://dominio-frontend/
```

PWA:

```text
https://dominio-frontend/pwa/dontito
```

No confundir el estado `mock_standby` con una base persistente conectada.

---

# 25. Pruebas

## Backend

Ejecutar:

```powershell
cd backend
python -m pytest -q
```

Resultado confirmado:

```text
77 pruebas aprobadas
```

Pruebas incluidas:

- FEFO.
- Login.
- RUT.
- Tokens.
- Seguridad.
- POS.
- Fiados.
- Abonos.
- Inventario.
- CSV.
- Excel.
- PWA.
- Telegram.

## Frontend

Ejecutar:

```powershell
cd frontend
npm test
```

Resultado confirmado:

```text
41 pruebas aprobadas
```

Pruebas incluidas:

- Login.
- RUT.
- Validaciones de clientes.
- Abonos.
- Header.
- Navegación por roles.
- Modales.

## Build

```powershell
cd frontend
npm run build
npm run lint
```

Resultados esperados:

- Build aprobado.
- ESLint aprobado.
- PWA generada.

---

# 26. Seguridad

## Contraseñas

Las contraseñas se almacenan mediante hash PBKDF2-HMAC-SHA256.

No almacenar contraseñas sin cifrar.

## Tokens

El backend entrega un token Bearer.

El frontend lo envía en:

```text
Authorization: Bearer TOKEN
```

## Variables secretas

Nunca subir:

- SECRET_KEY.
- DB_PASSWORD.
- ORACLE_PASSWORD.
- TELEGRAM_BOT_TOKEN.

Usar `.env.example` sin valores reales.

## Base de datos

- Usar conexiones parametrizadas.
- Restringir Oracle a la red Docker.
- No exponer Oracle públicamente.
- Cambiar contraseñas seed.

## CORS

Configurar solo dominios reales.

Ejemplo:

```env
CORS_ORIGINS=https://barriostock.up.railway.app
```

---

# 27. Resolución de problemas

## Frontend no inicia

Revisar:

```powershell
npm install
npm run build
```

Comprobar:

- Node.js.
- `package-lock.json`.
- Dependencias instaladas.

## Backend no inicia

Revisar:

```powershell
pip install -r requirements.txt
```

Comprobar:

- Variables Oracle.
- Puerto 8000.
- SECRET_KEY.
- Dependencias.

## Oracle queda CRASHED

Síntomas:

- Reinicios repetidos.
- Memoria insuficiente.
- Uncompressing database data.
- OOM Killed.

Acciones:

- Aumentar memoria.
- Revisar disponibilidad del plan.
- Mantener volumen persistente.
- Esperar la primera inicialización.
- No eliminar el volumen si no es necesario.

## Frontend responde 404 al login

Revisar:

```env
VITE_API_URL=https://backend.example.com/api/v1
```

Comprobación:

```text
POST /api/v1/auth/login
```

No utilizar:

```text
POST /auth/login
```

si el backend está configurado bajo `/api/v1`.

## Nginx indica backend inexistente

Si aparece:

```text
host not found in upstream "backend"
```

La configuración Nginx fue creada para Docker Compose.

En Railway:

- No usar `proxy_pass http://backend:8000`.
- Usar `VITE_API_URL`.
- Servir los archivos frontend directamente.

## Telegram no envía

Revisar:

- Token.
- Chat ID.
- Usuario que inició el bot.
- Conexión HTTPS.
- Respuesta de Telegram.

## Importación falla

Revisar:

- Encabezados.
- Separadores.
- UTF-8.
- Extensión.
- Precios.
- Código único.
- Archivo `.xlsx`.

---

# 28. Evidencias para anexar

Insertar capturas de:

1. Docker Compose ejecutándose.
2. Contenedores backend, frontend y Oracle.
3. Swagger.
4. Login.
5. Inicio.
6. POS.
7. Producto FEFO.
8. Venta efectiva.
9. Venta fiada.
10. Fiados.
11. Abono.
12. Alertas.
13. Historial.
14. Inventario.
15. CSV.
16. Excel `.xlsx`.
17. PWA.
18. Telegram.
19. Pruebas backend.
20. Pruebas frontend.
21. Build frontend.
22. Despliegue Railway.
23. Variables de entorno sin valores secretos.

---

# 29. Conclusión

BarrioStock puede ejecutarse localmente mediante Docker Compose y puede desplegarse mediante servicios separados en Railway.

Antes de una defensa o entrega, se debe confirmar:

- Oracle está disponible con persistencia real.
- El backend responde.
- El frontend se conecta al backend.
- CORS coincide con el dominio.
- Telegram fue probado.
- Las 77 pruebas backend están aprobadas.
- Las 41 pruebas frontend están aprobadas.
- Los archivos `.env` reales no están versionados.

---

## Comandos rápidos

```powershell
# Levantar sistema
docker compose up -d --build

# Ver estado
docker compose ps

# Ver logs
docker compose logs -f

# Ejecutar backend
cd backend
uvicorn app.main:app --reload --port 8000

# Ejecutar frontend
cd frontend
npm install
npm run dev

# Ejecutar pruebas backend
cd backend
python -m pytest -q

# Ejecutar pruebas frontend
cd frontend
npm test
npm run build
npm run lint
```