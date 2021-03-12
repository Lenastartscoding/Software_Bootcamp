
#!/usr/bin/env python

import requests
import json
import sys
from pathlib import Path
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint

here = Path(__file__).parent.absolute()
repository_root = (here / ".." ).resolve()
sys.path.insert(0, str(repository_root))

import env

inv_url = env.UMBRELLA.get("inv_url")
inv_token = env.UMBRELLA.get("inv_token")
en_url = env.UMBRELLA.get("en_url")
en_token = env.UMBRELLA.get("en_key")
#Use a domain of your choice
domain = "www.internetbadguys.com"
#domain = "google.com"

def getDomainStatus(domain):
    #Construct the API request to the Umbrella Investigate API to query for the status of the domain
    url = f"{inv_url}/domains/categorization/{domain}?showLabels"
    headers = {"Authorization": f'Bearer {inv_token}'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    domain_status = response.json()[domain]["status"]

    return domain_status


def getHistoryDomain(domain):

    #Add another call here, where you check the historical data for either the domain from the intro or your own domain and print it out in a readable format

    url_history = f"https://investigate.api.umbrella.com/whois/{domain}/history"
    headers = {"Accept": "application/json", "Authorization": f'Bearer {inv_token}'}
    response = requests.request("GET", url_history, headers=headers)
    data = response.json()

    return data

def addBlockedList(domain):
    url_history = f"https://s-platform.api.opendns.com/1.0/events?customerKey={en_token}"
    headers = {"Content-Type": "application/json"}
    data = {
        "alertTime": "2021-03-11T16:40:36.284Z",
        "deviceId": "ba6a59f4-e692-4724-ba36-c28132c761de",
        "deviceVersion": "13.7a",    
        "dstDomain": "{}".format(domain),
        "dstUrl": "{}".format(domain),
        "eventTime": "2021-03-11T16:40:36.284Z",
        "protocolVersion": "1.0a",
        "providerName": "Security Platform"
        }
    response = requests.request("POST", url_history, headers=headers, data=json.dumps(data))
    data_requete = response.json()

    return data_requete

def getDomainsList():

    url_history = f"https://s-platform.api.opendns.com/1.0/domains?customerKey={en_token}"
    headers = {"Content-Type": "application/json"}
    response = requests.request("GET", url_history, headers=headers)
    data_requete = response.json()

    return data_requete

def main():

    test_req = getDomainStatus(domain)
    test_req2 = getHistoryDomain(domain)
    
    if test_req == 1:
        print(f"The domain {domain} is found CLEAN")
    elif test_req == -1:
        print(f"The domain {domain} is found MALICIOUS")
        test_req4 = addBlockedList(domain)
    elif test_req == 0:
        print(f"The domain {domain} is found UNDEFINED")
        test_req4 = addBlockedList(domain)

    #pprint(test_req2)
    test_req3 = getDomainsList()
    pprint(test_req3)
    pprint(test_req4)

if __name__ == "__main__":
    # execute only if run as a script
    main()