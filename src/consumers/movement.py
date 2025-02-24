from fastapi import Depends
from faststream.kafka.fastapi import Logger

from src.api.services.movement import MovementService
from src.api.services.warehouse import WarehouseService
from src.main import kafka_router
from src.schemas.movement import MovementMessage


@kafka_router.subscriber("response")
async def hello_response(
    m: MovementMessage,
    logger: Logger,
    movement_service: MovementService = Depends(MovementService),
    warehouse_service: WarehouseService = Depends(WarehouseService),
):
    logger.info("Message received")
    try:
        await movement_service.save_movement_info(m)
        await warehouse_service.change_product_quantity(m)
        logger.info("Message processed")
    except Exception as e:
        logger.error(f"Error processing message: {e}")
