from django.urls import path,include
from.import views

urlpatterns = [
    path("",views.registerpage,name='registerpage'),
    path("register/",views.userregister,name='register'),
    path("loginpage/",views.loginpage,name='login'),
    path("loginuser/",views.loginuser,name='loginuser'),

]   