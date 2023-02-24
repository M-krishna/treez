from django.contrib import admin
from transactions.models import Transaction, Status

# Register your models here.
admin.site.register(Transaction)
admin.site.register(Status)