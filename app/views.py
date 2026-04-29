from django.shortcuts import render, get_object_or_404, redirect
from employeeapp.models import Department, Salary, Employee
from django.contrib import messages
# Create your views here.

def list_department(request):
    departments = Department.objects.all()
    context = {'departments' : departments}
    return render(request, 'list_department.html', context)

def edit_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        dname = request.POST.get('dname')
        department.name = dname
        department.save()
        messages.success(request, "The Department is updated successfully")
        return redirect('list-department')
    context = {'department' :department}
    return render(request, 'edit_department.html', context)

def delete_department(request,pk):
    department = get_object_or_404(Department, pk=pk)
    department.delete()
    messages.success(request, "The Department is deleted successfully")
    return redirect('list-department')

    
def employee_salary(request):
    saleries = Salary.objects.all()
    context = {'saleries' :saleries}
    return render(request, 'employee_salary.html', context)

def list_employee(request):
    employees = Employee.objects.all()
    context = {'employees' : employees}
    return render(request, 'list_employee.html', context)
    
    