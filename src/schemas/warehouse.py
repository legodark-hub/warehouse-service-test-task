from pydantic import BaseModel

from src.schemas.response import BaseResponse

class WarehouseBase(BaseModel):
    warehouse_id: str
    product_id: str
    quantity: int

class WarehouseDB(WarehouseBase):
    id: int

    class Config:
        from_attributes = True
        
class WarehouseResponse(BaseResponse):
    payload: WarehouseBase