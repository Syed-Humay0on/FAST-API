from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
import motor.motor_asyncio
from dotenv import load_dotenv
import os

# FastAPI app
app = FastAPI()

# MongoDB connection
MONGO_URL = os.getenv("MONGO_URL")
client = motor.motor_asyncio.AsyncIOMotorClient("MONGO_URL")
db = client.mydb
collection = db.items

# Helper to convert ObjectId to string
def item_helper(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "description": item.get("description"),
        "price": item["price"]
    }

# Pydantic model
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

# ✅ Create
@app.post("/items/")
async def create_item(item: Item):
    new_item = await collection.insert_one(item.model_dump())
    created_item = await collection.find_one({"_id": new_item.inserted_id})
    return item_helper(created_item)

# ✅ Read all
@app.get("/items/")
async def get_items():
    items = []
    async for item in collection.find():
        items.append(item_helper(item))
    return items

# ✅ Read one
@app.get("/items/{item_id}")
async def get_item(item_id: str):
    item = await collection.find_one({"_id": ObjectId(item_id)})
    if item:
        return item_helper(item)
    raise HTTPException(status_code=404, detail="Item not found")

# ✅ Update
@app.put("/items/{item_id}")
async def update_item(item_id: str, updated_item: Item):
    result = await collection.update_one(
        {"_id": ObjectId(item_id)},
        {"$set": updated_item.model_dump()}
    )
    if result.modified_count == 1:
        item = await collection.find_one({"_id": ObjectId(item_id)})
        return item_helper(item)
    raise HTTPException(status_code=404, detail="Item not found")

# ✅ Delete
@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    result = await collection.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count == 1:
        return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
