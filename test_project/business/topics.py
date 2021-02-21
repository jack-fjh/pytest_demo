from test_project.common.singdriver import SingleDriver

class TopicAction(object):
    '''
    话题相关操作
        发布话题
        修改话题
        删除话题
        回复话题
    '''

    def __init__(self):
        self.driver=SingleDriver()

    def add_topic(self,title,tab,content):
        self.driver.find_element_by_css_selector('select[id="tab-value"]').click()
        self.driver.find_element_by_css_selector(f'option[value="{tab}"]').click()
        self.driver.find_element_by_css_selector('textarea[id="title"]').send_keys(title)
        self.driver.find_element_by_css_selector('div[class="CodeMirror-scroll"]').send_keys(content)
        self.driver.find_element_by_css_selector('input[class="span-primary submit_btn"]').click()

    def edit_topic(self,title,tab,content):
        pass

    def del_topic(self,title):
        pass

    def reply_topic(self,title,reply_content):
        pass

    @property
    def tipmessage(self):
        '''
        发布话题页面 错误提示信息
        :return:
        '''
        return self.driver.find_element_by_css_selector('div[class="alert alert-error"]>strong').text
