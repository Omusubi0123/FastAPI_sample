from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None

class User(BaseModel):
    username: str
    email: str
    age: int
