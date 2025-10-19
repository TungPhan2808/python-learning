from pydantic import BaseModel, EmailStr

class Todo(BaseModel):
    title: str
    description: str
    status: bool
    owner: EmailStr