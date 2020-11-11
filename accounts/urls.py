from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),

    path('tickets/', views.tickets, name="tickets"),
    path('contractors/<str:pk_id>/', views.contractors, name="contractors"),
    path('user/', views.userPage, name="user"),

    path('create_ticket/<str:pk_id>/', views.create_ticket, name="create_ticket"),
    path('update_ticket/<str:pk_id>', views.update_ticket, name="update_ticket"),
    path('delete_ticket/<str:pk_id>', views.delete_ticket, name="delete_ticket"),
    path('create_contractor/', views.create_contractor, name="create_contractor"),
    path('update_contractor/<str:pk_id>', views.update_contractor, name="update_contractor"),
    path('delete_contractor/<str:pk_id>', views.delete_contractor, name="delete_contractor"),
]