from django.db import models


# Create your models here.
class Wallet(models.Model):
    name = models.CharField(max_length= 255)
    balance = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    WITHDRAWAL = 'W'
    REFILL = 'R'

    OPERATION_TYPE_CHOICES = [
        (WITHDRAWAL, 'WITHDRAWAL'),
        (REFILL, 'REFILL')
    ]

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    operation_type = models.CharField(choices=OPERATION_TYPE_CHOICES, max_length=2)

    def __str__(self):
        return f"{self.operation_type} {self.amount}"
