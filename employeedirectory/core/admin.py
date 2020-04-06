from django.contrib import admin
from .models import Employee, EmergencyContact, Employment
from .models import ExternalSystem, ExternalUserAccount
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass

@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    pass

@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
    pass

@admin.register(ExternalSystem)
class ExternalSystemAdmin(admin.ModelAdmin):
    pass

@admin.register(ExternalUserAccount)
class ExternalUserAccountAdmin(admin.ModelAdmin):
    pass