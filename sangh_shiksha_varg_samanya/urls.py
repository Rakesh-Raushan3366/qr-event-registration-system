from django.urls import path
from . import views

app_name = 'sangh_shiksha_varg_samanya'

# Create your urls here.

urlpatterns = [
    # Registerations and login modules
    path("mobile_verification/", views.mobile_verification, name="mobile_verification"),
    path("otp/", views.otp_verification, name="otp_verification"),
    path('', views.homepage, name='home'),
    path('verify_registration/', views.verify_registration, name='verify_registration'),
    path('register/', views.register, name='register'),   
    path('view_registration/', views.view_registration, name='view_registration'),
    path('update/', views.update_register, name='update_register'),

    # QR-Code Scanner modules
    # path("scan_qr/", views.scan_qr, name="scan_qr"),
    # path("save_qr/", views.save_qr, name="save_qr"),
    # path("history/", views.qr_history, name="qr_history"),
    path('qr/<str:data>/', views.generate_qr, name='generate_qr'),
    path('user_logout/', views.user_logout, name='userlogout'),
  
]
