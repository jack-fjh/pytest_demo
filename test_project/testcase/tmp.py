import os,sys


def setup_module():
    print('--setup module--')



class TestTmp(object):

    @classmethod
    def setup_class(cls):
        print('--setup class--')

    def setup(self):
        print('--set up--')

    def test_01(self):
        print('--test 01--')

    def test_02(self):
        print('--test 02--')

    def teardown(self):
        print('--teardown--')

    @classmethod
    def teardown_class(cls):
        print('--teardown class--')


def teardown_module():
    print('--teardown module--')
    dir=os.path.dirname(os.path.dirname(__file__))+'/pitcure'
    print(dir)

'''
执行命令： pytest -v -s  test_project/testcase/tmp.py
'''