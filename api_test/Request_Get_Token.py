import requests


def get_token():
    data = {"name": "123", "password": "123456"}
    login_url = "http://192.168.16.225:8788/api/gs/client/number/login/123/123456"
    response = requests.get(url=login_url, params=data)
    # print(response)
    token = response.json()['loginResponse']['token']
    # print(token)
    return token
