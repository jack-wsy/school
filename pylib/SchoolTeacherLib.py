# -*- coding:utf-8 -*-
# !/usr/bin/env python3
# @author : Wsy
# @date : 2019/9/29
# @file : SchoolTeacherLib
# @version : 1.0.0
# @desc :  School Teacher Lib
import json
from pprint import pprint
from random import randint

import requests
from pylib.Base import Base

class Teacher(Base):
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    # 列出老师
    def get_teacher(self,subjectid = None,action = "search_with_pagenation"):
        result = requests.get(self.get_teacher_address(),params={
            "vcode" : self.get_vcode(),
            "action" : action,
            "subjectid" : subjectid
        }).json()

        return result

    # 添加老师
    def add_teacher(self,username,realname,subjectid,phonenumber,email,idcardnumber,*args,action = "add"):
        classlist = []
        for one in args:
            id_dict = {"id":one}
            classlist.append(id_dict)
        result = requests.post(self.get_teacher_address(),data={
            "vcode" : self.get_vcode(),
            "action" : action,
            "username": username,
            "realname" : realname,
            "subjectid" : subjectid,
            "classlist" : json.dumps(classlist),
            "phonenumber" : phonenumber,
            "email" : email,
            "idcardnumber" : int(idcardnumber)
        }).json()

        return result

    # 修改老师
    def modify_teacher(self,teacherId,*args,realname = None,subjectid = None,
                       phonenumber = None,email = None,
                       idcardnumber = None,action = "modify"):
        classlist = []
        for one in args:
            id_dict = {"id" : one}
            classlist.append(id_dict)
        result = requests.put(self.get_teacher_address() + "/%s" %teacherId,data={
            "vcode" : self.get_vcode(),
            "action" : action,
            "realname" : realname,
            "subjectid" : subjectid,
            "classlist" : json.dumps(classlist),
            "phonenumber" : phonenumber,
            "email" : email,
            "idcardnumber" : idcardnumber
        }).json()

        return result

    # 删除老师
    def delete_teacher(self,teacherId):
        result = requests.delete(self.get_teacher_address() + "/%s" %teacherId,data={
            "vcode" : self.get_vcode()
        }).json()

        return result

    # 删除所有老师
    def delete_teacher_all(self):
        teacherList = self.get_teacher()["retlist"]
        for one in teacherList:
            self.delete_teacher(one["id"])

        again_teacher_list = self.get_teacher()["retlist"]
        if again_teacher_list:
            raise Exception("teacher is not empty")


    # 判断老师是否在返回列表中
    def verify_teacher(self,subjectId,*args,**kwargs):
        classlist = []
        for one in args:
            id_dict = {"id" : one}
            classlist.append(id_dict)
        kwargs["teachclasslist"] = classlist
        result = self.get_teacher(subjectId)["retlist"]
        for one in result:
            if kwargs == one:
                return True
        return False
    # 统计老师登录名数量
    def sum_loginname(self,username):
        sum = 0
        result = self.get_teacher()["retlist"]
        for one in result:
            if one["username"] == username:
                sum += 1
        return sum

    # phonenumber生成,idcardnumber生成
    def create_phone_or_idcard(self, type):
        if "0" == str(type):
            phonenumber = str(randint(10000000000, 99999999999))
            return phonenumber
        elif "1" == str(type):
            idcardnumber = str(randint(100000000000000000, 999999999999999999))
            return idcardnumber
        else:
            return None

if "__main__" == __name__:
    t = Teacher()
    # pprint(t.add_teacher("admin1","测试","1","13451813409","jcy@123.com","3209251983090987899",233363))
    # pprint(t.modify_teacher(65186,232926,232927,realname="测试修改",subjectid=1))
    # pprint(t.delete_teacher(64819))
    # t.delete_teacher_all()
    pprint(t.get_teacher(),indent=2)