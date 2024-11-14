from django.contrib import admin
from .models import ExchangeRate, Currency


class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('base_currency', 'target_currency', 'exchange_rate', 'date')
    list_filter = ('base_currency', 'target_currency')
    search_fields = ('base_currency__code', 'target_currency__code')


admin.site.register(ExchangeRate, ExchangeRateAdmin)
admin.site.register(Currency)
