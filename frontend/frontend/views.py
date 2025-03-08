from django.shortcuts import render
import requests


def index(request):
    response = requests.get("http://127.0.0.1:8000/currencies")
    available_currencies = []
    if response.status_code == 200:
        available_currencies = response.json()["currencies"]
    return render(request, "index.html", {"currencies": available_currencies})
