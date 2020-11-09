from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('tickets/<str:pk_id>/', views.tickets),
    path('contractors/<str:pk_id>/', views.contractors),
]
