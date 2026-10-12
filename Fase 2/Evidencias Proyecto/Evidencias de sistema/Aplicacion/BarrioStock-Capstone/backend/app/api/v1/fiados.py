from fastapi import APIRouter, Depends, HTTPException, status
import oracledb
from typing import List
from datetime import datetime

from app.core.database import get_db
from app.schemas.fiados import ClienteFiadoResponse, AbonoFiadoRequest, AbonoFiadoResponse

router = APIRouter(prefix="/fiados", tags=["2. Cuaderno Digital de Fiados"])

@router.get("/clientes", response_model=List[ClienteFiadoResponse])
def listar_clientes_fiado(db: oracledb.Connection = Depends(get_db)):
    return [
        ClienteFiadoResponse(
            cliente_id=1,
            rut="12345678-9",
            nombre="Juan Pérez",
            telefono="+56912345678",
            limite_credito=50000.0,
            saldo_deuda=15000.0,
            cupo_disponible=35000.0
        )
    ]

@router.post("/abonos", response_model=AbonoFiadoResponse, status_code=status.HTTP_201_CREATED)
def registrar_abono(abono: AbonoFiadoRequest, db: oracledb.Connection = Depends(get_db)):
    saldo_actual = 15000.0
    limite = 50000.0

    if abono.monto_abono > saldo_actual:
        raise HTTPException(status_code=400, detail="El abono no puede superar el saldo deudor actual")

    nuevo_saldo = saldo_actual - abono.monto_abono

    return AbonoFiadoResponse(
        abono_id=901,
        cliente_id=abono.cliente_id,
        monto_abonado=abono.monto_abono,
        nuevo_saldo_deuda=nuevo_saldo,
        cupo_disponible=limite - nuevo_saldo,
        fecha_abono=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )