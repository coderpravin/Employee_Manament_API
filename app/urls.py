from django.urls import path
from . import views
urlpatterns = [
    path('list-department/', views.list_department, name="list-department"),
    path('edit-department/<int:pk>', views.edit_department, name="edit-department"),
    path('delete-department/<int:pk>', views.delete_department, name="delete-department"),
    
    path('employee-salary/', views.employee_salary, name="employee-salary"),
    path('list-employee/', views.list_employee, name="list-employee"),
]