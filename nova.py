import requests
from init import env_url, nova_port, payload

flavor_parameter = '/flavors'
key_parameter = '/os-keypairs'
server_parameter = '/servers'

#NOVA SERVICE

def nova_service(factor, headers, server_specs):

    if factor == 'flavors':
        nova_response = requests.get(url=f"{env_url}:{nova_port}/flavors", headers=headers).json().get('flavors')

    if factor == 'key_pairs':
        nova_response = requests.get(url=f"{env_url}:{nova_port}/os-keypairs", headers=headers).json().get('keypairs')

    if factor == 'server':
        nova_response = requests.post(url=f"{env_url}:{nova_port}/servers", headers=headers, json=server_specs)

    return nova_response

