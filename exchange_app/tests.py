from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Currency, ExchangeRate

class CurrencyTests(APITestCase):
    def setUp(self):
        self.base_currency = Currency.objects.create(code="EUR")
        self.target_currency = Currency.objects.create(code="USD")
        ExchangeRate.objects.create(
            base_currency=self.base_currency,
            target_currency=self.target_currency,
            exchange_rate=1.034,
            date="2024-01-01"
        )

    def test_currency_list(self):
        url = reverse('currency-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_latest_exchange_rate(self):
        url = reverse('latest-exchange-rate', args=['EUR', 'USD'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['exchange_rate'], 1.034)
        self.assertEqual(response.data['currency_pair'], 'EURUSD')