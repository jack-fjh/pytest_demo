from test_project.common.singdriver import SingleDriver
from test_project.common.utils import util_demo
from test_project.business.user import UserAction
from test_project.business.topics import TopicAction
from test_project.business.viewmanage import ViewManage
from test_project.business.usercenter import UserCenter
from test_project.pom.topic_page import TopicPage
from test_project.pom.edittopic_page import EditTopicPage
import os,sys,pytest


userAction=UserAction()
topicAction=TopicAction()
viewManage=ViewManage()
driver=SingleDriver()
topicpage=TopicPage()
usercenter=UserCenter()
util=util_demo()
edittopicPage=EditTopicPage()

@pytest.fixture(scope='module',autouse=True)
def module():
    '''
    所有的操作依赖登录，所有的用例执行之前应该先登录
    :return:
    '''
    userAction.user_login('testuser1', '123456')
    yield
    driver.quit()


testdata=[
    ('share',None,'hello_alex','page','标题不能是空的。'),
    ('share','helloworld_alex',None,'page','内容不可为空'),
    (None,'helloworld_alex','hello_alex','alert','必须选择一个版块！')
]
test_title=['title is None','content isNone','tab is None']
@pytest.fixture(params=testdata,ids=test_title)
def data(request):
    '''
    request.param是固定写法
    :param request:
    :return:
    '''
    return request.param

def test_topic_ex(data):
    '''发布话题'''
    viewManage.go_to_home_page()
    viewManage.go_to_newtopic_page()

    nav_text=edittopicPage.breadcrumb_text
    assert  nav_text=='发布话题'
    topicAction.add_topic(data[0],data[1],data[2])

    if data[3]=='page':
        page_text=edittopicPage.error_msg_text
        assert page_text==data[4]
    elif data[3]=='alert':
        alert_text=edittopicPage.alert_msg_text
        assert  alert_text==data[4]