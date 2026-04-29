from django.shortcuts import render
from employeeapp.models import Department
# Create your views here.

def list_department(request):
    departments = Department.objects.all()
    context = {'departments' : departments}
    return render(request, 'list_department.html', context)
    