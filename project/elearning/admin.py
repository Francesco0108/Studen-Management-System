from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
admin.site.register(User)
admin.site.register(Myuser)
admin.site.register(Enrollment)
admin.site.register(Predmeti)
admin.site.register(Status)
admin.site.register(Role)
admin.site.register(SubjectStatus)


