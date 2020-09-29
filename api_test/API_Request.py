import requests
import pandas as pd
import json
from api_test import Request_Get_Token


class API_Request():
    # 接收请求数据
    def __init__(self, api_data):
        self.url = api_data['url']
        self.method = api_data['method']
        self.data = api_data['data']
        self.headers = api_data['headers']
        # print(api_data)

    # 发送请求返回结果
    def request(self):
        # 判断请求方式
        if self.method == "POST":
            # 判断请求头是否为空
            if pd.isnull(self.headers):
                # 判断请求携带数据是否为空
                if pd.isnull(self.data):
                    response = requests.post(url=self.url)
                else:
                    self.data = json.loads(self.data)
                    response = requests.post(url=self.url, data=self.data)
            else:
                token = Request_Get_Token.get_token()
                self.headers = json.loads(self.headers)
                self.headers['token'] = token
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
                token = Request_Get_Token.get_token()
                self.headers = json.loads(self.headers)
                self.headers['token'] = token
                if pd.isnull(self.data):
                    response = requests.get(url=self.url, headers=self.headers)
                else:
                    self.data = json.loads(self.data)
                    response = requests.get(url=self.url, params=self.data, headers=self.headers)
        # print(self.headers)
        return response
