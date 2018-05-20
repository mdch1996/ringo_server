from requests import post, exceptions
from .models import Device


# global variable
raspberry_pi_address = 'http://192.168.1.100:8000'


def post_data(device_ip, data, url):
    # url_post = "http://" + device_ip + ":8000/api/switch/"
    url_post = raspberry_pi_address + url
    print('------url_post-----', url_post)
    try:
        response = post(url=url_post, data=data)
        print("-----response-------", response)
        return response
    except exceptions.RequestException:
        print("-------except--------")
        return
