from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .smsapis import get_chetra_prant_mappings, get_registration_mappings

# URL patterns for the project Module Configuration

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('', include('register_samautkarsh.urls', namespace='register_samautkarsh')),
    path('updated_registration/', include('updated_registration.urls', namespace='updated_registration')),
    path('dashboard/', include('core.urls', namespace='core')),
    path('scanner/', include('scanner_admin.urls', namespace='scanner_admin')),
    path('ghoshwarg/', include('ghosh_warg.urls', namespace='ghosh_warg')),      # घोष वर्ग
    path('ABPP/', include('akhilbhartiye.urls', namespace='akhilbhartiye')),      # घोष वर्ग 
    path('get-registration-mappings/', get_registration_mappings, name='get_registration_mappings'),  # Get All Registration Mappings
    path('get-chetra-prant-mappings/', get_chetra_prant_mappings, name='get_chetra_prant_mappings'),  # Get Chetra Prant Mappings
    # path('akhil-bhartiye/', include('akhilbhartiye.urls', namespace='akhilbhartiye')),    # कार्यकर्ता विकास वर्ग – प्रथम (सामान्य)
    # path('sangh-shiksha-varg-vishesh/', include('sangh_shiksha_varg_vishesh.urls', namespace='sangh_shiksha_varg_vishesh')),    # संघ शिक्षा वर्ग (विशेष)
    # path('sangh-shiksha-varg-samanya/', include('sangh_shiksha_varg_samanya.urls', namespace='sangh_shiksha_varg_samanya')),    # संघ शिक्षा वर्ग (सामान्य)
    # path('karyakarta-vikas-varg-pratham-samanya/', include('karyakarta_vikas_varg_pratham_samanya.urls', namespace='karyakarta_vikas_varg_pratham_samanya')),    # कार्यकर्ता विकास वर्ग – प्रथम (सामान्य)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
