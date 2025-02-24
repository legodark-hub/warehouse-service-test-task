from datetime import datetime
from src.utils.service import BaseService
from src.utils.uow import transaction_mode
from fastapi import HTTPException, status


class MovementService(BaseService):
    base_repository = "movement"

    @transaction_mode
    async def get_movement_info(self, movement_id: str):
        departure_movement = await self.uow.movement.get_movement(
            movement_id, "departure"
        )
        arrival_movement = await self.uow.movement.get_movement(
            movement_id, "arrival"
        )

        if not departure_movement and not arrival_movement:
            return {}

        def get_value_or_none(obj, attr):
            return getattr(obj, attr, None) if obj else None

        movement_info = {
            "movement_id": movement_id,
            "departure_from": get_value_or_none(departure_movement, "source"),
            "arrival_at": get_value_or_none(arrival_movement, "source"),
            "departure_time": str(
                get_value_or_none(departure_movement, "timestamp")
            ),
            "arrival_time": str(get_value_or_none(arrival_movement, "timestamp")),
            "duration": str(
                get_value_or_none(arrival_movement, "timestamp")
                - get_value_or_none(departure_movement, "timestamp")
            )
            if departure_movement and arrival_movement
            else None,
            "quantity_difference": get_value_or_none(arrival_movement, "quantity")
            - get_value_or_none(departure_movement, "quantity")
            if departure_movement and arrival_movement
            else None,
        }

        return movement_info
        
    @transaction_mode
    async def save_movement_info(self, movement_message: dict):
        existing_movement = await self.uow.movement.get_movement(
            movement_message["data"]["movement_id"], movement_message["data"]["event"]
        )
        if existing_movement:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Movement with given ID and event already exists.",
            )

        movement_data = {
            "movement_id": movement_message["data"]["movement_id"],
            "event": movement_message["data"]["event"],
            "source": movement_message["source"],
            "warehouse_id": movement_message["data"]["warehouse_id"],
            "timestamp": movement_message["data"]["timestamp"],
            "product_id": movement_message["data"]["product_id"],
            "quantity": movement_message["data"]["quantity"],
        }
        movement = await self.uow.movement.add_movement(movement_data)
        return movement
    
    