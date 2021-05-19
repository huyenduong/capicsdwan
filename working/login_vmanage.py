
from vmanage.api.authentication import Authentication
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

vmanage_host = os.environ.get("VMANAGE_HOST")
vmanage_username = os.environ.get("VMANAGE_USERNAME")
vmanage_password = os.environ.get("VMANAGE_PASSWORD")

def login_vmanage():
    vmanage = vmanage_host
    auth = Authentication(host=vmanage_host, user=vmanage_username,
                      password=vmanage_password).login()
    return auth, vmanage
