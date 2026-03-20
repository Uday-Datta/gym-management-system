from django.contrib import admin
from .models import Attendance
# Register your models here.
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('member', 'check_in', 'check_out')
    list_filter = ('check_in', )
    search_fields = ('member__name',)
admin.site.register(Attendance, AttendanceAdmin)