from django.urls import path
from . import views

urlpatterns = [
    path('generate_tables/', views.generate_tables, name='generate_tables'),
]