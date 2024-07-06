from django.contrib.auth.models import AbstractUser
from django.db import models






class User(AbstractUser):
    # Add any additional fields here
    
    username = None

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']  

    def __str__(self):
        return self.email


class Transaction(models.Model):
    transaction_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    currency = models.CharField(max_length=10, default="INR")

    def __str__(self):
        return f"{self.transaction_date} - {self.amount} - {self.category} - {self.description}"
