# -*- coding:utf-8 -*-

from home_page_ui import HomePageUI


class HomePage(HomePageUI):
    """
    用户：学生
    页面对象(PO): HOME页面
    """
    def home_button(self):
        """
        点击"HOME"按钮
        """
        self.home_button_loc().click()

    def list_button(self):
        """
        点击"list"按钮
        """
        self.list_button_loc().click()
    def help_button(self):
        """
        点击【帮助】按钮
        """
        self.help_button_loc().click()
    def inform_button(self):
        """
        点击【通知】按钮
        """
        self.inform_button_loc().click()
    def hwToday_button(self):
        """
        点击【今日作业】按钮
        """
        self.hwToday_button_loc().click()
    def hwFlies_button(self):
        """
        点击【作业档案】
        """
        self.hwFiles_button_loc().click()
    def hwAnalyse_button(self):
        """
        点击【作业分析】
        """
        self.hwAnalyse_button_loc().click()
    def userCenter_button(self):
        """
        点击【个人中心】
        """
        self.userCenter_button_loc().click()
