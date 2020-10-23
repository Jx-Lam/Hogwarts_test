import pytest

# -------------同个py文件下调用fixture  test1-----------------------------
# @pytest.fixture(scope='module')
# def test1(get_cal):
#      b = '男'
#      print('传出了%s, 且同.py下所有用例开始前执行一次！！！' % b)
#      return b
#
#
# def test_a(test1):
#     print("test case a")
#
#
# class TestCase:
#     def test3(self, test1):
#         name = '男'
#         print('找到name')
#         assert test1 == name
#
#     def test4(self, test1):
#         sex = '男'
#         print('找到sex')
#         assert test1 == sex
#
#
# if __name__ == '__main__':
#     pytest.main(['-vs', 'test_fixture.py'])


# -------------跨py文件下调用conftest.py的feature-----------------------------
def test_a(get_cal):
    print("test case a")


class TestCase:
    def test3(self, get_cal):
        name = 'jie'
        print(f'test3--{name}')

    def test4(self, get_cal):
        sex = '男'
        print(f'test4--{sex}')


if __name__ == '__main__':
    pytest.main(['-vs', 'test_fixture.py'])