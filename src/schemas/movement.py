from pydantic import BaseModel
from datetime import datetime

from src.schemas.response import BaseResponse

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
        
class MovementInfo(MovementBase):
    movement_id: str
    departure_from: str | None = None
    arrival_at: str | None = None
    departure_time: str | None = None
    arrival_time: str | None = None
    duration: str | None = None
    quantity_difference: int | None = None
    
class MovementMessageData(BaseModel):
    movement_id: str
    warehouse_id: str
    timestamp: str
    event: str
    product_id: str
    quantity: int


class MovementMessage(BaseModel):
    id: str
    source: str
    specversion: str
    type: str
    datacontenttype: str
    dataschema: str
    time: int
    subject: str
    destination: str
    data: MovementMessageData
    
class MovementInfoResponse(BaseResponse):
    payload: MovementInfo