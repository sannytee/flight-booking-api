![Build Status](https://travis-ci.com/SannyTee/flight-booking-api.svg?branch=develop)
[![Coverage Status](https://coveralls.io/repos/github/SannyTee/flight-booking-api/badge.svg)](https://coveralls.io/github/SannyTee/flight-booking-api)
# Flight-Booking API - An amazing project
The flight-booking API allows user to perform basic flight booking operations.

## Technologies

* Django
* Django Rest Framework


## API Endpoints
The following are the endpoints currently available on the application
* Sign up: POST /api/v1/auth/signup/
* Log in: POST /api/v1/auth/login/
* Book Flight: POST /api/v1/flights/
* Get Passengers for a particular flight and date: GET /api/v1/flights?name={flight_name}&date={flight_datetime}

## Installation
Clone the repo
```bash
$ git clone https://github.com/SannyTee/flight-booking-api.git
```

Navigate to the project directory
```bash
$ cd flight-booking-api
```

Create a virtual environment by running

```bash
$ python venv {name of virtual folder}
```

The above command will create a virtual environment but it needs to be activated. To activate the virtual environment, run the command
```bash
source {name of virtual folder}/bin/activate
```

Install the required dependencies
```bash
$ pip install -r requirements.txt
```

create an env file that matches the content of the env.sample file

Run the Migration
```bash
$ python manage.py migrate
```

Install Redis and run the redis server

run the application
```bash
$ python manage.py runserver
```

with Django App and Redis running, run the following command in the project directory for asynchronous job with celery
```bash
$ celery -A flightbackend worker -l info
$ celery -A flightbackend beat -l info
```


## Testing
```bash
$ python manage.py test
```
To run the test with an html report, run this command
```bash
$ python manage.py test --cover-html
```
