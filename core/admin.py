from django.contrib import admin
from .models import *

# Register your models here.

# @admin.register(Role)
# class RoleAdmin(admin.ModelAdmin):
#     list_display = ['id','name', 'parent_role']

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'role']


@admin.register(BarcodeScan)
class BarcodeScanAdmin(admin.ModelAdmin):
    list_display = ['barcode_scan_id', 'name', 'phone_number', 'nagar', 'dayitv', 'qrcode', 'updated_at']

@admin.register(DayitvMaster)
class DayitvMasterAdmin(admin.ModelAdmin):
    list_display = ['dayitv_id', 'dayitv_name', 'ekai']

@admin.register(EkaiMaster)
class EkaiMasterAdmin(admin.ModelAdmin):
    list_display = ['ekai_id', 'ekai_name']

@admin.register(NagarMaster)
class NagarMasterAdmin(admin.ModelAdmin):
    list_display = ['nagar_id', 'nagar_name', 'nagar_hindi', 'jila']

@admin.register(PincodeMaster)
class PincodeMasterAdmin(admin.ModelAdmin):
    list_display = ['pincode_id', 'pincode', 'state', 'nagar', 'nagar_hindi']

@admin.register(PrantMaster)
class PrantMasterAdmin(admin.ModelAdmin):
    list_display = ['prant_id', 'prant_name', 'prant_hindi']

@admin.register(ProfessionMaster)
class ProfessionMasterAdmin(admin.ModelAdmin):
    list_display = ['profession_id', 'profession_name']

@admin.register(RegisterSamautkarshOtp)
class RegisterSamautkarshOtpAdmin(admin.ModelAdmin):
    list_display = ['id', 'mobile', 'otp', 'created_at']

@admin.register(RegisterSamautkarshRegistration)
class RegisterSamautkarshRegistrationAdmin(admin.ModelAdmin):
    list_display = ['register_id', 'name', 'dob', 'phone_number', 'gender', 'corress_address', 'nagar_address', 'pincode', 'user_type', 'updated_on']

@admin.register(RegisterSamautkarshUser)
class RegisterSamautkarshUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'mobile']

@admin.register(VibhagMaster)
class VibhagMasterAdmin(admin.ModelAdmin):
    list_display = ['vibhag_id', 'vibhag_name', 'vibhag_hindi', 'prant']

@admin.register(Vividhsanghthan)
class VividhsanghthanAdmin(admin.ModelAdmin):
    list_display = ['vividhsangathan_id', 'vividhsangathan_name', 'referral_code']

@admin.register(ZilaMaster)
class ZilaMasterAdmin(admin.ModelAdmin):
    list_display = ['jila_id', 'jila_name', 'jila_hindi', 'vibhag']