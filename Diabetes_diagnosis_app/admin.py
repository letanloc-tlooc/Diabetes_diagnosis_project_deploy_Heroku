# Register your models here.
from django.contrib import admin
from .models import Patient, HealthInfo, MedicalHistory

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'age', 'gender', 'phone_number')
    search_fields = ('full_name', 'phone_number')

@admin.register(HealthInfo)
class HealthInfoAdmin(admin.ModelAdmin):
    list_display = ('patient', 'checkup_date', 'blood_pressure', 'bmi', 'blood_glucose')
    search_fields = ('patient__full_name', 'checkup_date')
    list_filter = ('checkup_date', 'blood_pressure', 'bmi')

@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ('patient', 'result', 'accuracy')
    search_fields = ('patient__full_name', 'result')