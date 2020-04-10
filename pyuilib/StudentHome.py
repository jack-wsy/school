# -*- coding:utf-8 -*-
# !/usr/bin/env python3
# @author : Wsy
# @date : 2019/10/1
# @file : StudentHome
# @version : 1.0.0
# @desc :  Student Home Page
from time import sleep
from selenium.webdriver.common.by import By
from pyuilib.LoginPage import LoginPage
from pylib.mydriver import browser


class StudentHome(LoginPage):
    # path
    # uri = "/student/index.html#/home"
    # location

    # 学生列表信息
    student_list_infos = (By.XPATH,"//td/span[@class='ng-binding']")
    student_list_classes = (By.XPATH,"//strong[@class='ng-binding']")
    # 错题库信息
    error_question_button = (By.CSS_SELECTOR,"a[href='#/yj_wrong_questions']>li")


    cat_notic_button = (By.CSS_SELECTOR,".badge.badge-yellow.ng-binding")
    homework_select = (By.CSS_SELECTOR,"a.ng-binding")


    # 跳转至学生登录页面
    def goto_login(self):

        self.open()
        self.find_element(*self.student_login_button).click()
        sleep(1)
        assert self.driver.current_url == "http://ci.ytesting.com/student/login/login.html" , "goto student login page fail"

    # 获取学生列表信息
    def get_student_list_infos(self):
        list_eles = self.find_elements(*self.student_list_infos)
        infos = []
        for one in list_eles:
            infos.append(one.text)

        return infos

    # 获取学生上课信息
    def get_student_classes(self):
        classes_eles = self.find_elements(*self.student_list_classes)
        classes = []
        for one in classes_eles:
            classes.append(one.text)

        return classes

    # 跳转至对应导航页
    def goto_tab_page(self):
        pass

    # 完成作业
    def do_homework(self):
        self.find_element(*self.cat_notic_button).click()
        self.find_element(*self.homework_select).click()
        self.find_element(*self.goto_homework).click()
        answer = self.find_elements(*self.select_answer)
        for one in answer:
            one.click()

        self.find_element(*self.submit_homework).click()
        sleep(1)
        self.find_element(*self.homework_last).click()



if "__main__" == __name__:
    th = StudentHome(browser())
    th.goto_login()
    th.login("admin", 888888)
    th.do_homework()
    # print(th.get_student_list_infos())
    # print(th.get_student_classes())
    # print(th.get_error_question())
    # th.goto_class_student()
    # print(th.get_student_list())
