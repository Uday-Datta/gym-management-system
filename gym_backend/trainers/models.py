from django.db import models

# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    photo = models.ImageField(upload_to='trainers/', blank=True)

    def __str__(self):
        return self.name