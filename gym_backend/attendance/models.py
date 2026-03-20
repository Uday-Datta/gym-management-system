from django.db import models
from members.models import Member
from django.utils.timezone import now
# Create your models here.
class Attendance(models.Model):

    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    check_in = models.DateTimeField(auto_now_add=True)
    check_out = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        today = now().date()

        if not self.pk:
            if Attendance.objects.filter(member=self.member, check_in__date=today).exists():
                raise ValueError("Already checked in today")

        super().save(*args, **kwargs)

    def check_out_member(self):
        self.check_out = now()
        self.save()

    def __str__(self):
        return f"{self.member.name} - {self.check_in.date()}"