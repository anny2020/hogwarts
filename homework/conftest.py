import pytest

@pytest.fixture(scope="session")
def start():
    print("-----------开始计算------------")
    yield
    print("-----------计算结束-------------")

