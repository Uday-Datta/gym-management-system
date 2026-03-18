from django.db import models
from members.models import Member
from datetime import timedelta
# Create your models here.
class Payment(models.Model):

    PAYMENT_METHODS = [
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('bkash', 'bkash'),
        ('nagad', 'nagad'),
        ('rocket', 'rocket'),
    ]

    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHODS)
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        member = self.member
        plan = member.plan

        if plan:
            if member.expiry_date:
                member.expiry_date = member.expiry_date + timedelta(days=plan.duration_months)
            else:
                member.expiry_date = self.payment_date + timedelta(days=plan.duration_months)

            member.save()

    def __str__(self):
        return f"{self.member.name} - {self.amount}"