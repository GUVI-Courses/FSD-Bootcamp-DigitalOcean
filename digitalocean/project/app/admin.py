from django.contrib import admin
from .models import Contact,Order,Employee
# Register your models here.
admin.site.register(Order)
admin.site.register(Contact)
admin.site.register(Employee)