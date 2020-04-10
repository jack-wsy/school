# -*- coding:utf-8 -*-
#!/usr/bin/env python3
# @author : Wsy
# @date : 2019/10/5
# @file : tc005081
# @version : 1.0.0
# @desc :
from pylib.SchoolClassLib import Grade
from pylib.SchoolStudentLib import Student
from pylib.mydriver import browser
from pyuilib.SErrorDesc import SErrorDesc


class tc005081:
    def setUp(self):
        self.scl = Grade()
        self.id = self.scl.get_grade_id()
        self.st = Student()
        self.sed = SErrorDesc(browser())
        self.phonenumber = self.st.create_phone("0")

    def steps(self):
        result = self.st.add_student("admin","测试学生",1,self.id,self.phonenumber)
        assert result['retcode'] == 0

        self.sed.goto_login()
        self.sed.login("admin","888888")
        student_info = self.sed.get_student_list_infos()
        print(student_info)
        assert "测试学生" in student_info and "松勤学院00698" in student_info,"student info error"

        student_classes = self.sed.get_student_classes()
        assert ["0","0"] == student_classes,"student classes error"

        self.sed.goto_tab_page()
        question_error = self.sed.get_error_question()
        assert "您尚未有错题入库哦" == question_error,"error questiong view"

    def tearDown(self):
        self.st.delete_student_all()
        self.sed.driver.quit()