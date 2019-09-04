
from django.core.management.base import BaseCommand
from  apps.metric.utils import capture_timeseries_to_redis


from utils.providers.gmail.gmail import inbox_count

import kronos


@kronos.register('* * * * *')
class Command(BaseCommand):

    SERVICES = {
        'gmail': inbox_count()
    }

    def handle(self, *args, **options):
        for svc, value in self.SERVICES.items():
            capture_timeseries_to_redis(svc, value)
