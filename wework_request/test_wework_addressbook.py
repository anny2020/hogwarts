import json

import requests
from jsonpath import jsonpath
import pytest
'''
企业微信接口测试
'''

class TestWework:
    #获取token
    session = requests.Session()
    def setup_method(self):
        param = {
            'corpid': "wwb30512cbc7b69f64",
            'corpsecret': "gIE-ILmAIFzsuY7JXOrpp9HN7x1g61msy9KkR4SvP3w"
        }

        r = self.session.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',params=param)
        print(r.json())
        self.session.params.update({"access_token": r.json()['access_token']})
        print(self.session.params.items())

    #添加人员
    def test_add_addmem(self):
        param = {
            "userid": "liqi",
            "name": "李七",
            "mobile": "13800000009",
            "department": [1],
            "email": "wangwu34@gzdev.com"
        }
        r = self.session.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",json=param)
        # print(r.json())
        assert r.json()['errcode'] == 0


    #获取人员信息
    def test_getmem(self):
        param = {
            'userid': "ZhengXiangHong"
        }
        r = self.session.get("https://qyapi.weixin.qq.com/cgi-bin/user/get",params = param)
        #
        assert r.json()['errcode'] == 0


    #更新人员信息
    def test_update_mem(self):
        # param = json.load(open("./zhangsan.json","rb"))
        param = {
            "userid": "liliu",
            "name": "李六test"
        }
        r = self.session.post("https://qyapi.weixin.qq.com/cgi-bin/user/update",json=param)
        # print(r.json())
        assert r.json()['errcode'] == 0



    #删除人员
    def test_del_mem(self):
        param = {"userid": "zhangsan"}
        r = self.session.get("https://qyapi.weixin.qq.com/cgi-bin/user/delete",params=param)
        # print(r.json())
        assert r.json()['errcode'] == 0


    #批量删除人员
    def test_del_mulmem(self):
        data = {
            "useridlist": ['lisi','wangwu']
        }
        r = self.session.post("https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete",json=data)
        # print(r.json())
        assert r.json()['errcode'] == 0


    #获取部门下的人员
    def test_get_deartment_mem(self):
        param = {
            'department_id': 1,
            'fetch_child': 0
        }
        r = self.session.get("https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",params = param)
        # print(r.json())
        assert r.json()['errcode'] == 0


    #获取部门下人员的信息
    def test_get_department_mem_info(self):
        param = {
            'department_id': 1,
            'fetch_child': 0
        }
        r = self.session.get("https://qyapi.weixin.qq.com/cgi-bin/user/list",params=param)
        # print(r.json())
        assert r.json()['errcode'] == 0
