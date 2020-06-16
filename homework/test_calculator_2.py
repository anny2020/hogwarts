import pytest
import yaml
import selenium

datas = yaml.safe_load(open("calculator_data.yml"))

@pytest.mark.parametrize(('a'),datas)
class TestCal():

#加法
    # @pytest.mark.parametrize(('a'),datas)
    @pytest.mark.first
    def check_add(self,a,start,cmdoption):
        print("-加法")
        print(f"{a['a']},{a['b']},{a['expe_add']}")
        assert (a['a'] + a['b']) == a['expe_add']
        print(f"{cmdoption}")


    #乘法
    # @pytest.mark.parametrize(('a'),datas)
    @pytest.mark.third
    def check_mul(self,a):
        print("-乘法")
        print(f"{a['a']},{a['b']},{a['expe_mul']}")
        assert (a['a'] * a['b']) == a['expe_mul']

#减法
    # @pytest.mark.parametrize(('a'),datas)
    @pytest.mark.second
    def test_min(self,a):
        print("-减法")
        print(f"{a['a']},{a['b']},{a['expe_min']}")
        assert (a['a'] - a['b']) == a['expe_min']

    #除法
    # @pytest.mark.parametrize(('a'), datas)
    @pytest.mark.fourth
    def check_div(self,a):
        print("-除法")
        print(f"{a['a']},{a['b']},{a['expe_div']}")
        assert (a['a'] / a['b']) == a['expe_div']
