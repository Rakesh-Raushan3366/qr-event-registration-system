from django.urls import path
from . import views

app_name = 'sangh_shiksha_varg_samanya'

# Create your urls here.

urlpatterns = [
    path('Karyakarta-Vikas-Varg-Pratham-Samanya-Registration/', views.KaryakartaVikasVargPrathamSamanyaRegistration, name='karyakartavikasvargprathamsamanyaregistration'),
    path('Karyakarta-Vikas-Varg-Pratham-Samanya-View-Registration/', views.KaryakartaVikasVargPrathamSamanyaViewRegistration, name='karyakartavikasvargrathamsamanyaviewregistration'),
    path('Karyakarta-Vikas-Varg-Pratham-Samanya-Update-Registration/', views.KaryakartaVikasVargPrathamSamanyaUpdateRegistration, name='karyakartavikasvargprathamsamanyaupdateregistration'),
    path('user_logout/', views.user_logout, name='userlogout'), 
]
