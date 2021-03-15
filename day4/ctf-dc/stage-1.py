import requests
from env import config
import json
from utils.auth import IntersightAuth
from pprint import pprint

def getAlarmsInfo():
     # returns a list of all the organizations

    try:
        auth=IntersightAuth(secret_key_filename=config['INTERSIGHT_CERT'], api_key_id=config['INTERSIGHT_API_KEY'])
        BASE_URL='https://www.intersight.com/api/v1'
        url = f"{BASE_URL}/cond/Alarms"

        response = requests.get(url, auth=auth)

        return response.json()

    except:
        return "ERROR request NTP"

def getSummaryPhysicalInfra():
     # returns a list of all the organizations

    try:
        auth=IntersightAuth(secret_key_filename=config['INTERSIGHT_CERT'], api_key_id=config['INTERSIGHT_API_KEY'])
        BASE_URL='https://www.intersight.com/api/v1'
        url = f"{BASE_URL}/compute/PhysicalSummaries"

        response = requests.get(url, auth=auth)
        testData = response.json()
        responseSummary = []

        for data in testData["Results"]:

            mgmtModes = data["ManagementMode"]
            mgmtIPs = data["MgmtIpAddress"]
            names = data["Name"]
            cpus = data["NumCpus"]
            cpuCores = data["NumCpuCores"]
            powerStates = data["OperPowerState"]
            firmwares = data["Firmware"]
            models = data["Model"]
            serials = data["Moid"]

            dictTempo = {"mgmtModes": mgmtModes, "mgmtIPs": mgmtIPs, "names": names, "cpus": cpus, "cpuCores": cpuCores, "powerStates": powerStates, "firmwares": firmwares, "models": models, "serials": serials}
            responseSummary.append(dictTempo)

         #return response.json()
        return responseSummary

    except:
        return "ERROR request PhysicalSummaries"

def getVendorInfoComplianceHCL(vendorMoid):

    try:
        auth=IntersightAuth(secret_key_filename=config['INTERSIGHT_CERT'], api_key_id=config['INTERSIGHT_API_KEY'])
        BASE_URL='https://www.intersight.com/api/v1'
        url = f"{BASE_URL}/hcl/OperatingSystemVendors/{vendorMoid}"

        response = requests.get(url, auth=auth)

        return response.json()

    except:
        return "ERROR request VendorInfoComplianceHCL"

def getComplianceHCL():
     # returns a list of all the organizations

    try:
        auth=IntersightAuth(secret_key_filename=config['INTERSIGHT_CERT'], api_key_id=config['INTERSIGHT_API_KEY'])
        BASE_URL='https://www.intersight.com/api/v1'
        url = f"{BASE_URL}/hcl/OperatingSystems"

        response = requests.get(url, auth=auth)
        testData = response.json()
        responseSummary = []

        for data in testData["Results"]:

            version = data["Version"]
            vendorMoid = data["Vendor"]["Moid"]

            dictTempo = {"version": version, "vendorMoid": vendorMoid}
            responseSummary.append(dictTempo)

         #return response.json()
        return responseSummary

    except:
        return "ERROR request ComplianceHCL"

def getListNameKubernetesCluster():
     # returns a list of all the organizations

    try:
        auth=IntersightAuth(secret_key_filename=config['INTERSIGHT_CERT'], api_key_id=config['INTERSIGHT_API_KEY'])
        BASE_URL='https://www.intersight.com/api/v1'
        url = f"{BASE_URL}/kubernetes/ClusterProfiles"

        response = requests.get(url, auth=auth)
        testData = response.json()
        responseSummary = []

        for data in testData["Results"]:

            name = data["Name"]

            responseSummary.append(name)

         #return response.json()
        return responseSummary

    except:
        return "ERROR request ListNameKubernetesCluster"

def getCountKubernetesCluster():
     # returns a list of all the organizations

    try:
        responseSummary = getListNameKubernetesCluster()
        return len(responseSummary)

    except:
        return "ERROR request CountDeploymentKubernetesCluster"

def main():

    getAlarmsInfo()
    getSummaryPhysicalInfra()
    getComplianceHCL()
    getListNameKubernetesCluster()
    test_req = getCountKubernetesCluster()
    pprint(test_req, indent=6)

if __name__ == "__main__":
     # execute only if run as a script
    main()