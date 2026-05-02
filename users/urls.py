from django.urls import path
from . import views
app_name ='users'
urlpatterns = [
    path('register-user', views.register_user, name="register-user"),
    path('login-user', views.login_user, name="login-user"),
    
]