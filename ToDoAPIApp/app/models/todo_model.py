from pydantic import BaseModel, EmailStr

class Todo(BaseModel):
    title: str
    description: str
    completed: bool
    owner: EmailStr