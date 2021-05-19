#!/usr/bin/env python

import pprint
from vmanage.api.device import Device
from vmanage.api.central_policy import CentralPolicy
from login_vmanage import *
import os

# Print out centralized policy list
def display_central_policy():
    auth, vmanage_host = login_vmanage()
    vmanage_central_policy = CentralPolicy(auth, vmanage_host)
    central_policy_list = vmanage_central_policy.get_central_policy()
    
    return central_policy_list

# Find the current activated centralized policy
def activated_central_policy():
    central_policy_list = display_central_policy()
    for central_policy in central_policy_list:
        if central_policy['isPolicyActivated']:
            return central_policy['policyId']

if __name__ == "__main__":

    auth, vmanage_host = login_vmanage()
    vmanage_central_policy = CentralPolicy(auth, vmanage_host)
    activated_policy_id = activated_central_policy()
    if activated_policy_id:
        print(f"Deactivate central policy")
        vmanage_central_policy.deactivate_central_policy(activated_policy_id)
    else:
        print(f"There is no activated central policy.")
        exit
        
