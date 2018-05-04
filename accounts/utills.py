from requests import post, exceptions
from .models import Device


# global variable
server_address = 'http://192.168.1.34:8000'


def post_data(device_ip, data):
    # url_post = "http://" + device_ip + ":8000/api/switch/"
    url_post = "http://192.168.1.100:8000/api/switch/"
    print('------url_post-----', url_post)
    try:
        r = post(url=url_post, data=data)
        return r.status_code
    except exceptions.RequestException:
        print("-------except--------")
        return
