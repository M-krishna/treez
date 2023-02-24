import datetime
import random
from django.db import migrations
import factory
from transactions.models import Transaction
from faker import Faker
from faker.providers import python

fake = Faker()
fake.add_provider(python)


SOURCES = [source[0] for source in Transaction.SOURCE_CHOICES]


def seed_status_data(apps, schema_editor):
    Status = apps.get_model('transactions', 'Status')
    Status.objects.bulk_create([
        Status(status='Authorized'),
        Status(status='Initiated'),
        Status(status='Successful'),
        Status(status='Returned'),
        Status(status='Cancelled')
    ])


def seed_transactions_data(apps, schema_editor):
    Transaction = apps.get_model('transactions', 'Transaction')
    Status = apps.get_model('transactions', 'Status')
    NO_OF_TRANSACTIONS = 50

    status_ids = list(Status.objects.all().values_list('id', flat=True))
    for _ in range(NO_OF_TRANSACTIONS):
        Transaction.objects.create(
            customer=fake.name(),
            gross_amount=fake.pydecimal(left_digits=4, right_digits=2, positive=True),
            swifter_id=fake.pystr_format('????##', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
            external_id=fake.pystr_format('????##', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
            source=random.choice(SOURCES),
            status_id=random.choice(status_ids),
            date=factory.LazyFunction(datetime.datetime.now)
        )


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_status_data),
        migrations.RunPython(seed_transactions_data)
    ]
