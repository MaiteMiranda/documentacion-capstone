from pydantic import BaseModel
from typing import List

class OfertaExpressItem(BaseModel):
    producto_id: int
    nombre: str
    categoria: str
    precio_normal: float
    precio_oferta: float
    porcentaje_descuento: float
    dias_para_vencer: int
    stock_disponible: int

class OfertasExpressCatalogResponse(BaseModel):
    total_ofertas: int
    fecha_actualizacion: str
    ofertas: List[OfertaExpressItem]