from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    description: Optional[str] = None

class User(BaseModel):
    username: str
    email: str
    age: int
