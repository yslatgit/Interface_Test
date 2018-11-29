import os
import unittest
import paramunittest
from Base.BaseLog import MyLog
from Base.BaseHttp import Http
from Base.BaseData import GetUrl,GetData

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))

url_path = PATH("../../testData/interfaceURL.xml")
data_path = PATH("../../testData/userCase.xlsx")

data = GetData(data_path,'wholehotJob').get_data()
url = GetUrl(url_path,'wholehotJob').get_url()

@paramunittest.parametrized(*data)
class WholeHotJob(unittest.TestCase):
    def setParameters(self,case_name,method,jobFunc,cityCode,version,msg):
        self.case_name = str(case_name)
        self.method = str(method)
        self.jobFunc = str(jobFunc)
        self.cityCode = str(cityCode).split(".")[0]
        self.version = str(version)
        self.msg = str(msg)

    def description(self):
        return self.case_name

    def setUp(self):
        self.req = Http("app")
        self.url = url
        self.result = None
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        print(self.case_name + "测试开始前准备")
        self.logger.info("*"*50)
        self.logger.info(self.case_name + "测试")

    def testwholehotjob(self):
        #拼接完整的请求接口
        self.req.set_url(self.url)
        #设置header
        header = {"cookie":""}
        self.req.set_headers(header)
        #设置params
        param = {'params':'{"appkey":"%s","jobID":"%s"}'%(self.jobFunc,self.cityCode)}
        self.req.set_params(param)
        #打印发送请求的方法
        self.logger.info("请求方法为 " + self.method)
        #请求
        self.result = self.req.get()
        #print(self.req.get().url)

    def tearDown(self):
        self.req = None
        self.logger.info("断言结果是 " + "%s" %self.checkResult())
        print("测试结束，结果已输出到Log")

    def checkResult(self):
        try:
            self.result = self.result.json()
            self.assertEqual(self.result["code"],200)
            return "Pass" + "---->" + self.msg
        except Exception as ex:
            self.logger.error(str(ex))
            return "False" + "--原因-->" + self.msg









if __name__ == '__main__':
    unittest.main()