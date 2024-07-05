from django.db import models


class Transaction(models.Model):
    transaction_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    currency = models.CharField(max_length=10, default="INR")

    def __str__(self):
        return f"{self.transaction_date} - {self.amount} - {self.category} - {self.description}"
