from django.urls import path
from . import views
urlpatterns = [
    path('list-department/', views.list_department, name="list-department"),
    path('edit-department/<int:pk>', views.edit_department, name="edit-department"),
    path('delete-department/<int:pk>', views.delete_department, name="delete-department"),
    
    path('employee-salary/', views.employee_salary, name="employee-salary"),
    path('edit-salary/<int:pk>', views.edit_salary, name="edit-salary"),
    path('delete-salary/<int:pk>', views.delete_salary, name="delete-salary"),
    
    path('list-employee/', views.list_employee, name="list-employee"),
    path('edit-employee/<int:pk>', views.edit_employee, name="edit-employee"),
    path('delete-employee/<int:pk>', views.delete_employee, name="delete-employee"),
    
    path('base-page', views.base_view, name="base-page"),
    
    path('about-page', views.about_page, name="about-page"),
    path('contact-page', views.contact_page, name="contact-page"),
    
    
    
    
    
]