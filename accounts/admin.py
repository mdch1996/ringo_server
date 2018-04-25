from django.contrib import admin
from .models import Device, Ring, Open


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('user', 'raspberry_pi_code', 'ip')


@admin.register(Ring)
class RingAdmin(admin.ModelAdmin):
    list_display = ('date_of_ring',)


@admin.register(Open)
class OpenAdmin(admin.ModelAdmin):
    list_display = ('date_of_open',)
