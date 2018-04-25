from rest_framework import serializers
from accounts.models import Device, Ring, Open


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('ip',)


class RingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ring
        fields = ('date_of_ring',)


class OpenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Open
        fields = ('date_of_open',)
