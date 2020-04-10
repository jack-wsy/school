# -*- coding:utf-8 -*-
#!/usr/bin/env python3
# @author : Wsy
# @date : 2019/10/5
# @file : tc005101
# @version : 1.0.0
# @desc :
from pylib.mydriver import browser
from pyuilib.SMyTask import SMyTask
from pyuilib.THomework import THomework
from pyuilib.TPublishHomework import TPublishHomework


class tc005101:

    def setUp(self):
        self.thomework = THomework(browser())
        self.mytask = SMyTask(browser())
        self.tp = TPublishHomework(browser())

    def steps(self,t_username,s_username):
        self.thomework.goto_login()
        self.thomework.login(t_username, "888888")
        self.thomework.goto_tab_page()
        self.thomework.create_and_publish_homework()
        print(self.thomework.verify_publish_homework())
        verify_text = self.thomework.verify_publish_homework()
        assert "作业已发布给学生" in verify_text,"publish fail"

        self.mytask.goto_login()
        self.mytask.login(s_username, "888888")
        self.mytask.goto_tab_page()
        self.mytask.do_homework()

        self.mytask.driver.refresh()
        grade_lists = self.mytask.get_grade()

        self.tp.goto_login()
        self.tp.login(t_username, "888888")
        self.tp.goto_tab_page()
        assert self.mytask.verify_grade(grade_lists,self.tp.get_student_grade()),"answer view fail"

    def tearDown(self):
        self.thomework.driver.quit()
        self.mytask.driver.quit()
        self.tp.driver.quit()
