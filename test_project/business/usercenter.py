from test_project.pom.usercenter_page import UserCenterPage

class UserCenter(object):
    def __init__(self):
        self.user_center_page=UserCenterPage()


    def click_current_create_topic_by_index(self,index):
        '''
        点击个人中心最近创建的话题中的第几个话题
        :param index:
        :return:
        '''
        self.user_center_page.current_create_topic[index].click()

