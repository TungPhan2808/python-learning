from typing import Optional
from pydantic import BaseModel, Field


class ToDoCreate(BaseModel):
    title: str
    description: str

class ToDoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class ToDoResponse(BaseModel):
    id: str
    title: str
    description: str
    completed: bool = Field(default=False)