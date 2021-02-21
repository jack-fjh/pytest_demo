from test_project.business.user import UserAction
from test_project.business.topics import TopicAction
from test_project.business.viewmanage import ViewManage
userAction=UserAction()
topicAction=TopicAction()
viewManage=ViewManage()
def test_newtopic():
    '''
    测试创建话题
    :return:
    '''
    #1：用户登录成功
    userAction.user_login('testuser1','123456')
    #2:打开新建话题页面
    viewManage.go_to_newtopic_page()
    #3:创建新话题
    topicAction.add_topic('hello world','share','hello world')

    result_text=topicAction.tipmessage
    assert result_text == '内容不可为空'