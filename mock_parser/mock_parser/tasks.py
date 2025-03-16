from pprint import pprint
from random import uniform

from celery import shared_task
from django.db import transaction

from .models import CurrencyToUSD


@shared_task
def update_exchange_rates():
    print("Updating exchange rates...")
    data = {}
    data["USD"] = 1.0
    data["EUR"] = round(uniform(0.5, 2.5), 2)

    print("Data:")
    pprint(data)

    with transaction.atomic():
        for key, value in data.items():
            CurrencyToUSD.objects.update_or_create(
                currency_code=key, defaults={"price": value}
            )

    print("Exchange rates updated.")
