from rest_framework import serializers
from transactions.models import Transaction, Status


class StatusSerializer(serializers.ModelSerializer):

    label = serializers.SerializerMethodField()
    value = serializers.SerializerMethodField()

    class Meta:
        model = Status
        fields = '__all__'

    def get_label(self, obj):
        return obj.status

    def get_value(self, obj):
        return obj.status


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'

    status = serializers.CharField(source='status.status')
