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


def basicAuth():
    configuration, configuration_settings = readJSON()

    credentials = ('%s:%s' % (configuration_settings["function_id"], configuration_settings["password"]))
    encoded_credentials = b64encode(credentials.encode('ascii'))
    basicToken = 'Basic %s' % encoded_credentials.decode("utf-8")




    return basicToken
    #return response.access_token
