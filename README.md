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

- Start backend on port 8000:

    ```sh
    ./backend/manage.py runserver 127.0.0.1:8080
    ```

- Start frontend on port 8001:

    ```sh
    ./frontend/manage.py runserver 127.0.0.1:8001
    ```

## Run tests

```sh
./currencyconverter/manage.py test currencyconverter.tests
```
