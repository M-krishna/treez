# Generated by Django 4.1.7 on 2023-02-24 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20230224_0549'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'Status'},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'verbose_name_plural': 'Transactions'},
        ),
    ]
