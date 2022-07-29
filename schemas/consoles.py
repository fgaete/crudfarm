def consoleEntity(item) -> dict:
    return {
        "id" : str(item["_id"]),
        "name": item["name"],
        "company": item["company"],
        "year": item["year"]
    }
def consolesEntity(entity) -> list:
    return [consoleEntity(item) for item in entity]