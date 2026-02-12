from fastapi import FastAPI, HTTPException

from schemas import Item, ItemId, ItemIn, ItemUpdate

app = FastAPI()

# Fake in-memory database (resets on restart)
fake_db = {}
next_id = 1


@app.get("/")
def read_root():
    return {"items": list(fake_db.values())}


@app.post("/")
def create_root(item: ItemIn):
    global next_id
    item_out = Item(id=next_id, **item.dict())
    fake_db[next_id] = item_out.dict()
    next_id += 1
    return item_out


@app.put("/")
def update_root(item: ItemUpdate):
    if item.id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    stored = fake_db[item.id]
    if item.name is not None:
        stored["name"] = item.name
    if item.description is not None:
        stored["description"] = item.description
    fake_db[item.id] = stored
    return stored


@app.delete("/")
def delete_root(item: ItemId):
    if item.id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted = fake_db.pop(item.id)
    return {"deleted": deleted}
