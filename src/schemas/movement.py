from pydantic import BaseModel
from datetime import datetime

class MovementBase(BaseModel):
    movement_id: str
    event: str
    source: str
    warehouse_id: str
    timestamp: datetime
    product_id: str
    quantity: int

class MovementDB(MovementBase):
    id: int

    class Config:
        from_attributes = True