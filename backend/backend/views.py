import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import CurrencyToUSD


@csrf_exempt
def convert(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST requests are allowed"})

    try:
        data = json.loads(request.body)

        currency_from = data.get("from", "").strip()
        currency_to = data.get("to", "").strip()
        value = data.get("value", "")

        # If incomplete data
        if not currency_from or not currency_to or not value:
            return JsonResponse({"error": "Required fields: 'from', 'to', 'value'"})

        # If convert to self
        if currency_from == currency_to:
            return JsonResponse({"value": value})

        # Normal flow
        try:
            missing_currency = currency_from
            currency_to_usd_from = CurrencyToUSD.objects.get(
                currency_code=currency_from
            )
            missing_currency = currency_to
            currency_to_usd_to = CurrencyToUSD.objects.get(currency_code=currency_to)

        except Exception:
            return JsonResponse(
                {"error": f"Currency {missing_currency} is not supported."}
            )

        value = float(value)
        if value < 0:
            return JsonResponse({"error": f"Cannot convert negative value: '{value}'"})

        if value == 0:
            return JsonResponse({"value": 0})

        rate = currency_to_usd_from.price / currency_to_usd_to.price
        value = round(float(value) * rate, ndigits=2)
        return JsonResponse({"value": value})

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)


@csrf_exempt
def get_available_currencies(request):
    return JsonResponse(
        {"currencies": list(currency.currency_code for currency in CurrencyToUSD.objects.all())}
    )
