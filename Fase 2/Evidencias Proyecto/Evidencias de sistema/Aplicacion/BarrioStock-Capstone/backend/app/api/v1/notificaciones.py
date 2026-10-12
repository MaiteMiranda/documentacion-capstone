from fastapi import APIRouter, Depends, status
import oracledb

from app.core.database import get_db
from app.schemas.notificaciones import WhatsAppNotificacionRequest, WhatsAppNotificacionResponse

router = APIRouter(prefix="/notificaciones", tags=["3. WhatsApp Meta API"])

@router.post("/whatsapp/cobro", response_model=WhatsAppNotificacionResponse, status_code=status.HTTP_200_OK)
def enviar_recordatorio_cobro(payload: WhatsAppNotificacionRequest, db: oracledb.Connection = Depends(get_db)):

    return WhatsAppNotificacionResponse(
        notificacion_id=8801,
        cliente="Juan Pérez",
        telefono="+56912345678",
        monto_deuda=15000.0,
        estado_envio="ENVIADO",
        mensaje_preview="Hola Juan Pérez, te recordamos que tienes un saldo pendiente de $15.000 en BarrioStock."
    )