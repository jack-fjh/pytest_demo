from test_project.common.singdriver import SingleDriver

class UserCenterPage(object):

    def __init__(self):
        self.driver=SingleDriver()

    @property
    def current_create_topic(self):
        return self.driver.find_elements_by_css_selector('div#content > div.panel:nth-child(2) a.topic_title')
