"""
File I/O
'w' - Write-Only mode
'r' - Read-Only mode
'r+' - Read and Write mode
'a' - Append mode
"""
import json
from logging import exception

import requests
import pandas as pd
import _10genericmethods
api_url_path = 'api_url_file.csv'

class ExploreAPI(object):

    def __init__(self):
        self.get_df = _10genericmethods.GenericMethods()

    def get_all_user_details(self,filepath):
        df = self.get_df.get_data_frame(filepath)
        url = df['API URL'].values[0]
        response = requests.get(url)
        return response.json()

    def get_user_details_by_id(self,filepath, id):
        df = self.get_df.get_data_frame(filepath)

        df.set_index("API_Type", inplace=True)
        result = df.loc["GET_USER_BY_ID"]
        print(result)


        # url = df['API URL'].values[1]
        # response = requests.get(f'{url}{id}')
        url = f'{result[0]}{id}'
        response = requests.get(url)
        return response.json()


myobj = ExploreAPI()

path = 'apifile.csv'
userdetail = myobj.get_all_user_details(path)
print(userdetail)

givenuserdetail = myobj.get_user_details_by_id(api_url_path, 10)
print(givenuserdetail)

# path = 'apifile1.csv'
# data =  userdetail['data']
# df = pd.DataFrame(data)
# df.to_csv(path, index=False)

# df = _10genericmethods.GenericMethods().get_data_frame(api_url_path)
# df.set_index("API_Type", inplace = True)
# result = df.loc["GET_ALL_USERS"]
# print(result)

# result = df.iloc[0]
# print(result)

# print(df.keys())
# print(df.API_Type['GET_ALL_USERS'].values)


