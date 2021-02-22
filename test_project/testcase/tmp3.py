'''
autouse=True:可以自动加载
'''

import pytest

@pytest.fixture(autouse=True)
def func():
    print('--func set up--')
    yield
    print('--func teardown--')

@pytest.fixture(scope='class',autouse=True)
def fix_class():
    print('--class setup--')
    yield
    print('--class teardown--')


class TestTmps(object):

    def test_01(self):
        print('--test 01--')


    def test_02(self):
        print('--test 02--')