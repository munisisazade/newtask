from django.db import models
from django.utils import timezone

Choice = (
(1, 'cash'),
(2, 'nocash')

)

class Bank(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=300)
    map_link = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Currency(models.Model):
    code = models.CharField(max_length=10)
    buy = models.CharField(max_length=10)
    sell = models.CharField(max_length=10)
    currency_type = models.IntegerField(choices=Choice, default=1)
    bank = models.ForeignKey(Bank, related_name='exchange')
    update_time = models.DateTimeField(default=timezone.now)

    def get_bank_name(self):
        return "%s" % self.bank.name

    get_bank_name.show_tags = True
