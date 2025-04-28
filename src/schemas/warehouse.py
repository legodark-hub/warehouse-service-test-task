from pydantic import BaseModel

from src.schemas.response import BaseResponse

class WarehouseBase(BaseModel):
    warehouse_id: str
    product_id: str
    
    
class WarehouseProductQuantity(BaseModel):
    quantity: int

class WarehouseDB(WarehouseBase, WarehouseProductQuantity):
    id: int

    class Config:
        from_attributes = True
        
class WarehouseResponse(BaseResponse):
    payload: WarehouseBase
    
class WarehouseQuantityResponse(BaseResponse):
    payload: WarehouseProductQuantity
    
