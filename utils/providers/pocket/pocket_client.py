from pocket import Pocket, PocketException
from django.conf import settings

def article_count():

    creds = settings.PROVIDER_CREDS
    p = Pocket(
        consumer_key=creds['pocket']['consumer'],
        access_token=creds['pocket']['access']
    )
    try:
        return len(
            p.retrieve(offset=0)['list']
        )
    except PocketException as e:
	    print(e.message)

article_count()
