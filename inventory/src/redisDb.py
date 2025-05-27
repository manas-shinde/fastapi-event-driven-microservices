from redis_om import get_redis_connection

from config import config


redis_db = get_redis_connection(
    host=config.HOST,
    port=config.PORT,
    decode_responses=True,
    password=config.PASSWORD,
)
