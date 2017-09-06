from django.contrib import admin
from .models import Bank, Currency


class CurrencyAdmin(admin.ModelAdmin):
    readonly_fields = ('get_bank_name',)
    list_display = ('code', 'buy', 'sell', 'currency_type','get_bank_name','update_time')
    list_filter = ('currency_type', 'bank','update_time')

admin.site.register(Bank),
admin.site.register(Currency, CurrencyAdmin)
