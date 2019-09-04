import arrow
import redis
from redis.exceptions import (ResponseError as RedisResponseError)
import logging
from django.conf import settings
logging.basicConfig(level=logging.INFO)

redis_obj = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT,
                        password=settings.REDIS_PASSWORD, db=settings.REDIS_DB)


def capture_timeseries_to_redis(metric, value):
    try:
        key = f'ts:metric-{metric}'
        ts = arrow.utcnow().timestamp
        redis_obj.execute_command("ts.add", key, ts, value)
        logging.info(f'Captured {metric} value ({value}) to redis')
    except redis.ConnectionError as e:
        logging.info(f'Redis could not be accessed at {host}:{port}')


def retrieve_timeseries_from_redis(metric, test_redis=None):
    '''
    Gets the most recent timeseries value from Redis for the given metric`:w
    '''
    # if test_redis:
    #     redis_obj = test_redis

    key = f'ts:metric-{metric}'
    values = redis_obj.execute_command(
        "TS.RANGE",
        key,
        arrow.utcnow().shift(hours=-1).timestamp,
        arrow.utcnow().timestamp,
        "AGGREGATION",
        "last",
        (3600))

    return fmt_stored_timeseries_value(values[0])


def fmt_stored_timeseries_value(val: list) -> dict:
    return arrow.get(val[0]), float(val[1].decode())
