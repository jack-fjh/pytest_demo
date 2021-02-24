import pytest

testdata=[
    ('helloworld_alex','None','hello_alex'),
    ('None','share','hello_alex'),
    ('helloworld_alex','share','None'),
]
@pytest.fixture(params=testdata,ids=['tab is None','title is None','content isNone'])
def a(request):
    '''
    添加了ids，相当于对数据做了简要的说明，测试点是什么
    数据传参的时候主要是作为不同数据的不同解释
    :param request:
    :return:
    '''
    return request.param

def test_01(a):
    print(f'===={a}====')

