from django.urls import path
from . import views

# modules name register here.
app_name = 'sangh_shiksha_varg_vishesh'

# Create your urls here.

urlpatterns = [
    path('verify_registration/', views.verify_registration, name='verify_registration'),
    path('register/', views.register, name='register'),   
    path('view_registration/', views.view_registration, name='view_registration'),
    path('update/', views.update_register, name='update_register'),
]
