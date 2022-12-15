#GLOBAL PARAMETERS

env_url = "https://api-uat-001.ormuco.com"
keystone_port= '5000'
glance_port = '9292'
neutron_port = '9696'
nova_port = '8774/v2.1'

payload={
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "name": "workshop2022@utb.edu.co",
                    "domain": {
                        "name": "Default"
                    },
                    "password": "ILOVECLOUD2022"
                }
            }
        }
    }
}

