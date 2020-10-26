from django.contrib import admin
from .models import Employee, EmergencyContact, Employment
from .models import ExternalSystem, ExternalUserAccount

class EmergencyContactInline(admin.TabularInline):
    model = EmergencyContact

class EmploymentInline(admin.TabularInline):
    model = Employment

class ExternalUserAccountInline(admin.TabularInline):
    model = ExternalUserAccount

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [
        EmergencyContactInline,
        EmploymentInline,
        ExternalUserAccountInline,
        ]

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