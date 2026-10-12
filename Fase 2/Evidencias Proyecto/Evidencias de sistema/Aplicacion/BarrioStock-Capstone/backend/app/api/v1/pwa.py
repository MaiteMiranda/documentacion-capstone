from fastapi import APIRouter, Depends
import oracledb
from datetime import datetime

from app.core.database import get_db
from app.schemas.pwa import OfertasExpressCatalogResponse, OfertaExpressItem

router = APIRouter(prefix="/pwa", tags=["4. Catálogo Público PWA Vecinos"])

@router.get("/ofertas-express", response_model=OfertasExpressCatalogResponse)
def consultar_ofertas_express(db: oracledb.Connection = Depends(get_db)):

    ofertas_mock = [
        OfertaExpressItem(
            producto_id=10,
            nombre="Yogurt Vainilla 125g",
            categoria="Llácteos",
            precio_normal=1500.0,
            precio_oferta=1050.0,
            porcentaje_descuento=30.0,
            dias_para_vencer=2,
            stock_disponible=12
        )
    ]

    return OfertasExpressCatalogResponse(
        total_ofertas=len(ofertas_mock),
        fecha_actualizacion=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        ofertas=ofertas_mock
    )