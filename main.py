import init
from keystone import keystone_service
from glance import glance_service
from neutron import neutron_service
from nova import nova_service, nova_server_service

from flask import Flask, jsonify

app = Flask(__name__) #aplication

#LOGIN
@app.route('/mylogin', methods=['POST'])
def mylogin():
    return keystone_service()

headers = {'X-Auth-Token': keystone_service()}

#----------------------------------------------IMAGES-----------------------------------------------
@app.route('/myimages')
def myimages():
    return glance_service(headers=headers)

#ask image
images = glance_service(headers=headers)
for image in images:
    print(image["name"])

image_name = input("Image name: ")

#----------------------------------------------NETWORKS---------------------------------------------
@app.route('/mynetworks')
def mynetworks():
    return neutron_service(factor='networks', headers=headers)

#ask network
networks = neutron_service(factor='networks', headers=headers)
for network in networks:
    print(network["name"])

network_name = input("Network name: ")

#----------------------------------------------FLAVORS----------------------------------------------
@app.route('/myflavors')
def myflavors():
    return nova_service(factor='flavors', headers=headers)

#ask flavor
flavors = nova_service(factor='flavors', headers=headers)
for flavor in flavors:
    print(flavor["name"])

flavor_name = input("Flavor name: ")

#----------------------------------------------KEYPAIRS---------------------------------------------
@app.route('/mykey_pairs')
def mykeypairs():
    return nova_service(factor='key_pairs', headers=headers)

#ask keypair
key_pairs = nova_service(factor='key_pairs', headers=headers)
for key_pair in key_pairs:
    print(key_pair["keypair"]["name"])

keypair_name = input("Keypair name: ")

#----------------------------------------------SECURITY GROUPS---------------------------------------
@app.route('/mysecurity_groups')
def mysecurity_groups():
    return neutron_service(factor='security_groups', headers=headers)

#ask security group
security_groups = neutron_service(factor='security_groups', headers=headers)
for security_group in security_groups:
    print(security_group["name"])

security_group_name = input("Security Group name: ")


#----------------------------------------------GET SERVER SPECIFICATIONS-------------------------------

image_id = [image['id'] for image in images if image['name'] == image_name]
flavor_id = [flavor['id'] for flavor in flavors if flavor['name'] == flavor_name]
network_id = [network['id'] for network in networks if network['name'] == network_name]
key_name = [key_pair['keypair']['name'] for key_pair in key_pairs if key_pair['keypair']['name'] == keypair_name]
security_group_name = [security_group['id'] for security_group in security_groups if security_group['name'] == security_group_name]

server_specs = {
    "server": {
        "name": "pablo_pertuz",
        "imageRef": image_id[0],
        "flavorRef": flavor_id[0],
        "networks": [{"uuid": network_id[0]}],
        "key_name": key_name[0],
        "security_groups": [{"name": security_group_name[0]}]
    }
}

#----------------------------------------------CREATE SERVER--------------------------------------------
@app.route('/myserver')
def mycreate_server():
    return nova_server_service(headers=headers, server_specs=server_specs)

if __name__ == '__main__': #Initialize flask if main file
    app.run(debug=True, port=5000)