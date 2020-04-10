# -*- coding:utf-8 -*-
#!/usr/bin/env python3
# @author : Wsy
# @date : 2019/9/30
# @file : LoginPage
# @version : 1.0.0
# @desc :  Login page

from selenium.webdriver.common.by import By

from pyuilib.UiBase import UiBase
from pylib.mydriver import browser


class LoginPage(UiBase):
    # path
    uri = "/portal/home.html"
    # location
    teacher_login_button = (By.LINK_TEXT,"老师登录")
    student_login_button = (By.LINK_TEXT,"学生登录")
    username_input = (By.ID,"username")
    password_input = (By.ID,"password")
    submit_button = (By.ID,"submit")


    # 跳转至老师登录页面
    def goto_login(self):
        pass
        # self.open()
        # self.find_element(*self.teacher_login_button).click()
        # sleep(1)
        # assert self.driver.current_url == "http://ci.ytesting.com/teacher/login/login.html" , "goto teacher login page fail"

    # 跳转至学生登录页面
    # def goto_student_login(self):
    #     self.open()
    #     self.find_element(*self.student_login_button).click()
    #     sleep(1)
    #     assert self.driver.current_url == "http://ci.ytesting.com/student/login/login.html" , "goto student login page fail"

     # 登录操作
    def login(self,username,password):
        if username:
            self.find_element(*self.username_input).send_keys(username)
        if password:
            self.find_element(*self.password_input).send_keys(password)

        self.find_element(*self.submit_button).click()

if "__main__" == __name__:
    login = LoginPage(browser())
    login.goto_login()
    login.login("admin","888888")

