from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1.pos import router as pos_router
from app.api.v1.fiados import router as fiados_router
from app.api.v1.notificaciones import router as notificaciones_router
from app.api.v1.pwa import router as pwa_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    description="API REST de BarrioStock - POS, Motor FEFO, Fiados y WhatsApp Meta API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pos_router, prefix=settings.API_V1_STR)
app.include_router(fiados_router, prefix=settings.API_V1_STR)
app.include_router(notificaciones_router, prefix=settings.API_V1_STR)
app.include_router(pwa_router, prefix=settings.API_V1_STR)

@app.get("/health", tags=["Health Check"])
def health_check():
    return {"status": "online", "system": settings.PROJECT_NAME}