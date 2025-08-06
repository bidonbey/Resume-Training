from django.urls import path

from . import admin
from .views import index,contact

urlpatterns = [
    path('', index, name='index'),
    path('contact',contact, name='contact'),

]