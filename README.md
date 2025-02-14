# Summary

Simple web application to convert currencies.

## How to install locally

1. Create virtual environemnt (Python >=3.12)

```sh
python -m venv .venv
```

2. Activate the environment

```sh
source .venv/bin/activate
```

3. Install poetry

```sh
pip install poetry
```

4. Install dependencies with poetry

```sh
poetry install
```

## Start web server

```sh
./currencyconverter/manage.py runserver
```

## Run tests

```sh
./currencyconverter/manage.py test currencyconverter.tests
```