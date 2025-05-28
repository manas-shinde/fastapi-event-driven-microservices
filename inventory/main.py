from fastapi import FastAPI
from src.route import product_route


version = 'v1'

app = FastAPI(
    title="FastAPI microservice - INVENTORY",
    description="A FastAPI-based microservices architecture using Redis for data and stream-based messaging between services. ",
    version=version,
)

app.include_router(
    product_route, prefix=f"/api/{version}/products", tags=['products'])
