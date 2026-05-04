from django.contrib import admin
from .models import Employee, Salary, Department, ContactEnquiry
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "mobile", "get_department", 'get_salary']
    search_fields = ["name", "mobile"]
    list_filter = ["department"]

    def get_department(self, object):
        return object.department.name
    
    def get_salary(self, object):
        return object.salary.salary
    
admin.site.register(Employee, EmployeeAdmin)

class SalaryAdmin(admin.ModelAdmin):
    list_display = ["employee", "salary"]
    
admin.site.register(Salary, SalaryAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name"]
    
admin.site.register(Department, DepartmentAdmin)


class ContactEnquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
    
    def has_change_permission(self, request, obj = None):
        return False
    
    def has_add_permission(self, request):
        return False
admin.site.register(ContactEnquiry, ContactEnquiryAdmin)


