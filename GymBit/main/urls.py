from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index.html'),
    path('trainees', trainees_view, name='trainees.html'),
    path('charts', charts_view, name='charts.html'),
    path('profile', profile_view, name='profile.html'),
    path('tables', tables_view, name='tables.html'),
    path('login', login_view, name='login.html'),
    path('register', register_view, name="register.html"),
    path('trainee/<str:name>', trainee_info_view, name='trainee_profile.html')
]
