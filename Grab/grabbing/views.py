from django.shortcuts import render
from django.http import HttpResponse
import json, requests
from .models import Bank, Currency
from rest_framework import generics
from .serializers import CurrencySerializer, BankSerializer

class CreateView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


def parser(request):
    grab_url = requests.get('http://www.azn.az/data/data.json')
    if grab_url.status_code == 200:
        response = grab_url.text
        data = json.loads(response)
        for x in data:
             update_time= x.get('update_time')
             bank = Bank.objects.get(name=x['name'])
             d = x.get('cash')
             for k, v in d.items():
                 currency = Currency(
                 code = v.get('code'),
                 buy = v.get('buy'),
                 sell = v.get('sell'),
                 currency_type=1,
                 bank=bank,
                 )
                 currency.save()
             c = x.get('nocash')
             for k, v in c.items():
                 currency = Currency(
                 code = v.get('code'),
                 buy = v.get('buy'),
                 sell = v.get('sell'),
                 currency_type=2,
                 bank=bank,
                 )
                 currency.save()

    return render(request, 'parser.html')
