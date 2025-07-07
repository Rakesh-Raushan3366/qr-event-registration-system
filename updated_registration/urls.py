from django.urls import path
from . import views as up

app_name = 'updated_registration'

# Create your urls here.

urlpatterns = [
    path('', up.homepage, name='home'),
    path("mobileverification/", up.mobileVerification, name="mobileverification"),
    path("otpverification/", up.otpverification, name="otpverification"),
    path('verifyregistration/', up.verifyRegistration, name='verifyregistration'),
    path('profile/', up.profile, name='profile'),   
    path('viewregistration/', up.viewregistration, name='viewregistration'),
    path('updateprofile/', up.updateprofile, name='updateprofile'),
    path('qr/<str:data>/', up.generate_qr, name='generate_qr'),
    path('user_logout/', up.user_logout, name='userlogout'),  
]
