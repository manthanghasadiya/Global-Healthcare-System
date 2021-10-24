from django.contrib import admin
from django.contrib.auth.models import User
from .models import userInfo, doctorInfo, History, Appointment, Feedback

admin.site.register(userInfo)
admin.site.register(doctorInfo)
admin.site.register(History)
admin.site.register(Appointment)
admin.site.register(Feedback)
