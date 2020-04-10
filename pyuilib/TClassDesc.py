# -*- coding:utf-8 -*-
#!/usr/bin/env python3
# @author : Wsy
# @date : 2019/10/5
# @file : TClassDesc
# @version : 1.0.0
# @desc :  Teacher Home goto Class description

from time import sleep
from selenium.webdriver.common.by import By
from pyuilib.TeacherHome import TeacherHome


class TClassDesc(TeacherHome):
    # location
    student_list = (By.CSS_SELECTOR, "a[ng-click='showClassStudent(class.id)']")
    student_num = (By.CSS_SELECTOR, ".panel-heading .ng-scope")


    # 跳转至班级情况-班级学生页面
    def goto_tab_page(self):
        self.find_element(*self.class_info_button).click()
        # sleep(1)
        self.find_element(*self.class_student_button).click()

    # 获取学生列表信息
    def get_student_list(self):
        self.find_element(*self.student_list).click()
        student_num_text = self.find_element(*self.student_num).text
        return student_num_text

    #

