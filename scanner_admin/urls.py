from django.urls import path
from .import views

# module name register here.
app_name = 'scanner_admin'

urlpatterns = [
    path("scanner_verification_mobile/", views.scanner_mobile_verification, name="scanner_verification_mobile"),
    path("scanner_otp_verify/", views.scanner_otp_verification, name="scanner_otp_verify"),
    path("scan_qr/", views.scan_qr, name="scan_qr"),
    path("scan_save_qr/", views.scan_save_qr, name="scan_save_qr"),
    path("qr_history/", views.qr_history, name="qr_history"),
]