from django.shortcuts import render, get_object_or_404, redirect
from employeeapp.models import Department, Salary, Employee
from django.contrib import messages
from decimal import Decimal
from django.core.paginator import Paginator
# Create your views here.

def list_department(request):
    departments = Department.objects.all()
    paginators = Paginator(departments, 5)
    page = request.GET.get("page")
    departments = paginators.get_page(page)
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
    paginators = Paginator(saleries, 5)
    page = request.GET.get("page")
    saleries = paginators.get_page(page)
    context = {'saleries' :saleries}
    return render(request, 'employee_salary.html', context)

def edit_salary(request, pk):
    salary_instance = get_object_or_404(Salary, pk=pk)
    if request.method == "POST":
        new_salary = request.POST.get('salary') #str
        salary_instance.salary = Decimal(new_salary)
        salary_instance.save()
        return redirect('employee-salary')
    context = {'salary':salary_instance}
    return render(request, 'edit_salary.html', context)

def delete_salary(request, pk):
    salary_instance = get_object_or_404(Salary, pk=pk)
    salary_instance.delete()
    messages.success(request, "The Salary is deleted")
    return redirect('employee-salary')
    

def list_employee(request):
    employees = Employee.objects.all()
    paginators = Paginator(employees, 5)
    page = request.GET.get("page")
    employees = paginators.get_page(page)
    context = {'employees' : employees}
    return render(request, 'list_employee.html', context)
    
    
def edit_employee(request, pk):
    employee_instance = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        print("Post request come")
        ename = request.POST.get('ename')
        eemail = request.POST.get('eemail')
        emobile = request.POST.get('emobile')
        
        try:
           
            employee_instance.name = ename
            employee_instance.email = eemail
            employee_instance.mobile = emobile
            
            employee_instance.save()
            print("employee record save")
            messages.success(request, "The Employee Record Update Successfully")
            return redirect('list-employee')    
            
        except Department.DoesNotExist:
            messages.error(request, "The Department not found")
                    
        
    context= {'employee':employee_instance}
    return render(request, 'edit_employee.html', context)

def delete_employee(request, pk):
    employee_instance = get_object_or_404(Employee, pk=pk)
    employee_instance.delete()
    messages.success(request, "The Employee Record Deleted")
    return redirect('list-employee') 


def base_view(request):
    return render(request, 'base.html')
    