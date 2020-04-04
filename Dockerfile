FROM python:3.7-alpine3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apk update
RUN apk add make automake libressl-dev libffi-dev gcc g++ python3-dev subversion libxml2-dev libxslt-dev curl
RUN pip3 install --upgrade pip
ADD requirements.txt /code/
# RUN pip install Cython numpy 
# pyzmq==17.0.0

COPY wait-for-it.sh /usr/wait-for-it.sh
RUN chmod +x /usr/wait-for-it.sh

RUN pip install -r requirements.txt
ADD ./ /code/

# ENTRYPOINT [ "/bin/sh", "-c" ]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]

# CMD ["/bin/sh", "/usr/wait-for-it.sh" , "redis:6379" , "--strict" , "--timeout=300" , "--" , "./manage.py runserver 0.0.0.0:8001"]

    # command: CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
# command:bash -c "/usr/wait-for-it.sh --timeout=0 mongo:27017 && npm run dev"

