from pydantic import BaseModel, Field

class ClienteFiadoResponse(BaseModel):
    cliente_id: int
    rut: str
    nombre: str
    telefono: str
    limite_credito: float
    saldo_deuda: float
    cupo_disponible: float

class AbonoFiadoRequest(BaseModel):
    cliente_id: int = Field(..., gt=0)
    monto_abono: float = Field(..., gt=0, description="Monto en CLP a abonar")
    medio_pago: str = Field("EFECTIVO", description="'EFECTIVO' o 'TRANSFERENCIA'")

class AbonoFiadoResponse(BaseModel):
    abono_id: int
    cliente_id: int
    monto_abonado: float
    nuevo_saldo_deuda: float
    cupo_disponible: float
    fecha_abono: str