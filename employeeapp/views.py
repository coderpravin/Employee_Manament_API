from django.shortcuts import render, get_object_or_404
from .models import Department, Employee, Salary
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import DepartmentSerializer, EmployeeSerializer, SalarySerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(["GET"])
def department_List(request):
    departments = Department.objects.all()
    serializer = DepartmentSerializer(departments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
    
@api_view(["GET"])
def individual_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    serializer = DepartmentSerializer(department)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_Department(request):
    serializer = DepartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def edit_Department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    serializer = DepartmentSerializer(department, data=request.data, partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_Department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    department.delete()
    return Response({"message" : "The data is deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


#This API For Employee
@api_view(["GET"])
def employee_List(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def individual_Employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    serializer =  EmployeeSerializer(employee)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def employee_Create(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def employee_Edit(request, pk):
    employee= get_object_or_404(Employee, pk=pk)
    serializer = EmployeeSerializer(employee, data=request.data, partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def employee_Delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return Response({"message" : "The employee data deleted"}, status=status.HTTP_200_OK)

@api_view(["GET"])
def salary_List(request):
    salary = Salary.objects.all()
    serializer = SalarySerializer(salary, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def individual_Salary(request,pk):
    salary = get_object_or_404(Salary, pk=pk)
    serializer = SalarySerializer(salary)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_salary(request):
    serializer = SalarySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def Salary_edit(request, pk):
    salary = get_object_or_404(Salary, pk=pk)
    serializer = SalarySerializer(salary, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(["PATCH"])
def salary_partial_edit(request, pk):
    salary = get_object_or_404(Salary, pk=pk)
    serializer = SalarySerializer(salary, data=request.data, partial =True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["DELETE"])
def delete_salary(request, pk):
    salary = get_object_or_404(Salary, pk=pk)
    salary.delete()
    return Response({'message':'The data is deleted'})
