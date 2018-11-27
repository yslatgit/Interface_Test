#coding:utf-8
from locust import HttpLocust,TaskSet,task
import subprocess
import json
import requests

class UserBehavior(TaskSet):

    def on_start(self):
        pass
    @task(1)
    def login(self):
        r = self.client.get("http://account.mofanghr.com/login.action?account=yangsongglin%40mofanghr.com&action=login&password=1234")
        # print(json.loads(r.content)["title"])

    @task(2)
    def list(self):
        headers = {"Cookie":"accountToken=yangsonglin@mofanghr.com|A2F2220D9F4B86EB283410E03A6C88D6"}
        r = self.client.post("http://crm.mofanghr.com/member/resume/list.json",headers=headers)


class MobileUserLocust(HttpLocust):
    weight = 3
    task_set = UserBehavior
    host = 'http://127.0.0.1'
    min_wait = 3000
    max_wait = 6000

#task(c参数)：模拟时此用例所占的比例
#host:locust服务在那台机器上