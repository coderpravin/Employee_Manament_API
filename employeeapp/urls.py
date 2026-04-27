from django.urls import path
from . import views
urlpatterns = [
    path('', views.department_List, name="department-list"),
    path('<int:pk>/', views.individual_department, name="individual-dept"),
    path('create-dept/', views.create_Department, name="create-dept"),
    path('edit-dept/<int:pk>/', views.edit_Department, name="edit-dept"),
    path('del-dept/<int:pk>/', views.delete_Department, name="del-dept"),
    
    path('employee_List/', views.employee_List, name="employee_List"),
    path('individual_Employee/<int:pk>/', views.individual_Employee, name="individual_Employee"),
    path('employee_create/', views.employee_Create, name="employee_create"), 
    path('employee_Edit/<int:pk>/', views.employee_Edit, name="employee_Edit"), 
    path('employee_Delete/<int:pk>/', views.employee_Delete, name="employee_Delete"), 
]
