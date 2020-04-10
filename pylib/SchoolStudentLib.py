# -*- coding:utf-8 -*-
# !/usr/bin/env python3
# @author : Wsy
# @date : 2019/9/29
# @file : SchoolStudentLib
# @version : 1.0.0
# @desc :  School Student Lib
from pprint import pprint
from random import randint

import requests

from pylib.Base import Base

class Student(Base):
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    # 列出学生
    def get_student(self,page = None,action = "search_with_pagenation"):
        result = requests.get(self.get_student_address(),params={
            "vcode" : self.get_vcode(),
            "action" : action,
            "page" : page
        }).json()

        return result

    # 添加学生信息
    def add_student(self,username,realname,gradeId,classId,phonenumber,action = "add"):
        result = requests.post(self.get_student_address(),data={
            "vcode" : self.get_vcode(),
            "action" : action,
            "username" : username,
            "realname" : realname,
            "gradeid" : gradeId,
            "classid" : classId,
            "phonenumber" : phonenumber
        }).json()

        return result

    # 修改学生信息
    def modify_student(self,studentId,realname=None,phonenumber=None,action = "modify"):
        result = requests.put(self.get_student_address() + "/%s" %studentId,data={
            "vcode" : self.get_vcode(),
            "action" : action,
            "realname" : realname,
            "phonenumber" : phonenumber
        }).json()

        return result

    # 删除学生
    def delete_student(self,studentId):
        result = requests.delete(self.get_student_address() + "/%s" %studentId,data={
            "vcode" : self.get_vcode()
        }).json()

        return result

    # 删除所有学生
    def delete_student_all(self):
        studentList = self.get_student()["retlist"]
        for one in studentList:
            self.delete_student(one["id"])
        again_student_list = self.get_student()["retlist"]
        if again_student_list:
            raise Exception("Students are not empty")

    # phonenumber生成,idcardnumber生成
    def create_phone(self, type):
        if "0" == str(type):
            phonenumber = str(randint(10000000000, 99999999999))
            return phonenumber
        else:
            return None

    def verify_student(self,id):
        result = self.get_student()["retlist"]
        for one in result:
            if one["id"] == int(id):
                return True
        return False

    def get_student_id(self):
        result = self.get_student()["retlist"][0]
        return result["id"]

if "__main__" == __name__:
    "231640"
    s = Student()
    # pprint(s.add_student("admin","测试学生","1","233363","13451813456"))
    # pprint(s.modify_student(28854,realname="测试学生修改"))
    # pprint(s.delete_student(28854))
    pprint(s.delete_student_all())
    pprint(s.get_student())
