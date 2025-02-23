from src.utils.service import BaseService
from src.utils.uow import transaction_mode


class WarehouseService(BaseService):
    base_repository = "warehouse"
    
    @transaction_mode
    async def get_product_quantity(self, warehouse_id: str, product_id: str) -> int:
        quantity = await self.uow.warehouse.get_quantity(warehouse_id, product_id)
        return quantity