import pytest

from wework_request.api.tag import Tag
from wework_request.api.wework import Wework


class TestTag:

    @pytest.fixture(scope="session")
    def token(self):
        wework = Wework()
        yield wework.test_get_token()

    def setup(self):
        self.tag = Tag()

    def test_multi_data(self):
        data = [("dili" + str(x), x + 55, "dada" + str(x)) for x in range(10)]
        return data

    @pytest.mark.parametrize("tagname,tagid,update_tagname", test_multi_data("xx"))
    def test_all(self, tagname, tagid, update_tagname,token):
        # 创建tag
        try:
            assert self.tag.test_add_tag(tagname,tagid,token)['errmsg'] == 'created'
        except AssertionError as e:
            # 如果tagid重复，调用test_del_tag删除标签
            if 'invalid tagid' in e.__str__():
                self.tag.test_del_tag(tagid,token)
            # 如果tagname重复，要取出taglist，然后查找tagname对应的tagid取出，再调用test_del_tag
            if 'UserTag Name Already Exist' in e.__str__():
                # 获取taglist列表中的值
                taglist = self.tag.test_get_taglist(token)
                # 遍历列表中的值
                for i in taglist:
                    # 遍历字典键值对中的value，如果value中存在tagname,就取出其对应的tagid，这是要删除的tagid
                    for value in i.values():
                        if value == tagname:
                            del_tagid = i['tagid']
                self.tag.test_del_tag(del_tagid,token)
            # 断言添加接口的返回值
            assert self.tag.test_add_tag(tagname,tagid,token)['errmsg'] == 'created'
        # 查询成员
        assert self.tag.test_get_tag(tagid,token)['tagname'] == tagname

        # 更新成员
        assert self.tag.test_update_tag(tagid,update_tagname,token)['errmsg'] == "updated"
        assert self.tag.test_get_tag(tagid,token)['tagname'] == update_tagname

        # 删除成员
        assert self.tag.test_del_tag(tagid,token)['errmsg'] == 'deleted'
        assert self.tag.test_get_tag(tagid,token)['errcode'] == 40068

