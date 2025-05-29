from fastapi import FastAPI
from src.route import analytics_routes


version = 'v1'

app = FastAPI(
    title="FastAPI microservice - Analytics",
    description="A FastAPI-based microservices architecture using Redis for data and stream-based messaging between services. ",
    version=version,
)

app.include_router(
    analytics_routes, prefix=f"/api/{version}/analytics", tags=['analytics'])
