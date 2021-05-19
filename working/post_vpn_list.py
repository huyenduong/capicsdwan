import requests
import get_request
import post_request
import pprint
from vmanage.api.device import Device
from vmanage.api.authentication import Authentication
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

vmanage_host = os.environ.get("VMANAGE_HOST")
vmanage_username = os.environ.get("VMANAGE_USERNAME")
vmanage_password = os.environ.get("VMANAGE_PASSWORD")

