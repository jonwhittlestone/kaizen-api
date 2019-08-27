# Kaizen Server - A Personal Dashboard

In a world where we are always striving to do better, and to *continously improve*, this server provides you with current metrics. 

To run in a Python 3 Virtual Env:

    $ pip install -r requirements.txt; ./manage.py runserver;
    $ curl http://127.0.0.1:8000/ | jq


![Example API Hit](screenshot.png)

Natrually, this app continues to improve.

## Redis Timeseries
An example of analysing of timeseries data can be found in the following note$book.

You'll need to have Redis with the Timeseries module accessible at localhost. Using docker, you can do:

    docker run \
    -p 6379:6379 \           
    -v /home/jon/docker-data:/data \
    -d redislabs/redismod \
    -- loadmodule /usr/lib/redis/modules/redistimeseries.so \
    -- dir /data \
    -- dbfilename dump.rdb



