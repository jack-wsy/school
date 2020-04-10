# -*- coding:utf-8 -*-
# !/usr/bin/env python3
# @author : Wsy
# @date : 2019/9/30
# @file : TeacherHome
# @version : 1.0.0
# @desc :  Teacher Home Page
from time import sleep, strftime

from selenium.webdriver.common.by import By

from pyuilib.LoginPage import LoginPage
from pylib.mydriver import browser


class TeacherHome(LoginPage):
    # path
    # uri = "/teacher/index.html#/home"
    # location

    # 学校，姓名，学科，金币
    school_name = (By.CSS_SELECTOR,".ng-scope.ng-binding")
    list_infos = (By.XPATH,"//a[@class='ng-binding']")
    course_infos = (By.XPATH,"//strong[@class='ng-binding']")

    # 班级情况 - 班级学生
    class_info_button = (By.LINK_TEXT, "班级情况")
    class_student_button = (By.CSS_SELECTOR, ".fa.fa-sitemap.fa-fw+.menu-title")

    # 已发布作业
    exist_publish_homework = (By.CSS_SELECTOR, ".badge-blue")

    # 作业 - 创建作业
    work_button = (By.LINK_TEXT, "作业")
    create_button = (By.CSS_SELECTOR,"a[ng-click='show_page_addexam()'] span")

    # 跳转至老师登录页面
    def goto_login(self):

        self.open()
        self.find_element(*self.teacher_login_button).click()
        sleep(1)
        assert self.driver.current_url == "http://ci.ytesting.com/teacher/login/login.html" , "goto teacher login page fail"

    # 获取学校，姓名，学科，金币 状态
    def get_list_info(self):
        list_info = []
        school_name = self.find_element(*self.school_name).text
        list_info.append(school_name)
        list_eles = self.find_elements(*self.list_infos)
        for one in list_eles:
            list_info.append(one.text)

        return list_info

    # 获取微课，已发布作业信息状态
    def get_course_info(self):
        course_info = []
        course_eles = self.find_elements(*self.course_infos)
        for one in course_eles:
            course_info.append(one.text)

        return course_info

    # 进入导航相关页
    def goto_tab_page(self):
        pass
        # self.find_element(*self.class_info_button).click()
        # sleep(1)
        # self.find_element(*self.class_student_button).click()



    # 发布作业
    # def publish_work(self,number):
    #     pass
        # 跳转至创建作业页面
        # self.find_element(*self.work_button).click()
        # self.find_element(*self.create_button).click()
        # 输入作业名，选择题目页面
        # self.find_element(*self.input_homework_name).send_keys(strftime("%Y%m%d %H%M%S"))
        # self.find_element(*self.select_question_button).click()
        # sleep(1)
        # 进入frame框架，选择作业发布题目
        # frame = self.find_element(*self.frame_Id)
        # self.driver.switch_to.frame(frame)
        # self.find_element(*self.exception_submit_button).click()
        # but_eles = self.find_elements(*self.add_question_buttons)
        # for one in range(number):
        #     but_eles[one].click()
        #
        # self.find_element(*self.add_submit_button).click()
        # self.driver.switch_to.default_content()
        # sleep(1)
        # 发布作业
        # self.find_element(*self.publish_submit_button).click()
        # sleep(1)
        # # 新窗口页面发布
        # window_handle = self.driver.current_window_handle
        # self.find_element(*self.give_student_homework).click()
        # sleep(3)
        # handles = self.driver.window_handles
        # for one in handles:
        #     if one != window_handle:
        #         self.driver.switch_to.window(one)
        # # 选择发布的学生，发布作业
        # self.find_element(*self.select_student_checkbox).click()
        # self.find_element(*self.submit_button_success).click()
        # self.find_element(*self.publish_submit_success).click()


if "__main__" == __name__:
    # browser().switch_to.window()

    th = TeacherHome(browser())
    th.goto_login()
    th.login("admin1",888888)
    th.publish_work(3)
    # print(th.get_course_info())
    # print(th.get_list_info())
    # th.goto_class_student()
    # print(th.get_student_list())
