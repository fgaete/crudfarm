def consoleEntity(item) -> dict:
    return {
        "_id" : item["id"],
        "name": item["name"],
        "company": item["company"],
        "year": item["year"]
    }
