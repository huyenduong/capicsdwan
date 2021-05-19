#!/usr/bin/env python

import pprint
from vmanage.api.device import Device
from vmanage.api.central_policy import CentralPolicy
from login_vmanage import *
import os

# Return centralized policy list
def display_central_policy():
    auth, vmanage_host = login_vmanage()
    vmanage_central_policy = CentralPolicy(auth, vmanage_host)
    central_policy_list = vmanage_central_policy.get_central_policy()
    
    return central_policy_list

# Print out centralized policy
def print_central_policy():
    central_policy_list = display_central_policy()
    for central_policy in central_policy_list:
        if central_policy['isPolicyActivated']:
            state = "activated"
            print(f"Policy Name: {central_policy['policyName']} is activated. Policy ID: {central_policy['policyId']}")
        else:
            state = "inactive"
            print(
                f"Policy Name: {central_policy['policyName']} is inactive.Policy ID: {central_policy['policyId']} ")


# Find the current activated centralized policy
def activated_central_policy():
    central_policy_list = display_central_policy()
    for central_policy in central_policy_list:
        if central_policy['isPolicyActivated']:
            return central_policy['policyId']

if __name__ == "__main__":

    auth, vmanage_host = login_vmanage()
    vmanage_central_policy = CentralPolicy(auth, vmanage_host)
    vmanage_central_policy.activate_central_policy('segment-mcloud-2ways',
                                                   '20506b60-901d-449f-9e3c-819a0b596b56')
    #print_central_policy()
    print('Central Policy activation done!')
# vnendc lab: a85d2ced-d3d5-45f9-aea0-9d538e4dae06

