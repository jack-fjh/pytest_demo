from selenium import webdriver
from test_project.common.singdriver import SingleDriver
from test_project.pom.user_page import UserPage

userpage=UserPage()

class UserAction(object):
    '''
    用户相关业务
    用户注册
    用户登录
    '''
    def __init__(self):
        #确保浏览器实例是有一个
        self.driver=SingleDriver()

    def user_login(self,username,password):
        self.driver.get('http://49.233.108.117:3000/signin')
        userpage.username_input.send_keys(username)
        self.driver.find_element_by_css_selector('#pass').send_keys(password)
        self.driver.find_element_by_css_selector('input[value="登录"]').click()

    def user_register(self,username,password,repasswd,email):
        self.driver.get('http://49.233.108.117:3000/signup')
        self.driver.find_element_by_css_selector('#loginname').send_keys(username)
        self.driver.find_element_by_css_selector('#pass').send_keys(password)
        self.driver.find_element_by_css_selector('#re_pass').send_keys(repasswd)
        self.driver.find_element_by_css_selector('#email').send_keys(email)
        self.driver.find_element_by_css_selector('input[class="span-primary"]').click()