# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 19:20:11 2024

@author: Pawan Kumar
"""

import requests
import pandas as pd

API_KEY = 'xZxLw8pnvBy3RGuztrrv'
STOCK_SYMBOL = 'AMZN'
BASE_URL = "https://data.nasdaq.com/api/v3/datasets/WIKI/" + STOCK_SYMBOL

result = requests.get(BASE_URL, 
                      params={'api_key':API_KEY})
json_results = result.json()
col_names = json_results['dataset']['column_names']
data = json_results['dataset']['data']

# Creating data frame from json data
df = pd.DataFrame(data,
                  columns=col_names)