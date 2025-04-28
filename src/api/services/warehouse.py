from src.utils.service import BaseService
from src.utils.uow import transaction_mode


class WarehouseService(BaseService):
    base_repository = "warehouse"
    
    @transaction_mode
    async def get_product_quantity(self, warehouse_id: str, product_id: str):
        quantity = await self.uow.warehouse.get_quantity(warehouse_id, product_id)
        return {"quantity": quantity}
    
    @transaction_mode
    async def change_product_quantity(self, movement_message: dict):
        warehouse_id = movement_message["data"]["warehouse_id"]
        product_id = movement_message["data"]["product_id"]
        quantity = movement_message["data"]["quantity"]
        event = movement_message["event"]

        current_quantity = await self.uow.warehouse.get_quantity(
            warehouse_id, product_id
        )

        if current_quantity is None:
            if event == "arrival":
                await self.uow.warehouse.add_product(warehouse_id, product_id, quantity)
            else:
                raise ValueError(
                    f"Product with ID {product_id} does not exist in warehouse with ID {warehouse_id}"
                )
        else:
            change_amount = quantity if event == "arrival" else -quantity
            if event == "departure" and current_quantity < quantity:
                raise ValueError(
                    f"Insufficient quantity in warehouse: current quantity is {current_quantity}, requested quantity is {quantity}"
                )
            await self.uow.warehouse.change_quantity(
                warehouse_id, product_id, change_amount
            )