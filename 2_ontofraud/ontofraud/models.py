from django.db import models

from model_utils import Choices


class Wallet(models.Model):
    STATUSES = Choices(
        ('fraud', 'Fraudulent'),
        ('suspicious', 'Suspicious'),
        ('new', 'New'),
        ('ok', 'Ok'),
        ('trusted', 'Trusted'),
    )
    hashid = models.CharField(max_length=64, unique=True)
    status = models.CharField(max_length=16, choices=STATUSES, default=STATUSES.new)

    def __str__(self):
        return self.hashid


class Transaction(models.Model):
    hashid = models.CharField(max_length=64, unique=True)
    from_address = models.ForeignKey(Wallet, related_name='payers_transactions', on_delete=models.CASCADE)
    to_address = models.ForeignKey(Wallet, related_name='receivers_transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=16, decimal_places=9)
    description = models.CharField(max_length=64)

    def __str__(self):
        return self.hashid
