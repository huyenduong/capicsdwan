#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3
import sys
from botocore.config import Config
# current boto3 version is 1.15.8
# config for sydney region
# this code will update vpc1 and vpc2 point to sdwan subnets
# author: Huyen Duong
# code quality: POC

htduong01 = Config(
    region_name='ap-southeast-2',
    signature_version='v4',
    retries={
        'max_attempts': 10,
        'mode': 'standard'
    }
)

session = boto3.session.Session(profile_name='htduong01')
ec2 = session.resource('ec2', config=htduong01)
client = session.client('ec2', config=htduong01)

# check if vrf egress has wrong sdwan route
def isSdwanRouteToIgw(routeTableId,rt):
    wrongSdwanRoute = True
    response = client.describe_route_tables(
        RouteTableIds=[
            routeTableId
        ]
    )
    routes = response['RouteTables'][0]['Routes']
    for route in routes:
        if route['DestinationCidrBlock'] == rt:
            if 'GatewayId' in route:
                wrongSdwanRoute = True
            else:
                wrongSdwanRoute = False
    return wrongSdwanRoute

def fixSdwanRoute(routeTableId, rt, TgwId, ):
    response = client.replace_route(
        RouteTableId=routeTableId,
        DestinationCidrBlock = rt,
        TransitGatewayId = TgwId,
    )

def main():

    vrf1_egress_rt_id = 'rtb-0cae81911284c445a'
    vrf2_egress_rt_id = 'rtb-051d92ae05466749a'
    TgwId = "tgw-0a95bf2769ea49d23"
    
    #list route entry
    vpn10_1 = '101.1.3.0/24'
    vpn10_2 = '102.1.3.0/24'
    vpn11_1 = '101.1.4.0/24'
    vpn11_2 = '102.1.4.0/24'
    
    # check and fix vrf1_egress RT
    if isSdwanRouteToIgw(vrf1_egress_rt_id, vpn10_1):
        fixSdwanRoute(vrf1_egress_rt_id, vpn10_1, TgwId)
        print(f"Route to {vpn10_1} is now corrected.")
    else:
        print(f"Route to {vpn10_1} is correct, no action needed.")

    if isSdwanRouteToIgw(vrf1_egress_rt_id, vpn10_2):
        fixSdwanRoute(vrf1_egress_rt_id, vpn10_2, TgwId)
        print(f"Route to {vpn10_2} is now corrected.")
    else:
        print(f"Route to {vpn10_2} is correct, no action needed.")

    # check and fix vrf2_egress RT
    if isSdwanRouteToIgw(vrf2_egress_rt_id, vpn11_1):
        fixSdwanRoute(vrf2_egress_rt_id, vpn11_1, TgwId)
        print(f"Route to {vpn11_1} is now corrected.")
    else:
        print(f"Route to {vpn11_1} is correct, no action needed.")

    if isSdwanRouteToIgw(vrf2_egress_rt_id, vpn11_2):
        fixSdwanRoute(vrf2_egress_rt_id, vpn11_2, TgwId)
        print(f"Route to {vpn11_2} is now corrected.")
    else:
        print(f"Route to {vpn11_2} is correct, no action needed.")

if __name__ == "__main__":
   main()
