from selenium import webdriver

class SingleDriver(object):
    '''
    单例模式：统一管理浏览器的实例
    '''

    __instance=None
    def __new__(cls, *args, **kwargs):
        #new对象时会调用
        if cls.__instance is None:
            cls.__instance=webdriver.Chrome()
        #设置全局的等待时常
        cls.__instance.implicitly_wait(10)
        cls.__instance.maximize_window()
        return cls.__instance



if __name__ == '__main__':
    dr1=SingleDriver()
    dr2=SingleDriver()
    print(dr1==dr2,dr1,dr2)