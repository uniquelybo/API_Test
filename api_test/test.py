from api_test.Read_API_Data import Read_API_Data
import datetime

if __name__ == "__main__":
    print(datetime.datetime.now())
    read_api = Read_API_Data()
    read_api.execute_api()
