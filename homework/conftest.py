import pytest
import yaml

@pytest.fixture(scope="session")
def start():
    print("-----------开始计算------------")
    yield
    print("-----------计算结束-------------")

def pytest_addoption(parser, pluginmanager):
    mygroup = parser.getgroup("anny")
    mygroup.addoption("--env",default='test',dest='env',help='set your run env')

@pytest.fixture(scope="session")
def cmdoption(request):
    myenv =request.config.getoption("--env",default='test')
    if myenv == 'test':
        print("get test data")
        with open("datas/test/test.yml") as f:
            print(yaml.safe_load(f))
    elif myenv == "dev":
        print("get dev data")
        with open("datas/dev/dev.yml") as f:
            print(yaml.safe_load(f))
    elif myenv == "st":
        print("get st data")
        with open("datas/st/st.yml") as f:
            print(yaml.safe_load(f))
    return myenv

