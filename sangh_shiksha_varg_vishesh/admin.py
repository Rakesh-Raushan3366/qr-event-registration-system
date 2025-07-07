from django.contrib import admin # type: ignore
from .models import *

# Register your models here.

admin.site.register(EkaiMaster)
admin.site.register(DayitvMaster)
# admin.site.register(BarcodeScan)
@admin.register(BarcodeScan)
class BarcodeScanAdmin(admin.ModelAdmin):
    list_display = ['name','phone_number', 'nagar', 'dayitv', 'qrcode']
    search_fields = ['name', 'phone_number', 'nagar', 'dayitv', 'qrcode']

admin.site.register(PincodeMaster)
admin.site.register(NagarMaster)
admin.site.register(ZilaMaster)
admin.site.register(VibhagMaster)
admin.site.register(PrantMaster)

admin.site.register(ProfessionMaster)
# admin.site.register(RegisterSamautkarshRegistration)
@admin.register(RegisterSamautkarshRegistration)
class RegisterSamautkarshRegistrationAdmin(admin.ModelAdmin):
    list_display = ['name','phone_number', 'gender', 'corress_address', 'perman_address', 'nagar_address', 'pincode', 'user_type','ekai_mandal', 'referral_code','ekai_nagar','ekai_basti','ekai_upbasti']
    search_fields = ['name', 'phone_number', 'gender', 'perman_address', 'nagar_address', 'pincode','referral_code']