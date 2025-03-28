# Summary

Simple web application to convert currencies.

## Run with Docker Compose

1. Start the web service

```bash
docker compose --profile web up
```

2. Set your ExchangeRate-API key in `.env`

```env
EXCHANGE_RATE_API_KEY=your_key
```

3. Start parser services

```bash
docker compose --profile parser up
```

(Optional) Start MOCK parser for testing purposes

```bash
docker compose --profile mock_parser up
```

If running locally, this will start:

- Backend on port :8000
- Frontend on port :8001
- Postgres database on port :5432
- Redis (for celery) on port :6379

## Run tests

```sh
./currencyconverter/manage.py test currencyconverter.tests
```
