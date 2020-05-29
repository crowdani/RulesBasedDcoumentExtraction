from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
import os, json, copy, re

import requests, time
import datetime as dt
from base64 import b64encode
from readConfigJSON import readJSON
from loggingHandler import logger
from ssl import SSLError
import requests
from requests.auth import HTTPBasicAuth
import json


def oauth():
    configuration, configuration_settings = readJSON()

    username = configuration_settings["function_id"]
    password = configuration_settings["password"]
    scopes = ['opendid']




    url = configuration_settings["ums_url"]
    credentials = ('%s:%s' % (
    configuration_settings["client_id"], configuration_settings["client_secret"]))
    encoded_credentials = b64encode(credentials.encode('ascii'))

    payload = 'username=' + username + '&password='+ password
    headers = {
      'Authorization': 'Basic %s' % encoded_credentials.decode("utf-8"),
      'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data = payload,verify=False)
    j = json.loads(response.text)
    return j['access_token']
    #return response.access_token
