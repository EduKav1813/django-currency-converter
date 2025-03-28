from django.db import models


class CurrencyToUSD(models.Model):
    currency_code = models.CharField(max_length=3)
    price = models.DecimalField(max_digits=32, decimal_places=16)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.created_at}] {self.currency_code} = {self.price} (USD)"
