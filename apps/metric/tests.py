import redis
import arrow
from django.test import TestCase
from django.conf import settings
from  apps.metric.utils import retrieve_timeseries_from_redis


class MetricTests(TestCase):
    def setUp(self):
        '''Put some dummy data in Redis'''

        TEST_DB = 2

        self.SAMPLE_SERVICE = 'servicename'
        self.SAMPLE_KEY = f'ts:metric-{self.SAMPLE_SERVICE}'
        self.SAMPLE_VALUE = 100.00

        self.redis_obj = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT,
                                password=settings.REDIS_PASSWORD, db=TEST_DB)

        self.redis_obj.execute_command(
            "ts.add", self.SAMPLE_KEY, arrow.utcnow().timestamp, self.SAMPLE_VALUE)

    def tearDown(self):
        '''Clear the test Redis db'''
        self.redis_obj.flushdb()

    def test_retrieve_timeseries_from_redis(self):
        datetime, metric_val = retrieve_timeseries_from_redis(
            self.SAMPLE_SERVICE, self.redis_obj)

        self.assertTrue(metric_val == self.SAMPLE_VALUE)

