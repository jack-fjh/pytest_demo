from test_project.common.singdriver import SingleDriver


class UserPage(object):

    def __init__(self):
        self.driver=SingleDriver()

    @property
    def username_input(self):
        return self.driver.find_element_by_css_selector('#name')