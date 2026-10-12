from pydantic import BaseModel, Field

class WhatsAppNotificacionRequest(BaseModel):
    cliente_id: int = Field(..., gt=0)

class WhatsAppNotificacionResponse(BaseModel):
    notificacion_id: int
    cliente: str
    telefono: str
    monto_deuda: float
    estado_envio: str = Field(..., description="'ENVIADO' o 'FALLIDO'")
    mensaje_preview: str