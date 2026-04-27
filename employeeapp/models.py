from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length = 100)
    
    
    def __str__(self):
        return self.name
    
def check_mobile_digit(value):
    if not value.isdigit():
        raise ValidationError("Mobile Number should be only digit")
    if len(value) != 10:
        raise ValidationError("Mobile Number should be 10 digit")   
    return value 

class Employee(models.Model):
    name  = models.CharField(max_length=100)
    email = models.EmailField(unique = True)
    mobile = models.CharField(max_length=10, validators=[check_mobile_digit])
    
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Salary(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='salary') 
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    
       