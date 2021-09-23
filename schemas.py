from pydantic import BaseModel
from datetime import date


class csvCreate(BaseModel):
    start_date: date
    end_date: date
    min_price: float
    max_price: float
    name: str


class product:
    def __init__(self, min: int, max: int, start: date, end: date, name: str, change: float):
        self.min = min
        self.max = max
        self.start = start
        self.end = end
        self.name = name
        self.change = change
