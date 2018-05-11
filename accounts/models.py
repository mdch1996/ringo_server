from django.db import models
from django.conf import settings


class Device(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    raspberry_pi_code = models.PositiveIntegerField(unique=True, blank=True, null=True)
    ip = models.GenericIPAddressField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Device raspberry_pi {}'.format(self.raspberry_pi_code)


class Ring(models.Model):
    device = models.ForeignKey(Device, related_name='device_ring')
    created = models.DateTimeField(auto_now_add=True)
    date_of_ring = models.DateTimeField()

    class Meta:
        ordering = ('-created',)


class Switch(models.Model):
    device = models.ForeignKey(Device, related_name='device_switch')
    created = models.DateTimeField(auto_now_add=True)
    key = models.BooleanField()
    done = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)


class Sensor(models.Model):
    device = models.ForeignKey(Device, related_name='device_temp')
    created = models.DateTimeField(auto_now_add=True)
    temp = models.FloatField()

    class Meta:
        ordering = ('-created',)
