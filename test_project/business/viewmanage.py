from test_project.common.singdriver import SingleDriver


class ViewManage(object):
    def __init__(self):
        self.driver=SingleDriver()


    def go_to_newtopic_page(self):
        '''
        从首页打开到新建话题页面
        :return:
        '''
        self.driver.find_element_by_css_selector('a[id="create_topic_btn"]').click()