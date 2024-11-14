import yfinance as yf
from datetime import datetime
from django.core.management.base import BaseCommand
from exchange_app.models import Currency, ExchangeRate


class Command(BaseCommand):
    help = 'Load initial currency data from Yahoo Finance'

    def fetch_currency_data(self):
        pairs = ['EURUSD=X', 'USDJPY=X', 'PLNUSD=X']
        for pair in pairs:
            ticker = yf.Ticker(pair)
            exchange_rate = ticker.fast_info['lastPrice']
            base, target = pair[:3], pair[3:6]
            self.stdout.write(f"For pair {base}/{target}: {round(exchange_rate, 4)}")
            base_currency, _ = Currency.objects.get_or_create(code=base)
            target_currency, _ = Currency.objects.get_or_create(code=target)

            ExchangeRate.objects.create(base_currency=base_currency,
                                        target_currency=target_currency,
                                        exchange_rate=exchange_rate)

    def handle(self, *args, **kwargs):
        self.fetch_currency_data()
        self.stdout.write(self.style.SUCCESS('Successfully loaded initial currency data'))
