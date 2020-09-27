import pymysql
import configparser


# class Mysql_Data():
    # @classmethod
def get_conn():
    cfg = configparser.ConfigParser()
    cfg.read("config/config.ini", encoding='utf-8')
    cfg.sections()
    cfg.options("mysql")
    config = {"host": cfg.get("mysql", "host"),
              "port": cfg.getint("mysql", "port"),
              "db": cfg.get("mysql", "db"),
              "user": cfg.get("mysql", "user"),
              "password": cfg.get("mysql", "password")
              }
    # print(config)
    conn = pymysql.connect(**config)
    # conn = pymysql.connect(host='localhost',port=3306,db='test',user='root',password='root')
    # return conn

    cur = conn.cursor()
    sql = "select * from user"
    # sql1 = "INSERT INTO user(name,age) VALUES (%s,%s)"
    # sql2 = "UPDATE user SET name=%s,age=%s WHERE id = %s;"
    # sql3 = "SELECT age,name FROM user WHERE id = %s;"
    cur.execute(sql)
    result = cur.fetchall()
    for res in result:
        print(res)
    conn.commit()
    cur.close()
    conn.close()


# if __name__ == "__main__":
get_conn()
