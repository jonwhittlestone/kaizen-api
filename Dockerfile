FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apk update
RUN apk add make automake gcc g++ python3-dev subversion libxml2-dev libxslt-dev

# RUN pip3 install --upgrade pip
ADD requirements.txt /code/
RUN pip install Cython numpy 
# pyzmq==17.0.0
RUN pip install -r requirements.txt
ADD ./ /code/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]

