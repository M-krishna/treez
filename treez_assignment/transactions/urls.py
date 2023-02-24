from django.urls import path
from transactions.views import Transactions, Status

urlpatterns = [
    path('', Transactions.as_view(), name='transactions'),
    path('status', Status.as_view(), name='status')
]
