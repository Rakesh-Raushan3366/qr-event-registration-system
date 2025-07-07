from django.urls import path
from .import views

app_name = 'core'

urlpatterns = [
    # path('register/', views.register, name='register'),
    # path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    #path("verification_mobile/", views.mobile_verification, name="verification_mobile"),
    #path("otp_verify/", views.otp_verification, name="otp_verify"),
 
    # ================================================================ Admin Dashboard urls ==========================================================
    path('admin/', views.admin, name='admin'),
    # =============================================================== SuperAdmin Dashboard urls ======================================================
    
    # Super-Admin Count URLs Here.
    path('superadmin_dashboard/', views.superadmin_dashboard, name='superadmin_dashboard'),
    path('superadmin_dashboard/superadmin_userRole/', views.superadmin_userRole, name='superadmin_userRole'),
    path('delete_admin_role/<int:role_id>/', views.delete_admin_role, name='delete_admin_role'),
    path('delete_scanner_role/<int:scanner_id>/', views.delete_scanner_role, name='delete_scanner_role'),
    path('superadmin_dashboard/totalregistercount/', views.superadmin_dashboard_totalregistercount, name='superadmin_dashboard_totalregistercount'),
    path('superadmin_dashboard/totalothercount/', views.superadmin_dashboard_totalothercount, name='superadmin_dashboard_totalothercount'),

    # Sub-Admin Count URLs Here.
    path('sub_admin_dashboard/', views.sub_admin_dashboard, name='sub_admin_dashboard'),
    path('subadmin_dashboard/subadmin_userRole/', views.subadmin_userRole, name='subadmin_userRole'),
    path('delete_subadmin_role/<int:role_id>/', views.delete_subadmin_role, name='delete_subadmin_role'),
    path('delete_subscanner_role/<int:scanner_id>/', views.delete_subscanner_role, name='delete_subscanner_role'),

    # ================================================== Start Super Admin Chart URLs Here. ======================================
    path("superadmin_dashboard/vibhag-chart-data/", views.vibhag_chart_data, name="vibhag-chart-data"),
    path("superadmin_dashboard/nagar-chart-data/", views.nagar_chart_data, name="nagar_chart_data"),
    # ================================================== End Super Admin Chart URLs Here. =========================================
]