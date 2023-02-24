from django.db import models
from decimal import Decimal


class CurrencyField(models.DecimalField):

    def to_python(self, value):
        try:
            return super().to_python(value).quantize(Decimal("0.01"))
        except AttributeError:
            return None
