FROM python:3.6.5

RUN apt-get update
RUN apt-get -y install mysql-client

RUN pip install Flask PyMySQL

RUN mkdir /myapp
WORKDIR /myapp/

CMD python hello.py
