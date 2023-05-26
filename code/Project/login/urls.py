from django.urls import path
from . import views


# URLConf #Umamaheswar
urlpatterns = [

    path('user/', views.user_login, name='User_Login'),
    path('register/', views.user_register, name='register'),

]
