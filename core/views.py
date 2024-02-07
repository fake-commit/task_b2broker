from rest_framework import viewsets
from rest_framework_json_api.django_filters import DjangoFilterBackend

from .models import Wallet, Transaction
from .serializers import WalletSerializer, TransactionSerializer


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    filterset_fields = {
        'label': ('exact', 'icontains', 'iexact', 'contains',),
    }


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filterset_fields = {
        'txid': ('exact', 'icontains', 'iexact', 'contains',),
        'wallet': ('exact',),
        'amount': ('exact', '')
    }