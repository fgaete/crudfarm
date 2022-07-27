from fastapi import APIRouter
from config.db import conn
from schemas.consoles import consoleEntity,consolesEntity
from models.consoles import Console

consola = APIRouter()

@consola.get("/consolas")
def get_all_consoles():
    return consolesEntity(conn.collectvg.consoles.find())

@consola.post("/consolas")
def create_consoles(console: Console):
    new_console = dict(console)
    del new_console["id"]
    id = conn.collectvg.consoles.insert_one(new_console).inserted_id
    console = conn.collectvg.consoles.find_one({"_id":id})
    return consoleEntity(console)

@consola.put("/consolas/{id}")
def update_console():
    return "hello world consolas"

@consola.delete("/consolas/{id}")
def delete_console():
    return "hello world consolas"

@consola.get("/consolas/{id}")
def get_one_console():
    return "hello world consolas"