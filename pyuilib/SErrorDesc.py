# -*- coding:utf-8 -*-
#!/usr/bin/env python3
# @author : Wsy
# @date : 2019/10/5
# @file : SErrorDesc
# @version : 1.0.0
# @desc :  Student Error questing
from selenium.webdriver.common.by import By
from pyuilib.StudentHome import StudentHome


class SErrorDesc(StudentHome):
    # location

    # 错题库为空时获取相关信息
    error_question_info = (By.CSS_SELECTOR, ".fa.fa-bug+span")

    def goto_tab_page(self):
        self.find_element(*self.error_question_button).click()

    # 获取错题库信息
    def get_error_question(self):
        error_question = self.find_element(*self.error_question_info).text
        return error_question
