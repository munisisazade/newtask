from rest_framework import serializers
from .models import Currency, Bank

class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = ('code', 'buy', 'sell')


class BankSerializer(serializers.ModelSerializer):


    cash = serializers.SerializerMethodField('get_c')
    nocash = serializers.SerializerMethodField('get_nc')

    update_time = serializers.SerializerMethodField('is_named_bar')

    def get_c(self, bank):
        currency = Currency.objects.filter(bank=bank, currency_type=1).order_by('-update_time')[:5]
        serializer = CurrencySerializer(instance=currency,many=True)
        return serializer.data
    def get_nc(self, bank):
        currency = Currency.objects.filter(bank=bank, currency_type=2).order_by('-update_time')[:5]
        serializer = CurrencySerializer(instance=currency,many=True)
        return serializer.data

    def is_named_bar(self, foo):
        return Currency.objects.all().last().update_time

    class Meta:
        model = Bank
        fields = ('name', 'link', 'map_link','cash','nocash','update_time')
