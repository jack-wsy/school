# -*- coding:utf-8 -*-
#!/usr/bin/env python3
# @author : Wsy
# @date : 2019/10/5
# @file : THomework
# @version : 1.0.0
# @desc :  Teacher Home goto Teacher publish homework page
from time import strftime, sleep
from selenium.webdriver.common.by import By

from pylib.mydriver import browser
from pyuilib.TeacherHome import TeacherHome


class THomework(TeacherHome):

    # location

    # 题库选择题目按钮 - 输入作业名称按钮
    select_question_button = (By.ID, "btn_pick_question")
    input_homework_name = (By.ID, "exam_name_text")

    # 选择需要发布作业的题目
    frame_Id = (By.ID, "pick_questions_frame")
    exception_submit_button = (By.CSS_SELECTOR, "div.bootstrap-dialog-footer button.btn.btn-default")
    add_question_buttons = (By.CSS_SELECTOR, ".btn-xs.btn-green.btn-outlined.btn_pick_question")
    add_submit_button = (By.CSS_SELECTOR, ".btn.btn-blue")



    # 发布作业
    publish_submit_button = (By.ID, "btn_submit")
    give_student_homework = (By.XPATH, "(//div/button[@class='btn btn-primary'])[last()]")
    select_student_checkbox = (By.CLASS_NAME, "myCheckbox")
    submit_button_success = (By.CSS_SELECTOR, ".btn.btn-blue.btn-outlined")
    publish_submit_success = (By.CSS_SELECTOR, ".btn.btn-primary")

    # 判断作业发布成功
    verify_publish_success = (By.CLASS_NAME,"bootstrap-dialog-message")

    # 进入创建作业页面
    def goto_tab_page(self):
        self.find_element(*self.work_button).click()
        self.find_element(*self.create_button).click()

    # 进入题库选择题目页面
    def open_publish_homework(self):
        self.find_element(*self.input_homework_name).send_keys(strftime("%Y%m%d %H%M%S"))
        self.find_element(*self.select_question_button).click()

    # 选择发布的作业
    def select_publish_homework(self,number):
        # 进入frame框架
        frame = self.find_element(*self.frame_Id)
        self.driver.switch_to.frame(frame)
        # 取消异常按钮
        if self.is_element(*self.exception_submit_button):
            self.find_element(*self.exception_submit_button).click()
        # 选择要添加的题目
        sleep(1)
        but_eles = self.find_elements(*self.add_question_buttons)
        for one in range(number):
            but_eles[one].click()
        self.find_element(*self.add_submit_button).click()
        self.driver.switch_to.default_content()

    # 发布添加的作业
    def publish_homework(self):
        # 发布作业
        self.find_element(*self.publish_submit_button).click()
        sleep(1)
        # 新窗口页面发布
        window_handle = self.driver.current_window_handle
        self.find_element(*self.give_student_homework).click()
        sleep(1)
        handles = self.driver.window_handles
        for one in handles:
            if one != window_handle:
                self.driver.switch_to.window(one)
        # 选择发布的学生，发布作业
        self.find_element(*self.select_student_checkbox).click()
        self.find_element(*self.submit_button_success).click()
        self.find_element(*self.publish_submit_success).click()

    # 验证作业发布成功
    def verify_publish_homework(self):
        pub_bool = self.find_element(*self.verify_publish_success).text

        return pub_bool

    # 创建并发布作业
    def create_and_publish_homework(self):
        self.goto_tab_page()
        sleep(1)
        self.open_publish_homework()
        sleep(1)
        self.select_publish_homework(3)
        sleep(1)
        self.publish_homework()

if "__main__" == __name__:
    thomework = THomework(browser())
    thomework.goto_login()
    thomework.login("admin1",888888)
    thomework.goto_tab_page()
    thomework.create_and_publish_homework()
    if "作业已发布给学生" in thomework.verify_publish_homework():
        print("pass")
