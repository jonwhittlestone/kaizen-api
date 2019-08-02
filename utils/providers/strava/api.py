"""
user info (31716765,):
    http get "https://www.strava.com/api/v3/athlete" "Authorization: Bearer 260faa36531f147a9c03e90dfe4803d3a4e41028"

athelete stats:
    http get "https://www.strava.com/api/v3/athletes/31716765/stats" "Authorization: Bearer 260faa36531f147a9c03e90dfe4803d3a4e41028"

get activities between (start of June =1559347200, end = 1561939199 )

    http get "https://www.strava.com/api/v3/athlete/activities?before=1561939199&after=1559347200&page=&per_page=" "Authorization: Bearer 260faa36531f147a9c03e90dfe4803d3a4e41028"
    #print(arrow.utcnow().ceil('month').timestamp)

"""
from stravaio import StravaIO
from django.conf import settings


class Client:

    def __init__(self):
        '''See library for use: https://github.com/sladkovm/stravaio'''
        creds = settings.PROVIDER_CREDS

        access_token = creds.get('strava', {}).get('access_token')
        self.client = StravaIO(access_token=access_token)
        # strava_oauth2(client_id=STRAVA_CLIENT_ID, client_secret=STRAVA_CLIENT_SECRET)

    @property
    def monthly_km_cycled(self):
        # list_activities = self.client.get_logged_in_athlete_activities(after='last month')
        return '54.5'

    def oauth_flow(self):
        '''
            From: http://developers.strava.com/docs/getting-started/

            1. Go to https://www.strava.com/settings/api and copy your Client ID
            2. Paste your Client ID into this URL: 
                http://www.strava.com/oauth/authorize?client_id=[REPLACE_WITH_YOUR_CLIENT_ID]&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read
            3. Go to a browser
            4. Paste the URL you edited into the browser window (step 1 and 2 from the graph)
            5. Hit enter
            6. When you see the authorization page, click “Authorize” (step 3a from the graph) 
        '''