from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.code


class ExchangeRate(models.Model):
    base_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='bas_currency')
    target_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='tar_currency')
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=4)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('base_currency', 'target_currency', 'date')

    def __str__(self):
        return f"{self.base_currency.code} to {self.target_currency.code} rate"