import pytest

from py_code.calculator import Calculator


@pytest.fixture(scope='module')
def get_cal():
    print("计算开始  同目录下所有用例开始前执行一次")
    calc = Calculator()
    yield calc
    print("计算结束  同目录下所有用例结束执行一次")
