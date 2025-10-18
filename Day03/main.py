from fastapi import FastAPI
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client["todos"]
collection = db["todos"]

@app.post("/todos")
def add_todo(todo: dict):
    result = collection.insert_one(todo)
    return {"_id": str(result.inserted_id), "message": "Todo added successfully"}

@app.get("/todos")
def read_todos():
    todos = list(collection.find())
    for s in todos:
        s["_id"] = str(s["_id"])
    return todos

@app.get("/todos/{todo_id}")
def read_todo(todo_id: str):
    todo = collection.find_one({"_id": ObjectId(todo_id)})
    if not todo:
        return {"message": "Todo not found"}
    todo["_id"] = str(todo["_id"])
    return todo

