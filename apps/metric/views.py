from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from utils.providers.gmail.gmail import inbox_count
from apps.metric.utils import retrieve_timeseries_from_redis as get_from_redis
from utils.providers.amex.amex import get_balance as get_amex_balance
from utils.providers.sjd.sjd import HowappedReader
from utils.providers.goodreads.client import (
    Client as GrClient
)
# from utils.providers.strava.api import (
    # Client as Strava
# )
import datetime
import logging
logging.basicConfig(level=logging.INFO)

now = datetime.datetime.now()


def index(request):
    return HttpResponse('Hello')


def get(request):

    from utils.providers.pocket import pocket_client
    service_values = {
        'gmail': {'dt':'','value':0}
    }
    logging.info('Getting metrics ..')
    # todo. time this function
    # https://realpython.com/lessons/timing-functions-decorators/

    service_values['gmail']['dt'],service_values['gmail']['value'] = get_from_redis('gmail')

    return JsonResponse({
        'AIM HIGHER': {
            'PROFITS': HowappedReader().reported_profits,
            'BOOKS READ THIS YEAR': GrClient().books_on_shelf_count(f'read-{now.year}'),
            # 'MONTHLY KM CYCLED': Strava().monthly_km_cycled,
        },
        'AIM LOWER': {
            'GMAIL INBOX': service_values['gmail']['value'],
            'AMEX BALANCE': get_amex_balance(),
            'POCKET ARTICLES': pocket_client.article_count(),
        },
    })
