from typing import Optional
from fastapi import APIRouter

from app.services.secop_service import SecopService

router = APIRouter()

secop_service = SecopService()


@router.get("/procesos")
def obtener_procesos(
    limit: int = 5,
    buscar: Optional[str] = None,
    estado: Optional[str] = None,
):
    return secop_service.obtener_procesos(
        limit=limit,
        buscar=buscar,
        estado=estado,
    )


@router.get("/catalogos/{campo}")
def obtener_catalogo(campo: str):
    return secop_service.obtener_catalogo(campo)
