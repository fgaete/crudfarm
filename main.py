from fastapi import FastAPI
from routes.consoles import consola

app = FastAPI()

app.include_router(consola)