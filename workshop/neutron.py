import requests
from init import env_url, neutron_port, payload

network_parameter = '/v2.0/networks'
security_groups = '/v2.0/security-groups'

#NEUTRON SERVICE

def neutron_service(factor, headers):

    if factor == 'networks':
        neutron_response = requests.get(url=f"{env_url}:{neutron_port}/v2.0/networks", headers=headers).json().get('networks')

    if factor == 'security_groups':
        neutron_response = requests.get(url=f"{env_url}:{neutron_port}/v2.0/security-groups", headers=headers).json().get('security_groups')

    return neutron_response
