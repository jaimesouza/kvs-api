# Key-Value Store API

Simple REST API for a key-value store using Python FastAPI framework.


## Installation

The app can be installed using one the follwing options:

Option 1:

`git clone https://github.com/jaimesouza/kvs-api.git`

`cd kvs-api`

`pip install -e .`

Option 2:

`pip install git+https://github.com/jaimesouza/kvs-api.git`

## Tests

Make sure that the tests pass by running:

`pytest`

## Execution

After install the app, run it with:

`unicorn kvs:app --reload`

And access it on the browser:

`http://localhost:8000/docs`

## API

- GET `/`
  - return a JSON blob
  - app-author and app-name info are returned in the response headers

- GET `/api/pairs`
  - return all key-value pairs in KVS

- GET `/api/pairs/{key}`
  - return a key-value pair with the sent key
  - the result is also returned in the response headers

- POST `/api/pairs`
  - insert a new key-value pair in KVS

- PUT `/api/pairs/{key}`
  - update the value of a key-value pair with the sent key

- DELETE `/api/pairs/{key}`
  - delete a key-value pair with the sent key

## CI/CD

Github actions workflows run:

- Flake8 and Pytest (.github/workflows/test_ci.yml) on push and pull_request events.
- Build docker image and push it to dockerhub (.github/workflows/docker-build.yml) on release event.

## Try Online

The API was deployed on a Kubernetes cluster and it's available on:

`http://144.22.204.27/docs`
