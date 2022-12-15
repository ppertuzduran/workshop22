import requests
from init import env_url, glance_port, payload

image_parameter = '/v3/auth/tokens'

#GLANCE SERVICE

def glance_service(headers):
    images = requests.get(url=f"{env_url}:{glance_port}{image_parameter}", headers=headers).json().get('images')
    return images