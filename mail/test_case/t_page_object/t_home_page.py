# -*- coding:utf-8 -*-

from t_home_page_ui import THomePageUI


class HomePage(THomePageUI):
    """
    用户：教师
    页面对象(PO): HOME页面
    """
    def t_help_button(self):
        """
        点击【帮助】按钮
        """
        self.t_help_button_loc().click()
    def t_inform_button(self):
        """
        点击【通知】按钮
        """
        self.t_inform_button_loc().click()
    def t_hwToday_button(self):
        """
        点击【发布作业】按钮
        """
        self.t_hwToday_button_loc().click()
    def t_hwTrack_button(self):
        """
        点击【查评跟踪】按钮
        """
        self.t_hwTrack_button_loc().click()
    def t_hwFlies_button(self):
        """
        点击【作业档案】
        """
        self.t_hwFiles_button_loc().click()
    def t_hwAnalyse_button(self):
        """
        点击【作业分析】
        """
        self.t_hwAnalyse_button_loc().click()
    def t_infoCenter_button(self):
        """
        点击【通知中心】
        """
        self.t_infoCenter_button_loc().click()
    def t_userCenter_button(self):
        """
        点击【个人中心】
        """
        self.t_userCenter_button_loc().click()
