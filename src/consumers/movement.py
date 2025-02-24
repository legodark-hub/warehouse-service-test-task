from fastapi import Depends
from faststream.kafka.fastapi import KafkaRouter

from faststream.kafka.fastapi import Logger

from src.api.services.movement import MovementService
from src.api.services.warehouse import WarehouseService
from src.schemas.movement import MovementMessage
from src.utils.uow import transaction_mode

kafka_router = KafkaRouter("localhost:9092")

movement_data = {
    "id": "b3b53031-e83a-4654-87f5-b6b6fb09fd99",
    "source": "WH-3423",
    "specversion": "1.0",
    "type": "ru.retail.warehouses.movement",
    "datacontenttype": "application/json",
    "dataschema": "ru.retail.warehouses.movement.v1.0",
    "time": 1737439421623,
    "subject": "WH-3423:ARRIVAL",
    "destination": "ru.retail.warehouses",
    "data": {
        "movement_id": "c6290746-790e-43fa-8270-014dc90e02e0",
        "warehouse_id": "c1d70455-7e14-11e9-812a-70106f431230",
        "timestamp": "2025-02-18T14:34:56Z",
        "event": "arrival",
        "product_id": "4705204f-498f-4f96-b4ba-df17fb56bf55",
        "quantity": 100,
    },
}

@kafka_router.get("/")
async def hello_http():
    await kafka_router.broker.publish(movement_data, "movement")
    return "Hello, HTTP!"

@transaction_mode
@kafka_router.subscriber("movement")
async def movement_consumer(
    m: MovementMessage,
    logger: Logger,
    movement_service: MovementService = Depends(MovementService),
    warehouse_service: WarehouseService = Depends(WarehouseService),
):
    m = m.model_dump()
    await movement_service.save_movement_info(m)
    await warehouse_service.change_product_quantity(m)

