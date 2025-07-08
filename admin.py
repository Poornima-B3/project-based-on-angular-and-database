from django.contrib import admin

# Register your models here.
from StudentApp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address", "fee")
admin.site.register(Student, StudentAdmin)