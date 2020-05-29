'''
DISCLAIMER OF WARRANTIES.
 This code is sample code created by IBM Corporation. IBM grants you a
 nonexclusive copyright license to use this sample code example. This
 sample code is not part of any standard IBM product and is provided to you
 solely for the purpose of assisting you in the development of your
 applications. This example has not been thoroughly tested under all
 conditions. IBM, therefore cannot guarantee nor may you imply reliability,
 serviceability, or function of these programs. The code is provided "AS IS",
 without warranty of any kind. IBM shall not be liable for any damages
 arising out of your or any other parties use of the sample code, even if IBM
 has been advised of the possibility of such damages. If you do not agree with
 these terms, do not use the sample code.

 Copyright IBM Corp. 2019 All Rights Reserved.

 To run, see README.md
'''
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
'''
Execute Rules
'''

def executeRules():
    configuration, configuration_settings = readJSON()
    if (configuration):
        starttime = dt.datetime.now()
        dir_path = configuration_settings["output_directory_path"]
        count = 0
        errors = []
        output_results = []
        for subdir, dirs, files in os.walk(dir_path + "/json"):
            for file in files:
                file_path = os.path.join(subdir, file)
                new_file = copy.copy(file)

                file_split = new_file.rsplit(".")
                odm_file_value = str(file_split[0]) + "ODM.json"
                file_extension = str(file_split[-1].strip())

                old_file_name = new_file.replace("." + file_extension, '').strip()
                file_name = re.sub('[^A-Za-z0-9 _]+', ' ', old_file_name).strip() + "." + str(file_extension)
                new_file_path = os.path.join(subdir, file_name)
                print(new_file_path)
                f = open(new_file_path, "r")
                # deserializes into dict
                # and returns dict.
                y = json.loads(f.read())
                #json.append()
                odmData = {
                    '__DecisionID__': "myworld",
                    "document_in": y,
                    "metaData_inout": {
                        "dynamicParams": "string"
                      }
                }

                #var rex = new RegExp('Sensitivity":false', 'g');


               #var BACA_STRING_RESPONSE = JSON.stringify(res.data)
               #BACA_STRING_RESPONSE = BACA_STRING_RESPONSE.replace(rex, 'Sensitivity":0');


                odmJson = json.dumps(odmData)
                #print (odmJson)
                odmJson = odmJson.replace('"Sensitivity": false', '"Sensitivity":0')
                #odmpayload = {"__DecisionID__": "string","document_in": y, "metaData_inout": {"dynamicParams": "" }}
                authPayload= HTTPBasicAuth(configuration_settings["odmUser"], configuration_settings["odmPassword"])

                ODM_ProcessBacaDocument_ServiceURL = configuration_settings["odm_url"]
                #JsonPayload = odmpayload
                headers = {'content-type' : 'application/json'}
                #print(odmData)
                try:
                    response = requests.request("POST", ODM_ProcessBacaDocument_ServiceURL,headers=headers, data=odmJson, auth=authPayload, verify=False)
                    print(response.text)
                    jsonPayloadODM = json.loads(response.text)
                    fileOutPutPath =   configuration_settings["odm_output_directory_path"]+ "/" + odm_file_value
                    with open(fileOutPutPath, 'w') as outfile:
                        json.dump(jsonPayloadODM, outfile)
                    #return response
                except SSLError as sslerror:
                    logger.error("SSL error was thrown due to certificate failure, set ssl_verification to false in configuration config.json file.")
                    #dict_object.update({"error": str(sslerror)})
                    #errors.append(dict_object)
                    return False
                except Exception as ex:
                    #dict_object.update({"error": str(ex)})
                    #errors.append(dict_object)
                    #logger.error("An error occurred when trying to upload file " + file_path)
                    logger.debug(ex, exc_info=True)
                    pass


                f.close()
        return True
