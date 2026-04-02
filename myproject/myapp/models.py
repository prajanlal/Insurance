from django.db import models

class Policy(models.Model):
    policy_type = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    amount = models.IntegerField()


class Claim(models.Model):
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    document = models.CharField(max_length=255)