from invoice.models import Invoice,Transaction
from rest_framework import serializers

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('product', 'quantity','price','line_total','invoice_id')

class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    transactions = TransactionSerializer(many=True, read_only=True)
    class Meta:
        model = Invoice
        fields = ('customer', 'date', 'total_quantity', 'total_amount','transactions')



