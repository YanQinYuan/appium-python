# -*- coding:utf-8 -*-

from base import Base


class HomePageUI(Base):
    """
    用户：学生
    页面UI对象(PUO): HOME 页面 UI
    """
    def home_button_loc(self):
        """
        定位到"HOME"按钮
        :return: WebDriver对象
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': 'HOME',
            'android_by': 'wait_name',
            'android_value': 'HOME',
        })

    def list_button_loc(self):
        """
        定位到"list"按钮
        :return: WebDriver对象
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': 'list',
            'android_by': 'wait_name',
            'android_value': 'list',
        })
    def help_button_loc(self):
        """
        定位到【帮助】按钮
        :return: WebDriver对象
        """
        return self.selector({
            'android_by': 'accessibility_id',
            'android_value': '帮助'
        })
    def inform_button_loc(self):
        """
        定位到【通知】按钮
        :return: WebDriver对象
        """
        return self.selector({
            'android_by': 'accessibility_id',
            'android_value': '通知'
        })
    def hwToday_button_loc(self):
        """
        定位到【今日作业】按钮
        :return: WebDriver对象
        """
        return self.selector({
            'android_by': 'accessibility_id',
            'android_value': '今日作业'
        })
    def hwFiles_button_loc(self):
        """
        定位到【作业档案】按钮
        :return: WebDriver对象
        """
        return self.selector({
            'android_by': 'accessibility_id',
            'android_value': '作业档案'
        })
    def hwAnalyse_button_loc(self):
        """
        定位到【作业分析】按钮
        :return: WebDriver对象
        """
        return self.selector({
            'android_by': 'accessibility_id',
            'android_value': '作业分析'
        })
    def userCenter_button_loc(self):
        """
        定位到【个人中心】按钮
        :return: WebDriver对象
        """
        return self.selector({
            'android_by': 'accessibility_id',
            'android_value': '个人中心'
        })
