from fastapi import APIRouter, Response
from config.db import conn
from schemas.consoles import consoleEntity, consolesEntity
from models.consoles import Console
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

consola = APIRouter()


@consola.get("/consolas",response_model=list[Console], tags=["Consolas"])
def get_all_consoles():
    return consolesEntity(conn.collectvg.consoles.find())


@consola.post("/consolas", response_model=Console, tags=["Consolas"])
def create_consoles(console: Console):
    new_console = dict(console)
    del new_console["id"]
    id = conn.collectvg.consoles.insert_one(new_console).inserted_id
    console = conn.collectvg.consoles.find_one({"_id": id})
    return consoleEntity(console)


@consola.put("/consolas/{id}", response_model=Console, tags=["Consolas"])
def update_console(id: str, consola: Console):
    updatedconsole = consoleEntity(conn.collectvg.consoles.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(consola)}))
    return consoleEntity(conn.collectvg.consoles.find_one({"_id": ObjectId(id)}))


@consola.delete("/consolas/{id}", tags=["Consolas"])
def delete_console(id: str):
    consoleEntity(conn.collectvg.consoles.find_one_and_delete(
        {"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)


@consola.get("/consolas/{id}", response_model=Console, tags=["Consolas"])
def get_one_console(id: str):
    return consoleEntity(conn.collectvg.consoles.find_one({"_id": ObjectId(id)}))
