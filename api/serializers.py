from rest_framework import serializers
from accounts import models


class RaspberryPiCodeSerializer(serializers.Serializer):
    raspberry_pi_code = serializers.IntegerField()


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Device
        fields = ('raspberry_pi_code', 'ip',)


class RingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ring
        fields = ('date_of_ring',)


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sensor
        fields = ('temp',)
