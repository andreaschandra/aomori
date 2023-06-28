# Aomori

A pet project for deploying machine learning API using FastAPI and GCP Stack.

The struture of the project and its configuration is forked from [here](https://github.com/eightBEC/fastapi-ml-skeleton)

## Installation
Install the required packages in your local environment (ideally virtualenv, conda, etc.).
```bash
pip install -r requirements
``` 

## Run It

1. Start your  app with: 
```bash
uvicorn aomori.main:app
```

2. Go to [http://localhost:8000/docs](http://localhost:8000/docs).
   
3. Click `Authorize` and enter the API key as stated in the .env.

## Run Tests

If you're not using `tox`, please install with:
```bash
pip install tox
```

Run your tests with: 
```bash
tox
```

This runs tests and coverage for Python 3.6 and Flake8, Autopep8, Bandit.
