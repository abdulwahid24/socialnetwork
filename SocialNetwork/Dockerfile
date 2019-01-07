FROM python:3.6

RUN pip3 install pipenv
RUN mkdir /SocialNetwork

COPY . /SocialNetwork
WORKDIR /SocialNetwork

RUN  pipenv install --deploy --system
RUN pip3 install git+https://github.com/abdulwahid24/django-hstore
RUN pip3 install fullcontact.py
