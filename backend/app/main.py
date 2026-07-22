from fastapi import FastAPI

from dotenv import load_dotenv
import os

from app.api.routes.secop_routes import router as secop_router

# Cargar variables del archivo .env
load_dotenv()

app = FastAPI(
    title="SECOP Smart API",
    description="Sistema para consulta de procesos SECOP II",
    version="1.0.0"
)

@app.get("/")
def inicio():

    return {
        "mensaje": "Bienvenido a SECOP Smart 🚀",
        "api_secop": os.getenv("SECOP_API_URL")
    }
    
app.include_router(secop_router)