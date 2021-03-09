import requests

from env import config

s = requests.Session()
s.headers.update({
'Authorization': f"Bearer {config['WEBEX_ACCESS_TOKEN']}"
})

# Verify api access
WEBEX_BASE_URL = config['WEBEX_BASE_URL']

url = f"{WEBEX_BASE_URL}/v1/rooms"

resp = s.get(url)
resp_json = resp.json()
resp_items_list = resp_json["items"]

#print(resp_items_list)
for item in resp_items_list:
    if item["title"] == "CSAP Programmability CTF - Team 2":
        print(item["id"])