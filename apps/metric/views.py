from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from utils.providers.gmail.gmail import inbox_count
from utils.providers.amex.amex import get_balance as get_amex_balance
from utils.providers.sjd.sjd import HowappedReader
from utils.providers.pocket import pocket_client
from utils.providers.goodreads.client import (
    Client as GrClient
)
# from utils.providers.strava.api import (
    # Client as Strava
# )
import datetime

now = datetime.datetime.now()
def index(request):
    return HttpResponse('Hello')

def get(request):

    return JsonResponse({
        'AIM HIGHER': {
            'PROFITS': HowappedReader().reported_profits,
            'BOOKS READ THIS YEAR': GrClient().books_on_shelf_count(f'read-{now.year}'),
            # 'MONTHLY KM CYCLED': Strava().monthly_km_cycled,
        },
        'AIM LOWER': {
            'GMAIL INBOX': inbox_count(),
            'AMEX BALANCE': get_amex_balance(),
            'POCKET ARTICLES': pocket_client.article_count(),
        },
    })
