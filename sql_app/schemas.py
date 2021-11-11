from typing import List, Optional

from pydantic import BaseModel


class ItemEntry(BaseModel):
    item_name: str
    date: str
    price: float


class Item(BaseModel):
    id: int
    item_name: str
    date: str
    price: float

    class Config:
        orm_mode = True
