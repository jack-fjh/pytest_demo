from test_project.common.singdriver import SingleDriver
from test_project.common.utils import util_demo
from test_project.business.user import UserAction
from test_project.business.topics import TopicAction
from test_project.business.viewmanage import ViewManage
from test_project.business.usercenter import UserCenter
from test_project.pom.topic_page import TopicPage
import os,sys,pytest


userAction=UserAction()
topicAction=TopicAction()
viewManage=ViewManage()
driver=SingleDriver()
topicpage=TopicPage()
usercenter=UserCenter()
util=util_demo()

@pytest.fixture(scope='module',autouse=True)
def module():
    '''
    所有的操作依赖登录，所有的用例执行之前应该先登录
    :return:
    '''
    userAction.user_login('testuser1', '123456')
    yield
    driver.quit()

@pytest.fixture(scope='function',autouse=True)
def func():
    yield
    pic_name = util.get_screen_shoot
    screen_pic_name = util.get_png_file_name
    dir_pic = os.path.dirname(os.path.dirname(__file__)) + '/' + pic_name + '/' + screen_pic_name + '.png'
    driver.save_screenshot(dir_pic)


class TestTmp(object):
    def test_newtopic(self):
        '''
        测试创建话题
        :return:
        '''
        #1：用户登录成功
        # userAction.user_login('testuser1','123456')
        #2:打开新建话题页面
        viewManage.go_to_newtopic_page()
        #3:创建新话题
        topicAction.add_topic('share','hello world','hello world')

        #1。标题内容添加断言
        title_text=topicpage.title_text
        assert title_text == 'hello world'
        content_text=topicpage.content_text
        assert content_text == 'hello world'
        # result_text=topicAction.tipmessage
        # assert result_text == '内容不可为空'

    def test_updatetopic(self):
        '''
        更新话题
        :return:
        '''
        # viewManage.go_to_login_page()
        # userAction.user_login('testuser1','123456')
        viewManage.go_to_home_page()
        viewManage.go_to_user_center('testuser1')
        usercenter.click_current_create_topic_by_index(0)
        topicpage.click_edit_icon()
        topicAction.edit_topic(new_title='1111111',new_tab=None,new_content='222222222')
        title_text=topicpage.title_text
        assert title_text=='1111111'




