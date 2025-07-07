# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models # type: ignore


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BarcodeScan(models.Model):
    barcode_scan_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=255, null=True,unique=True)
    nagar = models.CharField(max_length=255, null=True)
    dayitv = models.CharField(max_length=255, null=True)
    qrcode = models.CharField(max_length=255, null=True)
    status=models.CharField(max_length=255, null=True,default='pending')
    #role_check_box=models.CharField(max_length=255,null=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        managed = False
        db_table = 'barcode_scan'


class DayitvMaster(models.Model):
    dayitv_id = models.AutoField(primary_key=True)
    dayitv_name = models.CharField(max_length=255)
    ekai = models.ForeignKey('EkaiMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dayitv_master'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EkaiMaster(models.Model):
    ekai_id = models.AutoField(primary_key=True)
    ekai_name = models.CharField(max_length=255)
    ekai_hindi = models.TextField(null=True)

    class Meta:
        managed = False
        db_table = 'ekai_master'


class NagarMaster(models.Model):
    nagar_id = models.AutoField(primary_key=True)
    nagar_name = models.CharField(max_length=255)
    nagar_hindi = models.CharField(max_length=255)
    jila = models.ForeignKey('ZilaMaster', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nagar_master'


class ScannerApprovals(models.Model):
    scanner_id = models.AutoField(primary_key=True)
    scanner_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    #scanner_check_box=models.CharField(max_length=255,null=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    class Meta:
        managed = False
        db_table = 'scanr_approval_persons'

class PincodeMaster(models.Model):
    pincode_id = models.BigAutoField(primary_key=True)
    pincode = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    nagar = models.CharField(max_length=255, blank=True, null=True)
    nagar_hindi = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pincode_master'


class PrantMaster(models.Model):
    prant_id = models.AutoField(primary_key=True)
    prant_name = models.CharField(max_length=255)
    prant_hindi = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'prant_master'


class ProfessionMaster(models.Model):
    profession_id = models.AutoField(primary_key=True)
    profession_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'profession_master'


class RegisterSamautkarshOtp(models.Model):
    id = models.BigAutoField(primary_key=True)
    mobile = models.CharField(max_length=10)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'register_samautkarsh_otp'


class RegisterSamautkarshRegistration(models.Model):
    register_id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    last_name = models.TextField()
    dob = models.DateField()
    phone_number = models.CharField(unique=True, max_length=255)
    gender = models.CharField(max_length=255)
    blood_group = models.CharField(max_length=255)
    corress_address = models.TextField(blank=True, null=True)
    perman_address = models.TextField(blank=True, null=True)
    address_pincode = models.TextField(blank=True, null=True)
    address_state = models.TextField(max_length=255, blank=True, null=True)
    ekai_milaan = models.TextField(blank=True, null=True)
    ekai_sakha_milan = models.TextField(blank=True, null=True)
    nagar_address = models.TextField(blank=True, null=True)
    pincode = models.TextField()
    user_type = models.CharField(max_length=255)
    ekai_mandal = models.CharField(max_length=255, blank=True, null=True)
    referral_code = models.CharField(max_length=255)
    vividhsangathan = models.CharField(max_length=255, blank=True, null=True)
    ekai_basti = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(max_length=255, blank=True, null=True)
    ekai_upbasti = models.CharField(max_length=255, blank=True, null=True)
    ekai = models.CharField(max_length=255, blank=True, null=True)
    ekai_nagar = models.CharField(max_length=255, blank=True, null=True)
    dayitv = models.CharField(max_length=255, blank=True, null=True)
    nagar = models.CharField(max_length=255, blank=True, null=True)
    prant = models.CharField(max_length=255, blank=True, null=True)
    vibhag = models.CharField(max_length=255, blank=True, null=True)
    jila = models.CharField(max_length=255, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'register_samautkarsh_registration'


class RegisterSamautkarshUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    mobile = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'register_samautkarsh_user'


class VibhagMaster(models.Model):
    vibhag_id = models.AutoField(primary_key=True)
    vibhag_name = models.CharField(max_length=255)
    vibhag_hindi = models.CharField(max_length=255)
    prant = models.ForeignKey(PrantMaster, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vibhag_master'


class Vividhsanghthan(models.Model):
    vividhsangathan_id = models.AutoField(primary_key=True)
    vividhsangathan_name = models.CharField(db_column='vividhSangathan_name', max_length=255)  # Field name made lowercase.
    referral_code = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vividhsanghthan'


class ZilaMaster(models.Model):
    jila_id = models.AutoField(primary_key=True)
    jila_name = models.CharField(max_length=255)
    jila_hindi = models.CharField(max_length=255)
    vibhag = models.ForeignKey(VibhagMaster, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zila_master'

class QRCode(models.Model):
    data = models.TextField()  # Stores scanned QR data
    scanned_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return f"{self.data[:50]} - {self.scanned_at}"


class ScannedPerson(models.Model):
    scanned_people_id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=255, null=True,unique=True)
    person_scanned=models.CharField(max_length=255,null=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        managed = False
        db_table = 'scanned_people'


class barcode_data(models.Model):
    barcode_id = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=15, null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)

class MandalMaster(models.Model):
    mandal_id = models.AutoField(primary_key=True)
    mandal_name = models.CharField(max_length=255)
    mandal_hindi = models.CharField(max_length=255)
    nagar = models.ForeignKey('NagarMaster', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mandal_master'

class BastiMaster(models.Model):
    basti_id = models.AutoField(primary_key=True)
    basti_name = models.CharField(max_length=255)
    basti_hindi = models.CharField(max_length=255)
    mandal = models.ForeignKey('MandalMaster', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basti_master'
    
class UpbastiMaster(models.Model):
    upbasti_id = models.AutoField(primary_key=True)
    upbasti_name = models.CharField(max_length=255)
    upbasti_hindi = models.CharField(max_length=255)
    basti = models.ForeignKey('BastiMaster', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'upbasti_master'


class EventForm(models.Model):
    new_register_id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    dob = models.DateField()
    phone = models.CharField(unique=True, max_length=255)
    address = models.CharField(max_length=255,blank=True, null=True)
    shreni  = models.CharField(max_length=255,blank=True, null=True)
    pincode  = models.CharField(max_length=255, blank=True, null=True)
    nagar = models.CharField(max_length=255,blank=True, null=True)
    ekai_upbasti  = models.CharField(max_length=255,blank=True, null=True)
    ekai  = models.CharField(max_length=255, blank=True, null=True)
    dayitv = models.CharField(max_length=255, blank=True, null=True)
    ekai_basti  = models.CharField(max_length=255, blank=True, null=True)
    ekai_milan = models.CharField(max_length=255, blank=True, null=True)
    ekai_sakha_milan = models.CharField(max_length=255, blank=True, null=True)
    sangh_shikshad = models.CharField(max_length=255, blank=True, null=True)
    prarambhik_varsh = models.CharField(max_length=255, blank=True, null=True)
    prathmik_varsh  = models.CharField(max_length=255, blank=True, null=True)
    pratham_varsh = models.CharField(max_length=255, blank=True, null=True)
    dwitiya_varsh = models.CharField(max_length=255, blank=True, null=True)
    tritiya_varsh = models.CharField(max_length=255, blank=True, null=True)
    reference_by= models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'event_register_form'

class ShikshanVisheshEvent(models.Model):
    registration = models.ForeignKey(RegisterSamautkarshRegistration,on_delete=models.CASCADE)
    shikshanvisheshevent_id = models.BigAutoField(primary_key=True)
    varg = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'shikshan_vishesh_event'

class ShikshanSamanyaEvent(models.Model):
    registration = models.ForeignKey(RegisterSamautkarshRegistration,on_delete=models.CASCADE)
    shikshansamanyaevent_id = models.BigAutoField(primary_key=True)
    varg = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'shikshan_samanya_event'

class GhoshEvent(models.Model):
    registration = models.ForeignKey(RegisterSamautkarshRegistration,on_delete=models.CASCADE)
    ghoshevent_id  = models.BigAutoField(primary_key=True)
    varg = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'ghosh_event'

class KaryakartaViskasVargPrathamSamanyaEvent(models.Model):
    registration = models.ForeignKey(RegisterSamautkarshRegistration,on_delete=models.CASCADE)
    karyakartaviskasvargprathamsamanyaevent_id  = models.BigAutoField(primary_key=True)
    varg = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'karyakarta_viskas_varg_pratham_samanya_event'


