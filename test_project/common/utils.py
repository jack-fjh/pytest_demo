import time
import os
class util_demo(object):

    def __init__(self):
        pass

    @property
    def get_screen_shoot(self):
        '''
        如果项目根目录下不存在screenshoots目录，那么就创建一个
        :return:screenshoots的绝对路径
        '''
        dir_name=os.path.dirname(os.path.dirname(__file__))
        dir_list=os.listdir(dir_name)
        if 'pitcure' not in dir_list:
            os.mkdir(dir_name+'/pitcure')
            print(os.listdir(dir_name))
        return 'pitcure'

    @property
    def get_png_file_name(self):
        '''
        @todo  返回文件名  年_月_日_时_分_秒
        :return:
        '''
        return time.strftime('%Y_%m_%d_%H_%M_%S')


if __name__ == '__main__':
    util=util_demo()
    pic_dir=util.get_screen_shoot