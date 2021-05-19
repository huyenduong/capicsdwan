#!/usr/bin/env python

import pprint
from vmanage.api.device import Device
from vmanage.api.central_policy import CentralPolicy
from login_vmanage import *
import os

def display_devices():
    auth, vmanage_host = login_vmanage()
    vmanage_device = Device(auth, vmanage_host)
    device_config_list = vmanage_device.get_device_config_list('all')

    for device in device_config_list:
        try:
            print(device['host-name'])
        except KeyError:
            pass

# Return the list of centralized policy
def list_central_policy():
    auth, vmanage_host = login_vmanage()
    vmanage_central_policy = CentralPolicy(auth, vmanage_host)
    central_policy_list = vmanage_central_policy.get_central_policy()
    return central_policy_list

# Print out centralized policy list
def display_central_policy():
    auth, vmanage_host = login_vmanage()
    vmanage_central_policy = CentralPolicy(auth, vmanage_host)
    central_policy_list = vmanage_central_policy.get_central_policy()
    
    for central_policy in central_policy_list:
        if central_policy['isPolicyActivated']:
            state = "activated"
            print(f"Policy Name: {central_policy['policyName']}. Stattus: activated. ID: {central_policy['policyId']}")
        else:
            state = "inactive"
            print(
                f"Policy Name: {central_policy['policyName']}. Status: inactive.ID: {central_policy['policyId']} ")

if __name__ == "__main__":

    print("Devices in SDWAN Lab:")
    devices = display_devices()

    print("Cetralized Policy:")
    central_policy = display_central_policy()
    
