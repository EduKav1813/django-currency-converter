import json

from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .conversion_table import conversion_table


@csrf_exempt
def convert(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST requests are allowed"})

    try:
        data = json.loads(request.body)

        currency_from = data.get("from", "").strip()
        currency_to = data.get("to", "").strip()
        value = data.get("value", "")

        if not currency_from or not currency_to or not value:
            return JsonResponse({"error": "Required fields: 'from', 'to', 'value'"})

        for currency in [currency_from, currency_to]:
            if currency not in conversion_table.keys():
                return JsonResponse(
                    {"error": f"Currency '{currency}' is not supported"}
                )

        value = float(value)
        if value < 0:
            return JsonResponse({"error": f"Cannot convert negative value: '{value}'"})

        if value == 0:
            return JsonResponse({"value": 0})

        rate = conversion_table[currency_from] / conversion_table[currency_to]
        value = round(float(value) * rate, ndigits=2)
        return JsonResponse({"value": value})

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
