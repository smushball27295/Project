# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 19:00:39 2021

@author: ramesh
"""
import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'GENDER':1, 'DISEASE GROUPING 1': 0, 'DISEASE GROUPING 2': 0, 'DISEASE GROUPING 3': 1})

print(r.json())

