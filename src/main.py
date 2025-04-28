from fastapi import FastAPI
from faststream.kafka.fastapi import KafkaRouter
from src.api.routers.movement import router as movement_router
from src.api.routers.warehouse import router as warehouse_router
from src.consumers.movement import kafka_router as consumer_router

app = FastAPI()

app.include_router(consumer_router)
app.include_router(movement_router)
app.include_router(warehouse_router)
