from fastapi import APIRouter

from app.services.secop_service import SecopService

router = APIRouter()

secop_service = SecopService()


@router.get("/procesos")
def obtener_procesos():
    return secop_service.obtener_procesos()
