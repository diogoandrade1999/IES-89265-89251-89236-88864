from django.urls import path
from main.views import *


urlpatterns = [
    path('', index_view, name='index.html'),
    path('trainees', trainees_view, name='trainees.html'),
    path('charts/<int:id>/', charts_view, name='charts.html'),
    path('profile', profile_view, name='profile.html'),
    # path('tables', tables_view, name='tables.html'),
    path('login', login_view, name='login.html'),
    path('logout', logout_view, name='logout.html'),
    path('register', register_view, name="register.html"),
    path('trainee_profile/<int:id>/', trainee_info_view, name='trainee_profile.html'),
]
