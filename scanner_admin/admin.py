from django.contrib import admin
from .models import *

# Register your models here.

# @admin.register(Role)
# class RoleAdmin(admin.ModelAdmin):
#     list_display = ['id','name', 'parent_role']

@admin.register(scanner)
class scannerAdmin(admin.ModelAdmin):
    list_display = ['scanner_id','scanner_name', 'phone_number', 'role']
