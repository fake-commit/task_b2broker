from django.db import models
from django.db.models import Sum


class Wallet(models.Model):
    label = models.CharField(max_length=255)

    @property
    def balance(self):
        return self.transactions.aggregate(total=Sum('amount'))['total'] or 0


class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='transactions')
    txid = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=20, decimal_places=18)

    def __str__(self):
        return f"Transaction {self.txid} with amount {self.amount}"
