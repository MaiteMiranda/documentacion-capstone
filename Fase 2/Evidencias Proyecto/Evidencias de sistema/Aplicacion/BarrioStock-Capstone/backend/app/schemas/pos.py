from pydantic import BaseModel, Field
from typing import List, Optional

class ProductoEscaneadoResponse(BaseModel):
    codigo_barras: str
    nombre: str
    precio_base: float = Field(..., ge=0)
    descuento_fefo_porcentaje: float = Field(..., ge=0, le=100)
    precio_final: float = Field(..., ge=0)
    aplica_fefo: bool
    dias_para_vencer: int
    lote_id: int

class VentaItemRequest(BaseModel):
    producto_id: int
    lote_id: int
    cantidad: int = Field(..., gt=0)
    precio_unitario: float = Field(..., ge=0)
    descuento_aplicado: float = Field(0.0, ge=0)

class VentaCreateRequest(BaseModel):
    medio_pago: str = Field(..., description="'EFECTIVO', 'TARJETA' o 'FIADO'")
    cliente_id: Optional[int] = Field(None, description="Requerido solo si medio_pago es FIADO")
    items: List[VentaItemRequest]

class VentaResponse(BaseModel):
    venta_id: int
    total_bruto: float
    total_descuento: float
    total_neto: float
    medio_pago: str
    fecha_venta: str
    mensaje: str