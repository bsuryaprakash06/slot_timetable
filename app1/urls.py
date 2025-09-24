from django.urls import path
from . import views

urlpatterns = [
    path('', views.slot, name='slot'),  
    path('slot/', views.slot, name='slot'),
]
