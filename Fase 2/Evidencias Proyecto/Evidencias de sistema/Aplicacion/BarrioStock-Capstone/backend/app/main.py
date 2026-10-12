from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="BarrioStock API",
    version="1.0.0",
    description="API REST para POS, Motor FEFO y Fiados"
)

# Configuración de CORS para permitir peticiones desde React
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/v1/health", tags=["Health Check"])
def health_check():
    return {
        "status": "online",
        "system": "BarrioStock Backend",
        "version": "1.0.0"
    }