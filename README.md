# Kaizen Server - A Personal Dashboard

In a world where we are always striving to do better, and to *continously improve*, this server provides you with current metrics. 

## Quickstart

1. To run in a Python 3 Virtual Env:

    $ pip install -r requirements.txt; ./manage.py runserver;
    $ curl http://127.0.0.1:8000/ | jq

2. Run a Redis docker container with the Redis Timeseries module. (See separate section for example command) 

3. To install the cron job with django-kronos, run:

    `./manage.py installtasks`

.. and then peek in `./debug.log`

## Example output

![Example API Hit](screenshot.png)

Natrually, this app continues to improve.

## Redis Timeseries
An example of analysing of timeseries data can be found by running this notebook.

    jupyter notebook utils/providers/strava/Monthly\ Kilometers\ Cycled\ timeseries\ exampe.ipynb

You'll need to have Redis with the Timeseries module accessible at localhost. Using docker, you can do:

    docker run \
    -p 6379:6379 \           
    -v /home/jon/docker-data:/data \
    -d redislabs/redismod \
    -- loadmodule /usr/lib/redis/modules/redistimeseries.so \
    -- dir /data \
    -- dbfilename dump.rdb


## Next Steps ..

[ ] For each metric, write script that obtains the metric from the 3rd party and writes a new row to a csv in {metric}/data/{year}.csv

[ ] Have the view retrieve the most recent row of the csv in json response

[ ] Schedule `get_metric()` to repeat every 5 seconds / 1 minute with celery

[ ] Dockerize celery

[ ] Check output file named with year exists, if not create it

[ ] have a Jupyter notebook generate the chart from existing data for each metric

[ ] A frontend android widget displaying a nuxt generated static site with refresh button to update data from server: https://tinyurl.com/y6qt52sp

[ ] New metric: github contributions this week

[ ] New metric: KM Cycled this month




