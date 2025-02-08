import json
import math

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
            return JsonResponse(
                {
                    "error": "Required fields: 'from', 'to', 'value'"
                }
            )

        rate = conversion_table[currency_from] / conversion_table[currency_to]
        print(f"rate is {rate}")
        value = round(float(value) * rate, ndigits=2)
        print(f"value: {value}")
        return JsonResponse({"value": str(value)})

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
