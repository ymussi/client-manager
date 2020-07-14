## Description

This is a simple API that manages customers, products and list of favorite products of each customer.

This API is implemented in production on an EC2 and its database on an RDS on the AWS.

You can access it through the link: http://52.67.150.239:17040/docs

## Projects Resources

- Languege: Python 3.6
- Package manager: pip
- Main dependencies: [_Flask 1.0.2_](https://flask.palletsprojects.com/en/1.1.x/), [_Flask-Restplus 0.13.0_](https://flask-restplus.readthedocs.io/en/stable/), [_SQLAlchemy 1.3.8_](https://docs.sqlalchemy.org/en/13/orm/tutorial.html), [_Alembic 1.2.1_](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
- DB: [_MySQL 5.7_](https://dev.mysql.com/doc/refman/5.7/en/)

## Installation

First of all, clone this project in your work environment.

`$ git clone https://github.com/ymussi/client-manager.git`

and after that choice your runing method:

## Running local

```bash
$ pip install -r requirements.txt
$ python setup.py develop
$ cd wishlist/
$ python run.py
```

The API Doc can be accessed at: http://localhost:5000/docs

## Running with docker container

Using the docker compose, the web services and database, will be configured and started automatically in the container through the following command line:

`$ docker-compose up`

The API Doc can be accessed at: http://localhost:8000/docs

## Database Server

The database server will be exposed externally on:

- host: localhost
- username: client
- password: client
- port: 23307
- database: client_manager


## Runing migrations

```bash
$ cd wishlist/
$ alembic upgrade head
```

## Testes

```bash
$ cd ..
$ FLASK_ENV=development python -m unittest -v
```

## Working

To register user

- Send a POST request to endpoint: **/register** with this payload:

```javascript
{
    "username": "Teste",
    "email": "teste@teste.com",
    "password": "teste1234"
}
```

To login

- Send a POST request to endpoint **/register/login** with this payload:

```javascript
{
    "email": "teste@teste.com",
    "password": "teste1234"
}
```

You will receive an authorization token.

- All endpoints require an authorization token.

## Logs
Records in the database can be tracked through the metabase dashboard on this link:

- http://52.67.150.239:17030/public/dashboard/639bf2fc-1458-402a-94b8-78ba5db5b8fc


Copyright (c) [2020] [Yuri Mussi]