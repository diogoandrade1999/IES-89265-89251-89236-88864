from main.views import *
from rest_framework_mongoengine import routers


routers = routers.DefaultRouter()
routers.register('trainees', TraineesView, 'trainees')
routers.register('profile', ProfileView, 'profile')
routers.register('trainee_profile', TraineesProfileView, 'trainee_profile')
routers.register('charts', ChartsView, 'charts')

urlpatterns = routers.urls
