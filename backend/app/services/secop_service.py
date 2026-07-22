import os
import httpx


class SecopService:

    def obtener_procesos(self):

        url = os.getenv("SECOP_API_URL")

        respuesta = httpx.get(
            url,
            params={
                "$limit": int(os.getenv("SECOP_DEFAULT_LIMIT", 5))
            }
        )

        return respuesta.json()