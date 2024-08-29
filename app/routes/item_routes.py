from fastapi import APIRouter
from typing import Optional

router = APIRouter()

@router.get("/{item_id}")
def read_item(item_id: int, name: Optional[str] = None, detail: Optional[bool] = False):
    response = {"item_id": item_id}
    if name:
        response["name"] = name
    if detail:
        response["detail"] = "This is a detailed description of the item."
    return response

class ItemManager:
    def __init__(self, name: str, description: str = None):
        self.name = name
        self.description = description

    def to_dict(self):
        return {"name": self.name, "description": self.description}

@router.post("/")
def create_item(name: str, description: Optional[str] = None):
    item = ItemManager(name=name, description=description)
    return item.to_dict()
