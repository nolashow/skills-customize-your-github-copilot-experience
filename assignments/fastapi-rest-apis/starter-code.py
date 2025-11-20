from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Simple FastAPI Example")

class Item(BaseModel):
    id: int
    title: str = Field(..., max_length=100, example="My Item")
    description: Optional[str] = Field(None, max_length=300)

# In-memory "database"
items = {}
next_id = 1

@app.get("/items", response_model=List[Item])
def list_items(limit: int = 10):
    return list(items.values())[:limit]

@app.post("/items", status_code=201, response_model=Item)
def create_item(item: Item):
    global next_id
    item.id = next_id
    next_id += 1
    items[item.id] = item
    return item

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return None
