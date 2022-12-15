import requests
from init import env_url, keystone_port, payload

login_parameter = '/v3/auth/tokens'

#KEYSTONE SERVICE

def keystone_service():
    token = requests.post(url=f"{env_url}:{keystone_port}{login_parameter}", json=payload)
    token_id = token.json().get('token').get('id')
    return token_id