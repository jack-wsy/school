# -*- coding:utf-8 -*-
# !/usr/bin/env python3
# @author : Wsy
# @date : 2019/10/5
# @file : TPublishHomework
# @version : 1.0.0
# @desc :  老师已发布作业页面
from time import sleep

from selenium.webdriver.common.by import By

from pylib.mydriver import browser
from pyuilib.TeacherHome import TeacherHome


class TPublishHomework(TeacherHome):

    # 查看学生作业情况
    view_student_grade = (By.XPATH,"//a[@ng-click='trackTask(task)']")
    grade_desc = (By.CSS_SELECTOR,"p[ng-if='taskTrack.summary']")

    def goto_tab_page(self):
        self.find_element(*self.exist_publish_homework).click()

    def get_student_grade(self):
        self.find_elements(*self.view_student_grade)[0].click()
        sleep(3)
        grade_text = self.find_element(*self.grade_desc).text
        return grade_text

if "__main__" == __name__:
    tp = TPublishHomework(browser())
    tp.goto_login()
    tp.login("admin1","888888")
    tp.goto_tab_page()

    print(tp.get_student_grade())
