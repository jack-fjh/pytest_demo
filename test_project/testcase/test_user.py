from test_project.common.singdriver import SingleDriver
driver=SingleDriver()
from test_project.business.user import UserAction
useraction=UserAction()

def test_login():
    useraction.user_login('testuser1','123456')
    #添加断言
    #1：登录成功应该跳转到首页
    current_url=driver.current_url
    assert  current_url=='http://49.233.108.117:3000/','应该跳转到首页'

    #2：用户名应该为testuser1
    username=driver.find_element_by_css_selector('span[class="user_name"]>a[class="dark"]').text
    assert username=='testuser1','登录用户名应该为testuser1'



def test_register():
    '''
    测试注册功能
    :return:
    '''
    useraction.user_register('testuser2','123456','123456','123456@qq.com')

    current_url=driver.current_url
    assert current_url=='http://49.233.108.117:3000/signup','应该跳转至注册界面'