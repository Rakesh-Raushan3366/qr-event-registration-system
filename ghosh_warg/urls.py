from django.urls import path
from . import views

# modules name register here.
app_name = 'ghosh_warg'

# Create your urls here.

urlpatterns = [ 
    path("", views.mobile_verification, name="mobile_verification"),
    path("otp/", views.otp_verification, name="otp_verification"),  
    path('ghoshwargregisteration/', views.GhoshWargRegisteration, name='ghoshwargregisteration'),
    path('ghoshwargviewregistration/', views.GhoshWargViewRegistration, name='ghoshwargviewregistration'),
    path('ghoshwargupdateregistration/', views.GhoshWargUpdateRegistration, name='ghoshwargupdateregistration'),
    path('user_logout/', views.user_logout, name='userlogout'),
]
