from fastapi import APIRouter

consola = APIRouter()

@consola.get("/consolas")
def get_all_consoles():
    return "hello world consolas"

@consola.post("/consolas")
def create_consoles():
    return "hello world consolas"

@consola.put("/consolas/{id}")
def update_console():
    return "hello world consolas"

@consola.delete("/consolas/{id}")
def delete_console():
    return "hello world consolas"

@consola.get("/consolas/{id}")
def get_one_console():
    return "hello world consolas"