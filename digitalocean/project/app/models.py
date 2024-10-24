from django.db import models
from django.utils.timezone import now

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.CharField(max_length=12)
    message=models.TextField()
    def __str__(self):
        return self.name     


class Employee(models.Model):
    emp_id=models.AutoField(primary_key=True)
    emp_name=models.CharField(max_length=50)
    emp_email=models.EmailField()
    emp_salary=models.IntegerField()
    emp_number=models.CharField(max_length=12)
    def __str__(self):
        return self.emp_name
    


class Order(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    age=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    slot=models.CharField(max_length=50)
    trainer=models.CharField(max_length=50)
    locality=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)        
    timeStamp=models.DateTimeField(default=now)

    
    def __str__(self):
        return self.name
        