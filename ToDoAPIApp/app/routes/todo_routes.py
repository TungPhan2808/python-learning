from typing import Optional
from typing import Any
from bson import ObjectId
from fastapi import APIRouter, Depends, status, HTTPException, Query
from app.core.database import todos_collection
from app.schemas.todo_schema import ToDoResponse, ToDoCreate, ToDoUpdate
from app.utils.jwt_handler import get_current_user

router = APIRouter(prefix="/todos", tags=["ToDos"])

# Create a To-Do Item
@router.post(path="/", response_model=ToDoResponse)
async def create_todo(todo: ToDoCreate, user_email: str = Depends(get_current_user)):
    todo_dict = {
        "title": todo.title,
        "description": todo.description,
        "owner": user_email
    }

    result = await todos_collection.insert_one(todo_dict)
    todo_dict["id"] = str(result.inserted_id)
    return ToDoResponse(
        id=todo_dict["id"],
        title=todo_dict["title"],
        description=todo_dict["description"]
    )

# Update a To-Do Item
@router.put("/{todo_id}", response_model=ToDoResponse)
async def update_todo(
        todo_id: str,
        todo: ToDoUpdate,
        user_email: str = Depends(get_current_user)
):
    existing_todo = await todos_collection.find_one({"_id": ObjectId(todo_id)})
    if not existing_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo doesn't exist",
        )

    if existing_todo["owner"] != user_email:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden"
        )

    update_data = {k: v for k,v in todo.model_dump().items() if v is not None}
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No data to update",
        )

    await todos_collection.update_one(
        {"_id": ObjectId(todo_id)},
        {"$set": update_data}
    )

    updated_todo = await todos_collection.find_one({"_id": ObjectId(todo_id)})

    return ToDoResponse(
        id=str(updated_todo["_id"]),
        title=updated_todo["title"],
        description=updated_todo["description"],
        completed = updated_todo["completed"]
    )

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: str, user_email: str = Depends(get_current_user)):
    existing_todo = await todos_collection.find_one({"_id": ObjectId(todo_id)})
    if not existing_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo doesn't exist",
        )

    if existing_todo["owner"] != user_email:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden"
        )

    await todos_collection.delete_one({"_id": ObjectId(todo_id)})

@router.get("")
async def get_todos(
        page: int = Query(1, ge=1),
        limit: int = Query(10, ge=1),
        completed: Optional[bool] = Query(None),
        search: Optional[str] = Query(None, description="Search by title or description"),
        sort_order: str = Query("desc", regex="^(asc|desc)$"),
        user_email: str = Depends(get_current_user),
):
    query: dict[str, Any] = {"owner": user_email}

    # Filter
    if completed is not None:
        query["completed"] = completed

    # Search
    if search:
        query["$or"] = [
            {"title": {"$regex": search, "$options": "i"}},
            {"description": {"$regex": search, "$options": "i"}},
        ]

    # Sort
    sort_direction = -1 if sort_order == "desc" else 1

    skip = (page - 1) * limit
    total = await todos_collection.count_documents({})
    cursor = (todos_collection
              .find(query)
              .sort("_id", sort_direction)
              .skip(skip)
              .limit(limit))

    todos = []
    async for item in cursor:
        todos.append({
            "id": str(item["_id"]),
            "title": item["title"],
            "description": item["description"],
        })

    return {
        "data": todos,
        "page": page,
        "limit": limit,
        "total": total
    }

@router.get("/{todo_id}", response_model=ToDoResponse)
async def get_todo(
        todo_id: str,
        user_email: str = Depends(get_current_user),
):
    existing_todo = await todos_collection.find_one({"_id": ObjectId(todo_id)})
    if not existing_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo doesn't exist",
        )

    if existing_todo["owner"] != user_email:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden"
        )

    return ToDoResponse(
        id=str(existing_todo["_id"]),
        title=existing_todo["title"],
        description=existing_todo["description"]
    )