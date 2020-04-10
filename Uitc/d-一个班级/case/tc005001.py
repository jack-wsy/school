# -*- coding:utf-8 -*-
# !/usr/bin/env python3
# @author : Wsy
# @date : 2019/10/5
# @file : tc005001
# @version : 1.0.0
# @desc :  tc005001 test case
from pylib.SchoolClassLib import Grade
from pylib.mydriver import browser
from pyuilib.TClassDesc import TClassDesc
from pylib.SchoolTeacherLib import Teacher
from robot.api import logger

class tc005001():

    def setUp(self):
        self.scl = Grade()
        self.id = self.scl.get_grade_id()
        self.th = Teacher()
        self.tcd = TClassDesc(browser())
        self.phonenumber = self.th.create_phone_or_idcard("0")
        self.idcard = self.th.create_phone_or_idcard("1")


    def steps(self,username):
        result = self.th.add_teacher(username, "测试", 1, self.phonenumber, "jcy@123.com", self.idcard, self.id)
        assert result['retcode'] == 0

        self.tcd.goto_login()
        self.tcd.login(username, "888888")
        list_infos = self.tcd.get_list_info()
        assert ["松勤学院00698","测试","初中数学","0"] == list_infos,"teacher's info error"

        course_list = self.tcd.get_course_info()
        assert ["0","0"] == course_list,"course info error"

        self.tcd.goto_tab_page()
        student_num = self.tcd.get_student_list()
        assert "0" == student_num,"student number error"

    def tearDown(self):
        self.th.delete_teacher_all()
        self.tcd.driver.quit()

if "__main__" == __name__:
    t = tc005001()
    t.setUp()
    t.steps("admin","888888")
    t.tearDown()