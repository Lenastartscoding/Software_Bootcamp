import requests
import json

network_url = "https://api.meraki.com/api/v1/organizations/549236/networks"
base_url = "https://api.meraki.com/api/v1"
global orga_id
global network_id
device_dict = dict()
device_list = list()
payload = None

headers = {
"Content-Type": "application/json",
"Accept": "application/json",
"X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

response_network = requests.request('GET', url = network_url , headers=headers, data = payload)
response_network_json = response_network.json()

for line in response_network_json:
    if line['name'] == 'DevNet Sandbox ALWAYS ON':
        network_id = line['id']

device_url = network_url + '/'+ network_id + '/devices'

#print(device_url)

response_device = requests.request('GET', url = device_url , headers=headers, data = payload)
response_device_json = response_device.json()

#print(response_device_json)
for line in response_device_json:
    if 'name' in line:
        print("Device name : "+line['name']+"; Mac: "+line['mac']+"; Serial: "+line['serial']+ "; Model: "+line['model'])
    else:
        print("Device name : No device Name"+"; Mac: "+line['mac']+"; Serial: "+line['serial']+ "; Model: "+line['model'])

