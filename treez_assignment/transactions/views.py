from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from transactions.models import Transaction, Status
from transactions.serializers import TransactionSerializer, StatusSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import Filter, FilterSet
from django_filters.constants import EMPTY_VALUES


class ListFilter(Filter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs
        values_list = value.split(',')
        qs = super().filter(qs, values_list)
        return qs


class StatusFilter(FilterSet):
    status = ListFilter(field_name='status', lookup_expr='in')


class Transactions(ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = StatusFilter
    search_fields = ['customer']


class Status(ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
