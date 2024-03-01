from django.contrib import admin

from db.models import University, School, Program, Student

# Register your models here.

admin.site.register(University)
admin.site.register(School)
admin.site.register(Program)
admin.site.register(Student)
