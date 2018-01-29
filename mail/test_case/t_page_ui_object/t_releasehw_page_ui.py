# -*- coding:utf-8 -*-

from base import Base

class TReleaseHw(Base):
    """
    用户: 教师
    页面 UI 对象(PUO): 发布作业 页面 UI
    """
    def t_hwtitle_input_loc(self):
        """
        定位到【作业标题】输入栏
        :return: WebDriver 对象
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': '',
            'android_value': ''
        })
    def t_deadtime_button_loc(self):
        """
        定位到【截止日期】按钮
        :return: WebDriver 对象
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': '',
            'android_value': ''
        })
    def t_hwrequire_input_loc(self):
        """
        定位到【作业要求】输入栏
        :return: WebDriver 对象
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': '',
            'android_value': ''
        })
    def t_hwcontent_upload_loc(self):
        """
        定位到【作业内容】文件上传页面
        :return: WebDriver 对象
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': '',
            'android_value': ''
        })
    def t_hwanswer_upload_loc(self):
        """
        定位到【作业答案】文件上传页面
        :return: WebDriver 对象
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': '',
            'android_value': ''
        })
    def t_hwobject_button_loc(self):
        """
        定位到【发布对象】按钮
        :return: WebDriver 对象
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': '',
            'android_value': ''
        })
    def t_release_button_loc(self):
        """
        定位到【发布】按钮
        :return: WebDriver 对象
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': '',
            'android_value': ''
        })
