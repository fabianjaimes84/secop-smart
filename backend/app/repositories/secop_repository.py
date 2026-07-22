import httpx
from app.core.config import settings


class SecopRepository:
    def obtener_procesos(
        self,
        limit: int = 5,
        buscar: str | None = None,
        estado: str | None = None,
    ):

        url = settings.SECOP_API_URL

        params = {"$limit": limit}

        if buscar:
            params["$q"] = buscar

        if estado:
            params["estado_del_procedimiento"] = estado

        respuesta = httpx.get(url, params=params, timeout=settings.TIMEOUT)

        respuesta.raise_for_status()

        return respuesta.json()

    def obtener_catalogo(self, campo: str):
        params = {
            "$select": campo,
            "$group": campo,
            "$order": campo,
        }

        response = httpx.get(
            settings.SECOP_API_URL,
            params=params,
            timeout=settings.TIMEOUT,
        )

        response.raise_for_status()

        return response.json()
