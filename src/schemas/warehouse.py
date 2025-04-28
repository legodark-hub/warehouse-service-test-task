from pydantic import BaseModel

class WarehouseBase(BaseModel):
    warehouse_id: str
    product_id: str
    quantity: int

class WarehouseDB(WarehouseBase):
    id: int

    class Config:
        from_attributes = True
