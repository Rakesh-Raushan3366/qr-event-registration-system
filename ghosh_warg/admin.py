from django.contrib import admin # type: ignore
from django.db import models
from .models import *

# Register your models here.

@admin.register(GhoshVargRegister)
class GhoshVargRegisterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GhoshVargRegister._meta.fields]
    search_fields = [field.name for field in GhoshVargRegister._meta.fields if isinstance(field, (models.CharField, models.TextField))]
    list_filter = ['nagar', 'dayitv', 'state', 'gender', 'ekai_mandal']
    ordering = ['name']
    readonly_fields = ['updated_on']