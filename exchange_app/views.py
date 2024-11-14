from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Currency, ExchangeRate
from .serializers import CurrencySerializer, SimplerExchangeRateSerializer, ExchangeRateSerializer


class CurrencyListView(APIView):
    def get(self, request):
        currencies = Currency.objects.all()
        sort = request.query_params.get('sort', None)
        if sort == 'desc':
            currencies = currencies.order_by('-code')
        else:
            currencies = currencies.order_by('code')
        serializer = CurrencySerializer(currencies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LatestExchangeRateView(APIView):
    def get(self, request, base_code, target_code):
        try:
            sort = request.query_params.get('sort', None)
            if sort == 'rate':
                exchange_rate = ExchangeRate.objects.filter(
                    base_currency__code=base_code,
                    target_currency__code=target_code
                ).order_by('-exchange_rate')
                serializer = SimplerExchangeRateSerializer(exchange_rate, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif sort == 'date':
                exchange_rate = ExchangeRate.objects.filter(
                    base_currency__code=base_code,
                    target_currency__code=target_code
                ).order_by('-date')
                serializer = ExchangeRateSerializer(exchange_rate, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                exchange_rate = ExchangeRate.objects.filter(
                    base_currency__code=base_code,
                    target_currency__code=target_code
                ).latest('date')

                response_data = {
                    "currency_pair": f"{base_code}{target_code}",
                    "exchange_rate": float(exchange_rate.exchange_rate)
                }
                return Response(response_data, status=status.HTTP_200_OK)

        except ExchangeRate.DoesNotExist:
            return Response(
                {"error": "Exchange rate data not found for the specified currency pair"},
                status=status.HTTP_404_NOT_FOUND
            )
