from django.contrib.auth.models import Group # type: ignore
from django.db import models # type: ignore

from django.contrib.auth.models import Group # type: ignore
from django.db import models # type: ignore

# create your models here.

# Admin Model
class Admin(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15, unique=True, null=True)
    role = models.CharField(max_length=255,null=True)
    role_level = models.CharField(max_length=255, null=True)
    role_sublevel = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.role.name})"
    

class RegisterSamautkarshUser(models.Model):
    mobile = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.mobile

    class Meta:
        managed = False
        db_table = 'register_samautkarsh_user'
    

class BarcodeScan(models.Model):
    barcode_scan_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    nagar = models.CharField(max_length=255)
    dayitv = models.CharField(max_length=255)
    qrcode = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default='pending')
    updated_at = models.DateTimeField(auto_now=True)
    Approving_person = models.CharField(max_length=255)
    #role_check_box = models.CharField(max_length=255, null=True)

    class Meta:
        managed = False
        db_table = 'barcode_scan'

    def __str__(self):
        return self.name


class DayitvMaster(models.Model):
    dayitv_id = models.AutoField(primary_key=True)
    dayitv_name = models.CharField(max_length=255)
    ekai = models.ForeignKey('EkaiMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dayitv_master'

    def __str__(self):
        return self.dayitv_name


class EkaiMaster(models.Model):
    ekai_id = models.AutoField(primary_key=True)
    ekai_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ekai_master'

    def __str__(self):
        return self.ekai_name

class NagarMaster(models.Model):
    nagar_id = models.AutoField(primary_key=True)
    nagar_name = models.CharField(max_length=255)
    nagar_hindi = models.TextField(max_length=255)
    jila = models.ForeignKey('ZilaMaster', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nagar_master'

    def __str__(self):
        return self.nagar_name

class PincodeMaster(models.Model):
    pincode_id = models.BigAutoField(primary_key=True)
    pincode = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    nagar = models.CharField(max_length=255, blank=True, null=True)
    nagar_hindi = models.CharField(max_length=255, blank=True, null=True)
    jila = models.ForeignKey('ZilaMaster',on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'pincode_master'

    def __str__(self):
        return self.nagar_hindi



class PrantMaster(models.Model):
    prant_id = models.AutoField(primary_key=True)
    prant_name = models.CharField(max_length=255)
    prant_hindi = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'prant_master'

    def __str__(self):
        return self.prant_hindi

class ProfessionMaster(models.Model):
    profession_id = models.AutoField(primary_key=True)
    profession_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'profession_master'

    def __str__(self):
        return self.profession_name

class RegisterSamautkarshOtp(models.Model):
    id = models.BigAutoField(primary_key=True)
    mobile = models.CharField(max_length=10)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'register_samautkarsh_otp'

    def __str__(self):
        return f"{self.mobile} - {self.otp}"


class RegisterSamautkarshRegistration(models.Model):
    register_id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    dob = models.DateField()
    phone_number = models.CharField(unique=True, max_length=255)
    gender = models.CharField(max_length=255)
    corress_address = models.TextField(blank=True, null=True)
    perman_address = models.TextField(blank=True, null=True)
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
   # other_dayitv_name = models.CharField(max_length=255, blank=True, null=True)
   
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'register_samautkarsh_registration'

    def __str__(self):
        return f"{self.name} - {self.phone_number}"


class VibhagMaster(models.Model):
    vibhag_id = models.AutoField(primary_key=True)
    vibhag_name = models.CharField(max_length=255)
    vibhag_hindi = models.CharField(max_length=255)
    prant = models.ForeignKey(PrantMaster, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vibhag_master'
    
    def __str__(self):
        return f"{self.vibhag_name} - {self.vibhag_hindi}"


class Vividhsanghthan(models.Model):
    vividhsangathan_id = models.AutoField(primary_key=True)
    vividhsangathan_name = models.CharField(db_column='vividhSangathan_name', max_length=255)  # Field name made lowercase.
    referral_code = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vividhsanghthan'

    def __str__(self):
        return f"{self.vividhsangathan_name} - {self.referral_code}"

class ZilaMaster(models.Model):
    jila_id = models.AutoField(primary_key=True)
    jila_name = models.CharField(max_length=255)
    jila_hindi = models.CharField(max_length=255)
    vibhag = models.ForeignKey(VibhagMaster, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zila_master'

    def __str__(self):
        return f"{self.jila_name} - {self.jila_hindi}"
        

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

# create your models here.

# Admin Model
class scanner(models.Model):
    scanner_id = models.AutoField(primary_key=True)
    scanner_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    #scanner_check_box=models.CharField(max_length=255,null=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    class Meta:
        managed = False
        db_table = 'scanr_approval_persons'

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