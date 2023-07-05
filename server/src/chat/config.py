from redis_om import get_redis_connection


# redis_db = get_redis_connection(
#     host='redis://redis:6379',
#     port='6379',
#     decode_responses=True
# )

redis_db = get_redis_connection(
    host="redis:redis:6379",
    port=6379,
    decode_responses=True
)