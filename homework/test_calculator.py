import pytest
import yaml

datas = yaml.safe_load(open("calculator_data.yml"))

@pytest.mark.parametrize(('a'),datas)
class TestCal():

#加法
    # @pytest.mark.parametrize(('a'),datas)
    def test_add(self,a,start):
        print("-加法")
        print(f"{a['a']},{a['b']},{a['expe_add']}")
        assert (a['a'] + a['b']) == a['expe_add']

    #减法
    # @pytest.mark.parametrize(('a'),datas)
    def test_min(self,a):
        print("-减法")
        print(f"{a['a']},{a['b']},{a['expe_min']}")
        assert (a['a'] - a['b']) == a['expe_min']

    #乘法
    # @pytest.mark.parametrize(('a'),datas)
    def test_mul(self,a):
        print("-乘法")
        print(f"{a['a']},{a['b']},{a['expe_mul']}")
        assert (a['a'] * a['b']) == a['expe_mul']

    #除法
    # @pytest.mark.parametrize(('a'), datas)
    def test_div(self,a):
        print("-除法")
        print(f"{a['a']},{a['b']},{a['expe_div']}")
        assert (a['a'] / a['b']) == a['expe_div']
