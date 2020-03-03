from django.contrib import admin
from .models import (
    CateForDesign, Design,
    CateForCon, Consultation,
    Marketing,
    Implementation
)

LIST_DISPLAY_INFO = ['id','name', 'status', 'desc', 'price']

@admin.register(CateForDesign)
class CateForDesignAdmi(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(CateForCon)
class CateForConAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Consultation)
class ConAdmin(admin.ModelAdmin):
    list_display = ['id','category', 'name', 'status', 'desc', 'price']

@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):
    list_display = ['id','category', 'name', 'status', 'desc', 'price']

@admin.register(Marketing)
class MarketingAdmin(admin.ModelAdmin):
    list_display = LIST_DISPLAY_INFO

@admin.register(Implementation)
class ImpAdmin(admin.ModelAdmin):
    list_display = LIST_DISPLAY_INFO
