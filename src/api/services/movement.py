from datetime import timedelta
from src.utils.service import BaseService
from src.utils.uow import transaction_mode


class MovementService(BaseService):
    base_repository = "movement"

    @transaction_mode
    async def get_movement_info(self, movement_id: str):
        async with self.uow:
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
                    timedelta(
                        seconds=(
                            get_value_or_none(arrival_movement, "timestamp")
                            - get_value_or_none(departure_movement, "timestamp")
                        ).total_seconds()
                    )
                )
                if departure_movement and arrival_movement
                else None,
                "quantity_difference": get_value_or_none(arrival_movement, "quantity")
                - get_value_or_none(departure_movement, "quantity")
                if departure_movement and arrival_movement
                else None,
            }

            return movement_info
