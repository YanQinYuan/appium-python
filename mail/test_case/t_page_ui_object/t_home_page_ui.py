# -*- coding:utf-8 -*-

from base import Base


class THomePageUI(Base):
    """
    用户：教师
    页面UI对象(PUO): HOME 页面 UI
    """
    def t_home_button_loc(self):
        """
        定位到【Home】按钮
        :return: WebDriver对象
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': 'HOME',
            'android_by': 'wait_name',
            'android_value': 'HOME',
        })

    def t_list_button_loc(self):
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
    def t_help_button_loc(self):
        """
        定位到【帮助】按钮
        :return: WebDriver对象
        """
        return self.selector({
            'android_by': 'accessibility_id',
            'android_value': '帮助'
        })
    def t_inform_button_loc(self):
        """
        定位到【通知】按钮
        :return: WebDriver对象
        """
        return self.selector({
            'android_by': 'accessibility_id',
            'android_value': '通知'
        })
    def t_hwToday_button_loc(self):
        """
        定位到【今日作业】按钮
        :return: WebDriver对象
        """
        return self.selector({
            'android_by': 'accessibility_id',
            'android_value': '今日作业'
        })
    def t_hwTrack_button_loc(self):
        """
        定位到【查评跟踪】按钮
        :return: WebDriver对象
        """
        return self.selector({
            'android_by': 'accessibility_id',
            'android_value': '查评跟踪'
        })
    def t_hwFiles_button_loc(self):
        """
        定位到【作业档案】按钮
        :return: WebDriver对象
        """
        return self.selector({
            'android_by': 'accessibility_id',
            'android_value': '作业档案'
        })
    def t_hwAnalyse_button_loc(self):
        """
        定位到【作业分析】按钮
        :return: WebDriver对象
        """
        return self.selector({
            'android_by': 'accessibility_id',
            'android_value': '作业分析'
        })
    def t_infoCenter_button_loc(self):
        """
        定位到【通知中心】按钮
        :return: WebDriver对象
        """
        return self.selector({
            'android_by': 'accessibility_id',
            'android_value': '通知中心'
        })
    def t_userCenter_button_loc(self):
        """
        定位到【个人中心】按钮
        :return: WebDriver对象
        """
        return self.selector({
            'android_by': 'accessibility_id',
            'android_value': '个人中心'
        })
