from django.urls import path
from akhilbhartiye import views

# modules name register here.
app_name = 'akhilbhartiye'

# Create your urls here.

urlpatterns = [ 
    path("", views.mobile_verification, name="mobile_verification"),
    path("otp/", views.otp_verification, name="otp_verification"),  
    path('akhil-registeration/', views.AkhilBhartiyaRegisteration, name='akhilregisteration'),
    path('user_logout/', views.user_logout, name='userlogout'),

]
