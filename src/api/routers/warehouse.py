from fastapi import APIRouter
from fastapi import Depends
from src.schemas.warehouse import WarehouseQuantityResponse
from src.api.services.warehouse import WarehouseService


router = APIRouter(prefix="/warehouses")


@router.get(
    "/{warehouse_id}/products/{product_id}", response_model=WarehouseQuantityResponse
)
async def get_product_quantity(
    warehouse_id: str,
    product_id: str,
    service: WarehouseService = Depends(WarehouseService),
):
    quantity = await service.get_product_quantity(warehouse_id, product_id)
    return WarehouseQuantityResponse(payload=quantity)
