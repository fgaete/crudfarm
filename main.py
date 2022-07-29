from fastapi import FastAPI
from routes.consoles import consola

app = FastAPI(
    title="APIS de Sistema de Colección"
)

app.include_router(consola)