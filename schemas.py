from pydantic import BaseModel


class ItemIn(BaseModel):
    name: str
    description: str | None = None


class Item(ItemIn):
    id: int


class ItemUpdate(BaseModel):
    id: int
    name: str | None = None
    description: str | None = None


class ItemId(BaseModel):
    id: int
