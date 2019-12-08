from django.conf.urls import url
from django.urls import path
from main import views
from .views import *

urlpatterns = [
    path('', index_view, name='index.html'),
    url('trainees', trainees_view, name='trainees.html'),
    url('charts', charts_view, name='charts.html'),
    url('profile', profile_view, name='profile.html'),
    url('tables', tables_view, name='tables.html'),
    url('login', login_view, name='login.html'),
    url('register', register_view, name="register.html"),
    url('trainee', trainee_info_view, name='trainee_profile.html')
]