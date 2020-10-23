# -*- coding: utf-8 -*-

import pytest
from py_code.calculator import Calculator


# # 跨.py模块调用conftest.py的feature
# def test_a(test1):
#     print("test case a")


def test1():
    b = 'function:test1 无调用feature'
    return b


class TestCalc:

    # def setup_class(self):
    #     print("计算开始")
    #     self.calc = Calculator()
    #
    # def teardown_class(self):
    #     print("计算结束")

    # 加法用例
    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 2], [100, 100, 200], [0.1, 0.2, 0.3], [-1, -1, -2],
        [1, 0, 1]
    ], ids=['int_case', 'bignum_case', 'float_case', 'minus_case', 'zero_case'])
    @pytest.mark.run(order=1)
    def test_add(self, get_cal, a, b, expect):
        result = get_cal.add(a, b)
        assert round(result, 2) == expect

    # 减法用例
    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 0], [100, 100, 0], [0.1, 0.2, -0.1], [-1.1, -1, -0.1],
        [1, 0, 1]
    ], ids=['int_case', 'bignum_case', 'float_case', 'minus_case', 'zero_case'])
    @pytest.mark.run(order=4)
    def test_sub(self, get_cal, a, b, expect):
        result = get_cal.sub(a, b)
        assert round(result, 2) == expect

    # 乘法用例
    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 1], [100, 100, 10000], [0.1, 0.2, 0.02], [-1.1, -1, 1.1],
        [1, 0, 0], [0, 0.1, 0]
    ], ids=['int_case', 'bignum_case', 'float_case', 'minus_case', 'zero_case_01', 'zero_case_02'])
    @pytest.mark.run(order=3)
    def test_mul(self, get_cal, a, b, expect):
        result = get_cal.mul(a, b)
        assert round(result, 2) == expect

    # 除法用例
    @pytest.mark.parametrize('a,b,expect', [
        [1, 0, 0], [0.1, 0.1, 1], [0, 0.2, 0], [1, 3, 0.33], [1, 99, 0.01]
    ])
    @pytest.mark.run(order=2)
    def test_div(self, get_cal, a, b, expect):
        if b == 0:
            with pytest.raises(ZeroDivisionError):
                get_cal.div(a, b)
        else:
            result = get_cal.div(a, b)
            print(result)
            assert round(result, 2) == expect

    # ---------------------------------------------分界线---------------------------------------------

    # python 浮点数（小数）在计算机中实际是以二进制存储的，并不精确。
    # 比如0.1是十进制，转换为二进制后就是一个无限循环的数。decial库来提升精度。
    @pytest.mark.parametrize('a,b,expect', [
        [0.1, 0.1, 0.2], [0.1, 0.2, 0.3]
    ])
    def test_add_float(self, get_cal, a, b, expect):
        result = get_cal.add1(a, b)
        print(result)
        assert round(result, 2) == expect

    # 除零错误
    @pytest.mark.parametrize('a,b', [
        [0.1, 0], [10, 0]
    ])
    def test_div_zero(self, get_cal, a, b):
        with pytest.raises(ZeroDivisionError):
            get_cal.div(a, b)

    # 笛卡尔积
    @pytest.mark.parametrize('a', [1, 2, 3])
    @pytest.mark.parametrize('b', [4, 5, 6])
    @pytest.mark.parametrize('c', [7, 8, 9])
    def test_cartesian_product(self, get_cal, a, b, c):
        print(a, b, c)
