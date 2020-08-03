from random import randint

import pytest
import requests


class TestTag:
    session = requests.Session()
    def setup_method(self):
        param = {
            'corpid': "wwb30512cbc7b69f64",
            'corpsecret': "gIE-ILmAIFzsuY7JXOrpp9HN7x1g61msy9KkR4SvP3w"
        }

        r = self.session.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=param)
        self.session.params.update({"access_token": r.json()['access_token']})

    def test_add_tag(self,tagname,tagid):
        param = {
            "tagname": tagname,
            "tagid": tagid
        }
        r = self.session.post('https://qyapi.weixin.qq.com/cgi-bin/tag/create',json=param)
        return r.json()

    def test_update_tag(self,tagid,tagname):
        param = {
            "tagid": tagid,
            "tagname": tagname
        }
        r = self.session.post('https://qyapi.weixin.qq.com/cgi-bin/tag/update', json=param)
        return r.json()

    def test_del_tag(self,tagid):
        param = {
            "tagid": tagid
        }
        r = self.session.get("https://qyapi.weixin.qq.com/cgi-bin/tag/delete",params=param)
        return r.json()


    def test_get_tag(self,tagid):
        param = {
            "tagid": tagid
        }
        r = self.session.get("https://qyapi.weixin.qq.com/cgi-bin/tag/get", params=param)
        return r.json()

    def test_get_taglist(self):
        r = self.session.get("https://qyapi.weixin.qq.com/cgi-bin/tag/list")
        return r.json()['taglist']


    def test_multi_data(self):
        data = [("dili"+str(x),x+55,"dada"+str(x))for x in range(10)]
        return data

    @pytest.mark.parametrize("tagname,tagid,update_tagname",test_multi_data("xx"))
    def test_all(self,tagname,tagid,update_tagname):
        # 创建tag
        try:
            assert self.test_add_tag(tagname,tagid)['errmsg'] == 'created'
        except AssertionError as e:
            #如果tagid重复，调用test_del_tag删除标签
            if 'invalid tagid' in e.__str__():
                self.test_del_tag(tagid)
            #如果tagname重复，要取出taglist，然后查找tagname对应的tagid取出，再调用test_del_tag
            if 'UserTag Name Already Exist' in e.__str__():
                #获取taglist列表中的值
                taglist = self.test_get_taglist()
                #遍历列表中的值
                for i in taglist:
                    #遍历字典键值对中的value，如果value中存在tagname,就取出其对应的tagid，这是要删除的tagid
                    for value in i.values():
                        if value == tagname:
                            del_tagid = i['tagid']
                self.test_del_tag(del_tagid)
            #断言添加接口的返回值
            assert self.test_add_tag(tagname,tagid)['errmsg'] == 'created'
        # 查询成员
        assert self.test_get_tag(tagid)['tagname'] == tagname

        #更新成员
        assert self.test_update_tag(tagid,update_tagname)['errmsg'] == "updated"
        assert self.test_get_tag(tagid)['tagname'] == update_tagname
        #
        #删除成员
        assert self.test_del_tag(tagid)['errmsg'] == 'deleted'
        assert self.test_get_tag(tagid)['errcode'] == 40068

