import pytest
'''
pytest.fixture()配置执行先后顺序
定义func函数为函数级别的运行时，在下面定义测试用例的时候，需要用到函数执行时，只需要在测试用例的参数
中引用即可，例如test_01(func)，func为@pytest.fixture运行时配置

同时执行之前和执行之后是用yield隔开，yield之前的是每个用例运行前需要做的动作，yield之后是每个用例运行结束后
需要做的动作

scope='module'模块级别，同理yield也是对执行之前和执行之后的分割线，为了生效module，需要在func引入modu
scope='class'类执行之前和执行之后
scope='func'默认是函数级别
scope='session'所有文件执行前后操作
'''

@pytest.fixture()
def func(fix_session,modu,fix_class):
    '''
    func是最小单元
    :param modu:
    :param fix_class:
    :return:
    '''
    print('--fun set up--')
    yield
    print('--func teardown--')

@pytest.fixture(scope='module')
def modu():
    print('--module setup--')
    yield
    print('--module teardown--')

@pytest.fixture(scope='class')
def fix_class():
    print('--class setup--')
    yield
    print('--class teardown--')

@pytest.fixture(scope='session')
def fix_session():
    print('--set up session--')
    yield
    print('tear down session--')

class TestTmps(object):

    def test_01(self,func):
        print('--test 01--')


    def test_02(self,func):
        print('--test 02--')


class Testtm(object):
    def test_1(self,func):
        print('--test_1--')