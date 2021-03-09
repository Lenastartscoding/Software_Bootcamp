import requests

from env import config

WEBEX_BASE_URL = config['WEBEX_BASE_URL']

url = f"{WEBEX_BASE_URL}/v1/rooms"

payload = {"title":"Test Room"}

headers = {
"Accept": "application/json",
'Authorization': f"Bearer {config['WEBEX_ACCESS_TOKEN']}"
}

listEmail = ["mneiding@cisco.com","frewagne@cisco.com"]
#listEmail = ["alrival@cisco.com","mickober@cisco.com"]

response = requests.request('POST', url, headers=headers, data = payload)
json_response = response.json()

#print(response.status_code)
#print(json_response)

roomId = json_response['id']
print(roomId)

for i in listEmail:
    url = f"{WEBEX_BASE_URL}/v1/memberships"
    payload_membership = {"roomId":roomId, "personEmail":i}
    response = requests.request('POST', url, headers=headers, data = payload_membership)
    json_response = response.json()

#print(response.status_code)

url = f"{WEBEX_BASE_URL}/v1/messages"
payload_message = {"roomId":roomId,"text":"When you read this, Lena is celebrating python code!"}

response = requests.request('POST', url, headers=headers, data = payload_message)
json_response = response.json()