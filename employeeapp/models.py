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
    
    
class ContactEnquiryManager(models.Manager):
    def get_recent_enquiries(self):
        return self.get_queryset().order_by("-created_at")
        
    def search_by_email(self, email):
        return self.get_queryset().filter(email__icontains=email)
    
    
class ContactEnquiry(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)
    
    objects = ContactEnquiryManager()
    
    
    
    
    
    
    
    
    
       