from django.urls import path
from .views import *


urlpatterns = [
    path('', createUserView, name='createUserView'),
    path('core/', coreindex, name='coreindex'),
]
