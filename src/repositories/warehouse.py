from src.models.warehouse import Warehouse
from src.utils.repository import SQLAlchemyRepository
from sqlalchemy import update
from sqlalchemy.future import select


class WarehouseRepository(SQLAlchemyRepository):
    model = Warehouse

    async def add_product(self, warehouse_id: str, product_id: str, quantity: int) -> None:
        new_product = Warehouse(
            warehouse_id=warehouse_id,
            product_id=product_id,
            quantity=quantity,
        )
        self.session.add(new_product)
        await self.session.commit()

    async def change_quantity(
        self, warehouse_id: str, product_id: str, amount: int
    ) -> None:
        query = (
            update(Warehouse)
            .where(
                Warehouse.warehouse_id == warehouse_id,
                Warehouse.product_id == product_id,
            )
            .values(quantity=Warehouse.quantity + amount)
        )
        await self.session.execute(query)
        await self.session.commit()

    async def get_quantity(self, warehouse_id: str, product_id: str) -> int:
        query = select(Warehouse.quantity).where(
            Warehouse.warehouse_id == warehouse_id, Warehouse.product_id == product_id
        )
        result = await self.session.execute(query)
        quantity = result.scalar_one_or_none()
        return quantity if quantity is not None else 0
