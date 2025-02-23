from fastapi import APIRouter
from fastapi import Depends
from src.api.services.warehouse import WarehouseService


router = APIRouter(prefix="/warehouses")


@router.get("/{warehouse_id}/products/{product_id}", response_model={"quantity": int})
async def get_product_quantity(
    warehouse_id: str,
    product_id: str,
    service: WarehouseService = Depends(WarehouseService),
):
    return await service.get_product_quantity(warehouse_id, product_id)
