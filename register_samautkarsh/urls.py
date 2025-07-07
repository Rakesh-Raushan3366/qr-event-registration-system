from django.urls import path
from . import views
from . import smsapis

# modules name register here.
app_name = 'register_samautkarsh'
# Create your urls here.

urlpatterns = [
    # Registerations and login modules
    path("mobile_verification/", views.mobile_verification, name="mobile_verification"),
    path("otp/", views.otp_verification, name="otp_verification"),
    path('', views.homepage, name='home'),
    path('role_glossary/', views.role_glossary, name='role_glossary'),
    path('verify_registration/', views.verify_registration, name='verify_registration'),
    path('register/', views.register, name='register'),   
    path('view_registration/', views.view_registration, name='view_registration'),
    path('update/', views.update_register, name='update_register'),

    # Registration for Shatabdi (शताब्दी वर्ष सूची)
    path('register_shatabdi/', views.register_shatabdi, name='register_shatabdi'),
    path('get-registration-mappings/', smsapis.get_registration_mappings, name='get_registration_mappings'),

    path('qr/<str:data>/', views.generate_qr, name='generate_qr'),
    path('user_logout/', views.user_logout, name='userlogout'),
  
]
