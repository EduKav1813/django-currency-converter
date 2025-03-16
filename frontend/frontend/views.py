import requests
from django.shortcuts import render


def index(request):
    response = requests.get("http://backend:8000/currencies")
    available_currencies = []
    if response.status_code == 200:
        available_currencies = response.json()["currencies"]
    return render(request, "index.html", {"currencies": available_currencies})
