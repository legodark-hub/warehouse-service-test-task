from sqlalchemy import select
from src.models.movement import Movement
from src.utils.repository import SQLAlchemyRepository


class MovementRepository(SQLAlchemyRepository):
    model = Movement

    async def add_movement(self, movement_data):
        movement = self.model(**movement_data)
        self.session.add(movement)
        await self.session.commit()
        await self.session.refresh(movement)
        return movement

    async def get_movement(self, movement_id, event):
        result = await self.session.execute(
            select(self.model).where(
                self.model.movement_id == movement_id, self.model.event == event
            )
        )
        return result.scalar_one_or_none()
