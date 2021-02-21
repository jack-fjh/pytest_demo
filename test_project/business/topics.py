from test_project.common.singdriver import SingleDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import sys


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
        self._tab_css='select[id="tab-value"]'
        self._title_css='textarea[id="title"]'
        self._content_css='div[class="CodeMirror-scroll"]'
        self._submit_css='input[value="提交"]'

    def __create_topic(self,title=None,tab=None,content=None):
        if tab is not None:
            select_tab=self.driver.find_element_by_css_selector(self._tab_css)
            Select(select_tab).select_by_value(tab)
        if title is not None:
            title_area=self.driver.find_element_by_css_selector(self._title_css)
            title_area.clear()
            title_area.send_keys(title)

        if content is not None:
            content_area=self.driver.find_element_by_css_selector(self._content_css)
            actions = ActionChains(self.driver)
            content_area.click()
            if sys.platform == 'win32':
                #用于windows系统
                actions.move_to_element(content_area).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
            else:
                #用于mac系统
                actions.move_to_element(content_area).key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND).send_keys(Keys.DELETE).perform()

            actions.move_to_element(content_area).send_keys(content).perform()

            submit=self.driver.find_element_by_css_selector(self._submit_css)
            submit.click()


    def add_topic(self,title,tab,content):
        # self.driver.find_element_by_css_selector('select[id="tab-value"]').click()
        # self.driver.find_element_by_css_selector(f'option[value="{tab}"]').click()
        # self.driver.find_element_by_css_selector('textarea[id="title"]').send_keys(title)
        # self.driver.find_element_by_css_selector('div[class="CodeMirror-scroll"]').send_keys(content)
        # self.driver.find_element_by_css_selector('input[class="span-primary submit_btn"]').click()
        self.__create_topic(title,tab,content)



    def edit_topic(self,new_title=None,new_tab=None,new_content=None):
        self.__create_topic(new_title,new_tab,new_content)

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
