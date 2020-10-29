import pandas as pd
from API_Request import API_Request
import datetime
import Request_Get_Token

class Read_API_Data():
    # 读取所有接口数据
    def __init__(self):
        self.api_file = pd.read_excel("API.xls")
        self.api_num = self.api_file.shape[0]
        print("共有%d条数据" % self.api_num)
        self.log_file = open("log.txt", "a", encoding='utf-8')
        self.log_file.fruncate(0)
        self.log_file.write("-------------------------------------------------------------------" + "\n")
        self.log_file.write(str(datetime.datetime.now()) + "\n")
        self.log_file.write("-------------------------------------------------------------------" + "\n")
        self.log_file.write("共有%d条数据" % self.api_num + '\n')
        self.token = Request_Get_Token.get_token()

    def execute_api(self):
        # 对数据进行逐条发送请求并接收结果
        for list_num in range(1, self.api_num + 1):
            print("当前第%d条" % list_num)
            data = self.api_file['DATA'][list_num - 1]
            host = self.api_file['host'][list_num - 1]
            url = self.api_file['URL'][list_num - 1]
            method = self.api_file['Method'][list_num - 1]
            headers = self.api_file['Header'][list_num - 1]
            json_data = self.api_file['json'][list_num - 1]
            url = host + url
            api_data = {"url": url, "method": method, "data": data, "json": json_data, "headers": headers}
            api_request = API_Request(api_data, self.token)
            response = api_request.request()
            print(response.url)
            print(response.text)
            # print(api_data)
            # 记录日志，为非200响应数据
            if response.status_code != 200:
                self.log_file.write("第%d条" % list_num + "\n")
                self.log_file.write("URL:%s" % response.url + "\n")
                self.log_file.write("响应状态：%s" % response + "\n")
                self.log_file.write("-------------------------------------------------------------------" + "\n")
        self.log_file.close()
