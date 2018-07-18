from django.contrib import admin

# Register your models here.
from app1.models import Course,Studyhall,Student,Enquiry,Expense

admin.site.register(Course)
admin.site.register(Studyhall)
admin.site.register(Student)
admin.site.register(Enquiry)
admin.site.register(Expense)