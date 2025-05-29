from redis_om import get_redis_connection

from config import config


REDIS_DB = get_redis_connection(
    host=config.HOST,
    port=config.PORT,
    decode_responses=True,
)