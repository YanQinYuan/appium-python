# -*- coding:utf-8 -*-

from t_home_page_ui import THomePageUI


class HomePage(THomePageUI):
    """
    用户：教师
    页面对象(PO): HOME页面
    """
    def t_hwtitle_input(self, text):
        """
        输入作业标题
        """
        self.t_hwtitle_input_loc().send_keys(text)

    def t_deadtime_button(self):
        """
        点击【截止日期】按钮
        """
        self.t_deadtime_button_loc().click()
    def t_hwrequire_input(self, text):
        """
        输入【作业要求】
        """
        self.t_hwrequire_input_loc().send_keys(text)
    def t_hwcontent_upload(self):
        """
        上传【作业内容】附件
        """
        self.t_hwcontent_upload_loc().click()
        # 需要4个点击，稍后补充
    def t_hwanswer_upload(self):
        """
        上传【作业答案】附件
        """
        self.t_hwanswer_upload_loc().click()
        # 需要4个点击，稍后补充
    def t_release_button(self):
        """
        点击【发布】附件
        """
        self.t_release_button_loc().click()
