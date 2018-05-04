from rest_framework import serializers
from accounts.models import Device, Ring, Switch


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('ip',)


class RingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ring
        fields = ('date_of_ring',)
