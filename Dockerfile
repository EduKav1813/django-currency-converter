FROM python:3.12-slim

# Setting resource quota
ARG MIN_MEM=2G
ARG MAX_MEM=2G

COPY ./currencyconverter ./currencyconverter
COPY pyproject.toml .
COPY poetry.lock .
COPY README.md .

RUN pip install poetry
RUN poetry install
EXPOSE 8000

#Execution
CMD poetry run ./currencyconverter/manage.py runserver
