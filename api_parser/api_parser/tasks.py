import os

import requests
from celery import shared_task
from django.db import transaction

from .models import CurrencyToUSD


@shared_task
def update_exchange_rates():
    print("[ExchangeRate-API] Updating exchange rates...")
    EXCHANGE_RATE_API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")

    if not EXCHANGE_RATE_API_KEY:
        print("[ERROR] EXCHANGE_RATE_API_KEY is not set")

    URL = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}/latest/USD"
    response = requests.get(URL)
    data = response.json()
    conversion_rates = data["conversion_rates"]

    print(dict(conversion_rates))

    with transaction.atomic():
        for key, value in conversion_rates.items():
            CurrencyToUSD.objects.update_or_create(
                currency_code=key, defaults={"price": 1 / value}
            )

    print("Exchange rates updated.")
