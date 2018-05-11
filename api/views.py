from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

from accounts.models import Device
from . import serializers


@api_view(['PATCH'])
def add_ip(request):
    raspberry_pi_code_serializer = serializers.RaspberryPiCodeSerializer(data=request.data)
    if raspberry_pi_code_serializer.is_valid():
        raspberry_pi_code = raspberry_pi_code_serializer.data.get("raspberry_pi_code")

        try:
            device = Device.objects.get(raspberry_pi_code__exact=raspberry_pi_code)
            device_serializer = serializers.DeviceSerializer(instance=device, data=request.data)

            if device_serializer.is_valid():
                device_serializer.save()
                print('----ip_device----', device, request.data['ip'])
                return Response(device_serializer.data, status=status.HTTP_201_CREATED)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(device_serializer.errors)
    return Response(raspberry_pi_code_serializer.errors)


@api_view(['POST'])
def add_ring(request):
    raspberry_pi_code_serializer = serializers.RaspberryPiCodeSerializer(data=request.data)
    if raspberry_pi_code_serializer.is_valid():
        raspberry_pi_code = raspberry_pi_code_serializer.data.get("raspberry_pi_code")

        try:
            device = Device.objects.get(raspberry_pi_code__exact=raspberry_pi_code)
            ring_serializer = serializers.RingSerializer(data=request.data)

            # ------get raspberry_pi's ip by my own server---------
            # new_ip = request.data['ip']
            # try:
            #     # case server 200.000.02.001
            #     client_address = request.META['HTTP_X_FORWARDED_FOR']
            #     print("request.META['HTTP_X_FORWARDED_FOR']", client_address)
            # except:
            #     # case localhost ou 127.0.0.1
            #     client_address = request.META['REMOTE_ADDR']
            #     print("request.META['REMOTE_ADDR']", client_address)
            #
            # if device.ip != new_ip:
            #     device.ip = new_ip
            #     device.save()

            if ring_serializer.is_valid():
                ring_serializer.save(device=device)
                return Response(ring_serializer.data, status=status.HTTP_201_CREATED)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(ring_serializer.errors)

    return Response(raspberry_pi_code_serializer.errors)


@api_view(['POST'])
def add_sensor(request):
    raspberry_pi_code_serializer = serializers.RaspberryPiCodeSerializer(data=request.data)
    if raspberry_pi_code_serializer.is_valid():
        raspberry_pi_code = raspberry_pi_code_serializer.data.get("raspberry_pi_code")

        try:
            device = Device.objects.get(raspberry_pi_code__exact=raspberry_pi_code)
            sensor_serializer = serializers.SensorSerializer(data=request.data)

            if sensor_serializer.is_valid():
                sensor_serializer.save(device=device)
                return Response(sensor_serializer.data, status=status.HTTP_201_CREATED)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(sensor_serializer.errors)

    return Response(raspberry_pi_code_serializer.errors)

