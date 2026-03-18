from django.db import models

# Create your models here.
class Attendance(models.Model):
    member_id = models.IntegerField()
    check_in_time = models.DateTimeField(auto_now_add=True)
    check_out_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Attendance {self.id} - Member {self.member_id} - Check-in {self.check_in_time}"