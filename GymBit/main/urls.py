from django.conf.urls import url
from django.urls import path
from main import views
from .views import *

app_name = "main"

urlpatterns = [
    path('', index_view, name='index.html'),
]