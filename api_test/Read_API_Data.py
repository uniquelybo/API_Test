import pandas as pd
from api_test.API_Request import API_Request


class Read_API_Data():
    def __init__(self):
        self.api_file = pd.read_excel("API.xls")
        self.api_num = self.api_file.shape[0]
        print("共有%d条数据" % self.api_num)
        self.log_file = open("log.txt", "a", encoding='utf-8')
        self.log_file.write("共有%d条数据" % self.api_num + '\n')

    def execute_api(self):
        for list_num in range(1, self.api_num + 1):
            print("当前第%d条" % list_num)
            data = self.api_file['DATA'][list_num - 1]
            host = self.api_file['host'][list_num - 1]
            url = self.api_file['URL'][list_num - 1]
            method = self.api_file['Method'][list_num - 1]
            headers = self.api_file['Header'][list_num - 1]
            url = host + url
            api_data = {"url": url, "method": method, "data": data, "headers": headers}
            api_request = API_Request(api_data)
            response = api_request.request()
            print(response.url)
            # print(response.text)
            # print(api_data)
            if response.status_code != 200:
                self.log_file.write("第%d条" % list_num + "\n")
                self.log_file.write("URL:%s" % response.url + "\n")
                self.log_file.write("响应状态：%s" % response + "\n")
                self.log_file.write("-------------------------------------------------------------------" + "\n")
        self.log_file.close()
