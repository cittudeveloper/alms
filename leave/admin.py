from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register (LeaveType)
admin.site.register (LeaveDuration)
admin.site.register (LeaveProcess)
admin.site.register (LeaveApplicationStatus)
admin.site.register (LeaveResumption)
admin.site.register (LeaveRecommendation)
admin.site.register (LeaveApplication)
