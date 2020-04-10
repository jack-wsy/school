# -*- coding:utf-8 -*-
#!/usr/bin/env python3
# @author : Wsy
# @date : 2019/10/5
# @file : SMyTask
# @version : 1.0.0
# @desc :  Student My Task page
from time import sleep
from selenium.webdriver.common.by import By

from pylib.mydriver import browser
from pyuilib.StudentHome import StudentHome
from pyuilib.TPublishHomework import TPublishHomework


class SMyTask(StudentHome):


    goto_homework = (By.CSS_SELECTOR, "button[ng-click='viewTask(taskTrack)']")
    select_answer = (By.XPATH, "//div[@class='btn-group']/button[last()]")
    submit_homework = (By.CSS_SELECTOR, ".btn.btn-blue.btn-outlined.btn-square")
    homework_last = (By.XPATH, "(//button[@class='btn btn-primary'])[last()]")

    # 获取作业完成情况
    view_task_desc = (By.CSS_SELECTOR,".btn-xs")
    sum_grade_text = (By.CSS_SELECTOR,"div.col-lg-12.pull-left.ng-scope>.ng-binding")

    def goto_tab_page(self):
        self.find_element(*self.cat_notic_button).click()
        self.find_element(*self.homework_select).click()

    # 完成作业
    def do_homework(self):

        self.find_element(*self.goto_homework).click()
        answer = self.find_elements(*self.select_answer)
        for one in answer:
            one.click()

        self.find_element(*self.submit_homework).click()
        sleep(1)
        self.find_element(*self.homework_last).click()

    def get_grade(self):
        self.find_element(*self.view_task_desc).click()
        grade_eles = self.find_elements(*self.sum_grade_text)
        grade_lists = []
        for one in grade_eles:
            grade_lists.append(one.text)

        return grade_lists

    def verify_grade(self,grade_lists,teacher_view_grade):
        for one in range(3):
            if grade_lists[one] not in teacher_view_grade:
                return False

        return True

if "__main__" == __name__:
    mytask = SMyTask(browser())
    mytask.goto_login()
    mytask.login("admin","888888")
    mytask.goto_tab_page()
    mytask.do_homework()
    mytask.driver.refresh()
    grade_lists = mytask.get_grade()
    tp = TPublishHomework(browser())
    tp.goto_login()
    tp.login("admin1", "888888")
    tp.goto_tab_page()
    print(mytask.verify_grade(grade_lists,tp.get_student_grade()))
