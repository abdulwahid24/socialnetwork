# Social Network Application
----------
This application is designed to accomplish the requirement given by TradeCore.

## Technologies Stack
- Python3.6
- Django2.+
- Django Rest Framework
- Swagger API Docs
- Postgres with HStore extention
- Docker + Compose
- Zappa + AWS Lambda

### Prerequisites
- Python3.6
- [Pipenv](https://pipenv.readthedocs.io/en/latest/)
- Docker & Docker Componse


### Setting up using Docker Compose

1. `cd socialnetwork`
2. `docker-compose up --build -d`
3. see `http://localhost:8000`

> Note: In case of an error related to **hstore** extension. You need to explicitly create the extension or you run the sql query `create extension hstore` in `python manage.py dbshell`.


### Running application on localhost
 1. Run `pipenv install && pipenv shell`
 2. `python manage.py runserver --settings SocialNetwork.settings.local_host`


> *Note: Live application is using a Heroku postgres instance which is located on US east region, That may cause a little bit slower response.*

> Please use your organization email to sign up as we are using **clearbit** which will only validate organization based email address.

*Please do let me know in case of any queries*

*Thanks*

*Abdulwahid Barguzar*

