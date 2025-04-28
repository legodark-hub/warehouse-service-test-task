from fastapi import FastAPI

from faststream.kafka.fastapi import KafkaRouter

kafka_router = KafkaRouter("localhost:9092")

app = FastAPI()
app.include_router(kafka_router)
