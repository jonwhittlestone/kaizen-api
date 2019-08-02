"""
user info (31716765,):
    http get "https://www.strava.com/api/v3/athlete" "Authorization: Bearer 260faa36531f147a9c03e90dfe4803d3a4e41028"

athelete stats:
    http get "https://www.strava.com/api/v3/athletes/31716765/stats" "Authorization: Bearer 260faa36531f147a9c03e90dfe4803d3a4e41028"

get activities between (start of June =1559347200, end = 1561939199 )

    http get "https://www.strava.com/api/v3/athlete/activities?before=1561939199&after=1559347200&page=&per_page=" "Authorization: Bearer 260faa36531f147a9c03e90dfe4803d3a4e41028"
    #print(arrow.utcnow().ceil('month').timestamp)

"""
from stravalib.client import Client
client = Client()