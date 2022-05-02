from django.urls import path
from . import views


app_name = 'app_gen'

urlpatterns = [
    path('registration', views.register, name='registration'),
    path('login', views.login, name='login'),
    path('user_login', views.user_login, name='user_login'),
]
