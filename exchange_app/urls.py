from django.urls import path
from .views import CurrencyListView, LatestExchangeRateView

urlpatterns = [
    path('currency/', CurrencyListView.as_view(), name='currency-list'),
    path('currency/<str:base_code>/<str:target_code>/', LatestExchangeRateView.as_view(), name='latest-exchange-rate')
]