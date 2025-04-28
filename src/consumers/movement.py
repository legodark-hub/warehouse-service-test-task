from fastapi import Depends
from faststream.kafka.fastapi import Logger

from src.api.services.movement import MovementService
from src.main import kafka_router
from src.schemas.movement import MovementMessage

@kafka_router.subscriber("response")
async def hello_response(
    m: MovementMessage,
    logger: Logger,
    service: MovementService = Depends(MovementService),
):
    logger.info(m)
    await service.save_movement_info(m)
    

    
    
