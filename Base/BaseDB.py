import pymysql
from readConfig import ReadConfig
from Base.BaseLog import MyLog

config_database = ReadConfig("DATABASE").readconfig()

class MyDB:
    global host,username,password,port,database,config
    host = config_database["host"]
    username = config_database["username"]
    password = config_database["password"]
    port = config_database["port"]
    database = config_database["database"]
    config = {
        'host':host,
        'user':username,
        'passwd':password,
        'port':port,
        'db':database
    }

    def __init__(self):
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.db = None
        self.cursor = None

    def connectDB(self):
        try:
            self.db = pymysql.connect(**config)
            self.cursor = self.db.cursor()
            print("Connect DB Successfully")
        except ConnectionError as ex:
            self.logger.error(str(ex))

    def closeDB(self):
        self.db.close()
        print("Database closed!")

    def executeSQL(self,sql):
        self.connectDB()
        try:
            #执行SQL
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            # results = self.cursor.fetchone()
            return results
        except:
            print('error:unable to fetch data!')


if __name__ == '__main__':
    """参照菜鸟教程数据库链接"""
    sql = 'select * from roles WHERE id = 1'
    r = MyDB().executeSQL(sql)
    print(r[0][0])