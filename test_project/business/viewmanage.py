from test_project.common.singdriver import SingleDriver


class ViewManage(object):
    def __init__(self):
        self.driver=SingleDriver()

    def go_to_home_page(self):
        self.driver.get('http://49.233.108.117:3000/')

    def go_to_login_page(self):
        self.driver.get('http://49.233.108.117:3000/signin')

    def go_to_register_page(self):
        self.driver.get('http://49.233.108.117:3000/signup')

    def go_to_user_center(self,user):
        self.driver.get(f'http://49.233.108.117:3000/user/{user}')

    def go_to_newtopic_page(self):
        '''
        从首页打开到新建话题页面
        :return:
        '''
        self.driver.find_element_by_css_selector('a[id="create_topic_btn"]').click()