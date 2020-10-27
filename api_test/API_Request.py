import requests
import pandas as pd
import json


class API_Request():
    def __init__(self, api_data, token):
        self.url = api_data['url']
        self.method = api_data['method']
        self.data = api_data['data']
        self.json_data = api_data['json']
        self.headers = api_data['headers']
        self.token = token

    def request(self):
        if self.method == "POST":
            if pd.isnull(self.headers):
                if pd.isnull(self.data):
                    if pd.isnull(self.json_data):
                        response = requests.post(url=self.url)
                    else:
                        self.json_data = json.loads(self.json_data)
                        response = requests.post(url=self.url, json=self.json_data)
                else:
                    if pd.isnull(self.json_data):
                        self.data = json.loads(self.data)
                        response = requests.post(url=self.url, data=self.data)
                    else:
                        self.data = json.loads(self.data)
                        self.json_data = json.loads(self.json_data)
                        response = requests.post(url=self.url, data=self.data, json=self.json_data)
            else:
                self.headers = json.loads(self.headers)
                self.headers["token"] = self.token
                if pd.isnull(self.data):
                    if pd.isnull(self.json_data):
                        response = requests.post(url=self.url, headers=self.headers)
                    else:
                        self.json_data = json.loads(self.json_data)
                        response = requests.post(url=self.url, json=self.json_data, headers=self.headers)
                else:
                    if pd.isnull(self.json_data):
                        self.data = json.loads(self.data)
                        response = requests.post(url=self.url, data=self.data, headers=self.headers)
                    else:
                        self.data = json.loads(self.data)
                        self.json_data = json.loads(self.json_data)
                        response = requests.post(url=self.url, data=self.data, json=self.json_data, headers=self.headers)

        elif self.method == "GET":
            if pd.isnull(self.headers):
                if pd.isnull(self.data):
                    if pd.isnull(self.json_data):
                        response = requests.get(url=self.url)
                    else:
                        self.json_data = json.loads(self.json_data)
                        response = requests.get(url=self.url, json=self.json_data)
                else:
                    if pd.isnull(self.json_data):
                        self.data = json.loads(self.data)
                        response = requests.get(url=self.url, params=self.data)
                    else:
                        self.data = json.loads(self.data)
                        self.json_data = json.loads(self.json_data)
                        response = requests.get(url=self.url, params=self.data, json=self.json_data)
            else:
                self.headers = json.loads(self.headers)
                self.headers["token"] = self.token
                if pd.isnull(self.data):
                    if pd.isnull(self.json_data):
                        response = requests.get(url=self.url, headers=self.headers)
                    else:
                        self.json_data = json.loads(self.json_data)
                        response = requests.get(url=self.url, json=self.json_data, headers=self.headers)
                else:
                    if pd.isnull(self.json_data):
                        self.data = json.loads(self.data)
                        response = requests.get(url=self.url, params=self.data, headers=self.headers)
                    else:
                        self.data = json.loads(self.data)
                        self.json_data = json.loads(self.json_data)
                        response = requests.get(url=self.url, params=self.data, json=self.json_data,
                                                 headers=self.headers)
        return response
