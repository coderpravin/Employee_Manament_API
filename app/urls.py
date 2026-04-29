from django.urls import path
from . import views
urlpatterns = [
    path('list-department/', views.list_department, name="list-department"),
]