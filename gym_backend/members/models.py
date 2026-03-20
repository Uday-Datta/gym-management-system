from django.db import models
from datetime import timedelta
from trainers.models import Trainer
from plans.models import Plan
# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    photo = models.ImageField(upload_to='members/', blank=True)

    join_date = models.DateField(auto_now_add=True)

    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)

    expiry_date = models.DateField(null=True, blank=True)

    status = models.CharField(max_length=20, default='active')

    def __str__(self):
        return self.name