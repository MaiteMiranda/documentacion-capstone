from fastapi import APIRouter, Depends, HTTPException, status
import oracledb
from typing import List
from datetime import datetime

from app.core.database import get_db
from app.schemas.pos import ProductoEscaneadoResponse, VentaCreateRequest, VentaResponse
from app.services.fefo_service import FEFOService

router = APIRouter(prefix="/pos", tags=["1. POS & Motor FEFO"])

@router.get("/productos/escaneo/{codigo_barras}", response_model=ProductoEscaneadoResponse)
def escanear_producto(codigo_barras: str, db: oracledb.Connection = Depends(get_db)):

    dias_vencer = 2
    precio_base = 1500.0
    descuento = FEFOService.calcular_descuento_por_vencimiento(dias_vencer)
    precio_final = precio_base * (1 - descuento / 100)

    return ProductoEscaneadoResponse(
        codigo_barras=codigo_barras,
        nombre="Yogurt Vainilla 125g",
        precio_base=precio_base,
        descuento_fefo_porcentaje=descuento,
        precio_final=precio_final,
        aplica_fefo=descuento > 0,
        dias_para_vencer=dias_vencer,
        lote_id=101
    )

@router.post("/ventas", response_model=VentaResponse, status_code=status.HTTP_201_CREATED)
def procesar_venta(venta: VentaCreateRequest, db: oracledb.Connection = Depends(get_db)):
  
    if not venta.items:
        raise HTTPException(status_code=400, detail="El carrito de venta está vacío")

    total_bruto = sum(item.precio_unitario * item.cantidad for item in venta.items)
    total_descuento = sum(item.descuento_aplicado * item.cantidad for item in venta.items)
    total_neto = total_bruto - total_descuento

    return VentaResponse(
        venta_id=5001,
        total_bruto=total_bruto,
        total_descuento=total_descuento,
        total_neto=total_neto,
        medio_pago=venta.medio_pago,
        fecha_venta=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        mensaje="Venta procesada exitosamente"
    )