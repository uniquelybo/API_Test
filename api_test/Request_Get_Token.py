import requests
import sys


def get_token():
    print("获取token.........")
    try:
        data = {"userid": "344267", "uttnum": "10238260", "uphone": "17363905237", "jiguangid": "13065ffa4eb9904bcf2", "facility": "0"}
        login_url = "http://192.168.16.226:8586/app/user/add"
        response = requests.post(url=login_url, data=data)
        # print(response.text)
        token = response.json()["user"]["token"]
        print(token)
        return token
    except Exception as ex:
        print("token获取失败。。。。", ex)
        sys.exit()

