from django.urls import path

from . import admin
from .views import index

urlpatterns = [
    path('', index, name='index'),

]