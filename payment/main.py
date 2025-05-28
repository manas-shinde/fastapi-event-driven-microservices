from fastapi import FastAPI

from src.route import order_route


version = 'v1'

app = FastAPI(
    title="FastAPI microservice - PAYMENT",
    description="A FastAPI-based microservices architecture using Redis for data and stream-based messaging between services. ",
    version=version,
)


app.include_router(
    order_route, prefix=f"/api/{version}/orders", tags=['orders'])
