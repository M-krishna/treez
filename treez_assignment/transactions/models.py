from django.db import models
from transactions.custom_fields import CurrencyField


class Status(models.Model):
    STATUS_CHOICES = [
        ('AUTHORIZED', 'Authorized'),
        ('INITIATED', 'Initiated'),
        ('SUCCESSFUL', 'Successful'),
        ('RETURNED', 'Returned'),
        ('CANCELLED', 'Cancelled'),
    ]
    status = models.CharField(choices=STATUS_CHOICES, max_length=30)

    class Meta:
        verbose_name_plural = "Status"


class Transaction(models.Model):
    SOURCE_CHOICES = [
        ('PAYMENTS', 'Payments'),
        ('E-COMMERCE', 'E-commerce'),
        ('IN-STORE', 'In-store'),
    ]

    id = models.AutoField(primary_key=True)
    customer = models.CharField(max_length=255)
    gross_amount = CurrencyField(decimal_places=2, max_digits=10)
    swifter_id = models.CharField(max_length=6)
    external_id = models.CharField(max_length=6)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=30)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Transactions"
