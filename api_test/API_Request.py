import requests
import pandas as pd
import json

class API_Request():
    def __init__(self, api_data, token):
        self.url = api_data['url']
        self.method = api_data['method']
        self.data = api_data['data']
        self.headers = api_data['headers']
        self.token = token
        # print(api_data)

    def request(self):
        if self.method == "POST":
            if pd.isnull(self.headers):
                if pd.isnull(self.data):
                    response = requests.post(url=self.url)
                else:
                    self.data = json.loads(self.data)
                    response = requests.post(url=self.url, data=self.data)
            else:
                self.headers = json.loads(self.headers)
                self.headers['token'] = self.token
                if pd.isnull(self.data):
                    response = requests.post(url=self.url, headers=self.headers)
                else:
                    self.data = json.loads(self.data)
                    response = requests.post(url=self.url, data=self.data, headers=self.headers)

        elif self.method == "GET":
            if pd.isnull(self.headers):
                if pd.isnull(self.data):
                    response = requests.get(url=self.url)
                else:
                    self.data = json.loads(self.data)
                    response = requests.get(url=self.url, params=self.data)
            else:
                self.headers = json.loads(self.headers)
                self.headers['token'] = self.token
                if pd.isnull(self.data):
                    response = requests.get(url=self.url, headers=self.headers)
                else:
                    self.data = json.loads(self.data)
                    response = requests.get(url=self.url, params=self.data, headers=self.headers)
        # print(self.headers)
        return response
