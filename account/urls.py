from django.urls import path
from . import views

# URL patterns for the account app

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.user_logout, name='logout'),
]