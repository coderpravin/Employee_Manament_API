from rest_framework import serializers
from .models import Employee, Department, Salary
class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()
    class Meta:
        model = Employee
        fields = ["id", "name", "email", "mobile", "department"]
        
        
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"
        
    
class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = "__all__"
    
