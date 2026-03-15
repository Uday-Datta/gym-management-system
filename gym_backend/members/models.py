from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField()
    membership_start_date = models.DateField(auto_now_add=True)
    membership_end_date = models.DateField(default=True)

    def __str__(self):
        return self.name