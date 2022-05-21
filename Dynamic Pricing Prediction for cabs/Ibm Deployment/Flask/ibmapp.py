# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 02:25:44 2021

@author: swetha m
"""

import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "U_RvQaIg609WWkob25zT3ThvNXjU_mGCbFUbxxmRCSwM"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": ['cab_type', 'name','product_id','source','destination'], "values": [input_feature]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/74e5be60-5848-40ff-a74e-4c1f17fe022f/predictions?version=2021-10-27', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())


